#!/usr/bin/env python3


#
# Nokia/Alcatel-Lucent router backup configuration tool
#
# Features:
# - Unpack/repack .cfg files generated from the backup and restore functionnality
#   in order to modify the full router configuration
# - Decrypt/encrypt the passwords/secret values present in the configuration
#
# Blog post: https://0x41.cf/reversing/2019/10/08/unlocking-nokia-g240wa.html
#
# Released under the MIT License (http://opensource.org/licenses/MIT)
# Copyright (c) Sami Alaoui Kendil (thedroidgeek)
#


import sys
import zlib
import struct
import base64
import binascii
import datetime


big_endian = True
encrypted_cfg = False


def u32(val):
    return struct.unpack('>I' if big_endian else '<I', val)[0]

def p32(val):
    return struct.pack('>I' if big_endian else '<I', val)

def checkendian(cfg):
    if (cfg[0:4] == b'\x00\x12\x31\x23'):
        return True
    elif (cfg[0:4] == b'\x23\x31\x12\x00'):
        return False
    else:
        return None


class RouterCrypto:

    def __init__(self):

        from Crypto.Cipher import AES

        # key and IV for AES
        key = '3D A3 73 D7 DC 82 2E 2A 47 0D EC 37 89 6E 80 D7 2C 49 B3 16 29 DD C9 97 35 4B 84 03 91 77 9E A4'
        iv  = 'D0 E6 DC CD A7 4A 00 DF 76 0F C0 85 11 CB 05 EA'

        # create AES-128-CBC cipher
        self.cipher = AES.new(bytes(bytearray.fromhex(key)), AES.MODE_CBC, bytes(bytearray.fromhex(iv)))

    def decrypt(self, data):

        output = self.cipher.decrypt(data)

        # remove PKCS#7 padding
        return output[:-ord(output[-1:])]

    def encrypt(self, data):

        # add PKCS#7 padding for 128-bit AES
        pad_num = (16 - (len(data) % 16))
        data += chr(pad_num).encode() * pad_num

        return self.cipher.encrypt(data)


#
# unpack xml from cfg
#

if (len(sys.argv) == 3 and sys.argv[1] == '-u'):

    # line feed
    print('')

    # read the cfg file
    cf = open(sys.argv[2], 'rb')
    cfg_data = cf.read()

    # check cfg file magic (0x123123) and determine endianness
    big_endian = checkendian(cfg_data)

    if big_endian == None:

        # check if config is encrypted
        decrypted = None
        try:
            # decrypt and check validity
            decrypted = RouterCrypto().decrypt(cfg_data)
            big_endian = checkendian(decrypted)
        except ValueError:
            pass

        # if decryption failed, or still invalid, bail out
        if big_endian == None:
            print('invalid cfg file/magic :(\n')
            exit()

        # set decrypted cfg buffer and encryption flag
        print('-> encrypted cfg detected')
        cfg_data = decrypted
        encrypted_cfg = True

    # log endianness
    if big_endian:
        print('-> big endian CPU detected')
    else:
        print('-> little endian CPU detected')

    # get fw_magic (unknown, could be fw version/compile time, hw serial number, etc.)
    fw_magic = u32(cfg_data[0x10:0x14])
    print('-> fw_magic = ' + hex(fw_magic))

    # get the size of the compressed data
    data_size = u32(cfg_data[4:8])

    # get the compressed data
    compressed = cfg_data[0x14 : 0x14 + data_size]

    # get the checksum of the compressed data
    checksum = u32(cfg_data[8:12])

    # verify the checksum
    if (binascii.crc32(compressed) & 0xFFFFFFFF != checksum):
        print('\nCRC32 checksum failed :(\n')
        exit()

    # unpack the config
    xml_data = zlib.decompress(compressed)

    # output the xml file
    out_filename = 'config-%s.xml' % datetime.datetime.now().strftime('%d%m%Y-%H%M%S')
    of = open(out_filename, 'wb')
    of.write(xml_data)

    print('\nunpacked as: ' + out_filename)

    print('\n# repack with:')
    print('%s %s %s %s\n' % (sys.argv[0], ('-pb' if big_endian else '-pl') + ('e' if encrypted_cfg else ''), out_filename, hex(fw_magic)))

    cf.close()
    of.close()


#
# generate cfg from xml
#

elif (len(sys.argv) == 4 and (sys.argv[1][:3] == '-pb' or sys.argv[1][:3] == '-pl')):

    fw_magic = 0

    try:
        # parse hex string
        fw_magic = int(sys.argv[3], 16)
        # 32-bit check
        p32(fw_magic)
    except:
        print('\ninvalid magic value specified (32-bit hex)\n')
        exit()

    big_endian = sys.argv[1][:3] == '-pb'
    encrypted_cfg = sys.argv[1][3:] == 'e'

    out_filename = 'config-%s.cfg' % datetime.datetime.now().strftime('%d%m%Y-%H%M%S')

    # read the xml file
    xf = open(sys.argv[2], 'rb')
    xml_data = xf.read()
    xf.close()

    # compress using default zlib compression
    compressed = zlib.compress(xml_data)

    ## construct the header ##
    # magic
    cfg_data = p32(0x123123)
    # size of compressed data
    cfg_data += p32(len(compressed))
    # crc32 checksum
    cfg_data += p32(binascii.crc32(compressed) & 0xFFFFFFFF)
    # size of xml file
    cfg_data += p32(len(xml_data) + 1)
    # fw_magic
    cfg_data += p32(fw_magic)

    # add the compressed xml
    cfg_data += compressed

    # encrypt if necessary
    if encrypted_cfg:
        cfg_data = RouterCrypto().encrypt(cfg_data)

    # write the cfg file
    of = open(out_filename, 'wb')
    of.write(cfg_data)
    of.close()

    print('\npacked as: ' + out_filename + '\n')


#
# decrypt/encrypt secret value
#

elif (len(sys.argv) == 3 and (sys.argv[1] == '-d' or sys.argv[1] == '-e')):

    decrypt_mode = sys.argv[1] == '-d'

    if decrypt_mode:

        # base64 decode + AES decrypt
        print('\ndecrypted: ' + RouterCrypto().decrypt(base64.b64decode(sys.argv[2])).decode('UTF-8') + '\n')

    else:

        # AES encrypt + base64 encode
        print('\nencrypted: ' + base64.b64encode(RouterCrypto().encrypt(sys.argv[2].encode())).decode('UTF-8') + '\n')


else:

    print('\n#\n# Nokia/Alcatel-Lucent router backup configuration tool\n#\n')
    print('# unpack (cfg to xml)\n')
    print(sys.argv[0] + ' -u config.cfg\n')
    print('# pack (xml to cfg)\n')
    print(sys.argv[0] + ' -pb  config.xml 0x13377331 # big endian, no encryption, fw_magic = 0x13377331')
    print(sys.argv[0] + ' -pl  config.xml 0x13377331 # little endian, ...')
    print(sys.argv[0] + ' -pbe config.xml 0x13377331 # big endian, with encryption, ...')
    print(sys.argv[0] + ' -ple config.xml 0x13377331 # ...\n')
    print('# decrypt/encrypt secret values within xml (ealgo="ab")\n')
    print(sys.argv[0] + ' -d OYdLWUVDdKQTPaCIeTqniA==')
    print(sys.argv[0] + ' -e admin\n')