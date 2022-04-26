# pylint: disable=C0111
from qutebrowser.config.configfiles import ConfigAPI  # noqa: F401
from qutebrowser.config.config import ConfigContainer  # noqa: F401
config: ConfigAPI = config  # noqa: F821 pylint: disable=E0602,C0103
c: ConfigContainer = c  # noqa: F821 pylint: disable=E0602,C0103




## Automatically start playing `<video>` elements. Note: On Qt < 5.11,
## this option needs a restart and does not support URL patterns.
## Type: Bool
c.content.autoplay = False


## Enable support for the HTML 5 web application cache feature. An
## application cache acts like an HTTP cache in some sense. For documents
## that use the application cache via JavaScript, the loader engine will
## first ask the application cache for the contents, before hitting the
## network.
## Type: Bool
c.content.cache.appcache = True


## Maximum number of pages to hold in the global memory page cache. The
## page cache allows for a nicer user experience when navigating forth or
## back to pages in the forward/back history, by pausing and resuming up
## to _n_ pages. For more information about the feature, please refer to:
## http://webkit.org/blog/427/webkit-page-cache-i-the-basics/
## Type: Int
c.content.cache.maximum_pages = 0


## Size (in bytes) of the HTTP network cache. Null to use the default
## value. With QtWebEngine, the maximum supported value is 2147483647 (~2
## GB).
## Type: Int
c.content.cache.size = None


## Allow websites to read canvas elements. Note this is needed for some
## websites to work properly.
## Type: Bool
c.content.canvas_reading = True


## Default encoding to use for websites. The encoding must be a string
## describing an encoding such as _utf-8_, _iso-8859-1_, etc.
## Type: String
# c.content.default_encoding = 'iso-8859-1'
c.content.default_encoding = 'utf-8'


## Allow websites to share screen content. On Qt < 5.10, a dialog box is
## always displayed, even if this is set to "true".
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
c.content.desktop_capture = 'ask'


## Try to pre-fetch DNS entries to speed up browsing.
## Type: Bool
# c.content.dns_prefetch = True
c.content.dns_prefetch = True


## Expand each subframe to its contents. This will flatten all the frames
## to become one scrollable page.
## Type: Bool
# c.content.frame_flattening = False
c.content.frame_flattening = False


# Set fullscreen notification overlay timeout in milliseconds. If set to
# 0, no overlay will be displayed.
# Type: Int
c.content.fullscreen.overlay_timeout = 3000


## Allow websites to request geolocations.
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
c.content.geolocation = 'ask'


## Custom headers for qutebrowser HTTP requests.
## Type: Dict
c.content.headers.custom = {}


## Value to send in the `DNT` header. When this is set to true,
## qutebrowser asks websites to not track your identity. If set to null,
## the DNT header is not sent at all.
## Type: Bool
c.content.headers.do_not_track = True


## When to send the Referer header. The Referer header tells websites
## from which website you were coming from when visiting them. No restart
## is needed with QtWebKit.
## Type: String
## Valid values:
##   - always: Always send the Referer.
##   - never: Never send the Referer. This is not recommended, as some sites may break.
##   - same-domain: Only send the Referer for the same domain. This will still protect your privacy, but shouldn't break any sites. With QtWebEngine, the referer will still be sent for other domains, but with stripped path information.
c.content.headers.referer = 'same-domain'


## Enable host blocking.
## Type: Bool
# c.content.host_blocking.enabled = True
c.content.blocking.enabled = True


## User agent to send. Unset to send the default. Note that the value
## read from JavaScript is always the global value.
## Type: String
# c.content.headers.user_agent = None
#
# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
#
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://accounts.google.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://docs.google.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://drive.google.com/*')
# content.blocking.method = both
c.content.blocking.method = 'auto'


## Value to send in the `Accept-Language` header. Note that the value
## read from JavaScript is always the global value.
## Type: String
# c.content.headers.accept_language = 'en-US,en'
#
# Block subdomains of blocked hosts. Note: If only a single subdomain is
# blocked but should be allowed, consider using
# `content.blocking.whitelist` instead.
# Type: Bool
c.content.blocking.hosts.block_subdomains = True


# List of URLs to ABP-style adblocking rulesets.  Only used when Brave's
# ABP-style adblocker is used (see `content.blocking.method`).  You can
# find an overview of available lists here:
# https://adblockplus.org/en/subscriptions - note that the special
# `subscribe.adblockplus.org` links aren't handled by qutebrowser, you
# will instead need to find the link to the raw `.txt` file (e.g. by
# extracting it from the `location` parameter of the subscribe URL and
# URL-decoding it).
# Type: List of Url
c.content.blocking.adblock.lists = [


## Store cookies. Note this option needs a restart with QtWebEngine on Qt
## < 5.9.
## Type: Bool
# c.content.cookies.store = True
    # AdBlock sources
    'https://easylist.to/easylist/easylist.txt',
    'https://easylist.to/easylist/easyprivacy.txt'
    # uBlock sources
    'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances.txt',
    'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badlists.txt',
    'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt',
    'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt',
    'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2020.txt',
    'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2021.txt',
    'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/lan-block.txt',
    'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt',
    'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resource-abuse.txt',
    'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt',
]
# List of URLs to host blocklists for the host blocker.  Only used when
# the simple host-blocker is used (see `content.blocking.method`).  The
# file can be in one of the following formats:  - An `/etc/hosts`-like
# file - One host per line - A zip-file of any of the above, with either
# only one file, or a file   named `hosts` (with any extension).  It's
# also possible to add a local file or directory via a `file://` URL. In
# case of a directory, all files in the directory are read as adblock
# lists.  The file `~/.config/qutebrowser/blocked-hosts` is always read
# if it exists.
# Type: List of Url
# c.content.blocking.hosts.lists = [


## Show javascript alerts.
## Type: Bool
c.content.javascript.alert = True


## Allow JavaScript to close tabs.
## Type: Bool
c.content.javascript.can_close_tabs = False


## Allow JavaScript to open new tabs without user interaction.
## Type: Bool
c.content.javascript.can_open_tabs_automatically = False


## Enable JavaScript.
## Type: Bool
c.content.javascript.enabled = True


## Log levels to use for JavaScript console logging messages. When a
## JavaScript message with the level given in the dictionary key is
## logged, the corresponding dictionary value selects the qutebrowser
## logger to use. On QtWebKit, the "unknown" setting is always used.
## Type: Dict
# c.content.javascript.log = {'unknown': 'debug', 'info': 'debug', 'warning': 'debug', 'error': 'debug'}
c.content.javascript.log = {
    "unknown": "debug",
    "info": "debug",
    "warning": "debug",
    "error": "debug",
}


## Use the standard JavaScript modal dialog for `alert()` and
## `confirm()`.
## Type: Bool
c.content.javascript.modal_dialog = False


## Show javascript prompts.
## Type: Bool
c.content.javascript.prompt = True



## Allow locally loaded documents to access other local URLs.
## Type: Bool
c.content.local_content_can_access_file_urls = True


## Allow locally loaded documents to access remote URLs.
## Type: Bool
c.content.local_content_can_access_remote_urls = False


## Enable support for HTML 5 local storage and Web SQL.
## Type: Bool
c.content.local_storage = True


## Allow websites to record audio/video.
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
# c.content.media_capture = 'ask'


## Allow websites to lock your mouse pointer.
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
c.content.mouse_lock = 'ask'


## Automatically mute tabs. Note that if the `:tab-mute` command is used,
## the mute status for the affected tab is now controlled manually, and
## this setting doesn't have any effect.
## Type: Bool
c.content.mute = False


## Netrc-file for HTTP authentication. If unset, `~/.netrc` is used.
## Type: File
c.content.netrc_file = None


## Allow websites to show notifications.
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
c.content.notifications.enabled = 'ask'


# What notification presenter to use for web notifications. Note that
# not all implementations support all features of notifications: - With
# PyQt 5.14, any setting other than `qt` does not support  the `click`
# and   `close` events, as well as the `tag` option to replace existing
# notifications. - The `qt` and `systray` options only support showing
# one notification at the time   and ignore the `tag` option to replace
# existing notifications. - The `herbe` option only supports showing one
# notification at the time and doesn't   show icons. - The `messages`
# option doesn't show icons and doesn't support the `click` and
# `close` events.
# Type: String
# Valid values:
#   - auto: Tries `libnotify`, `systray` and `messages`, uses the first one available without showing error messages.
#   - qt: Use Qt's native notification presenter, based on a system tray icon. Switching from or to this value requires a restart of qutebrowser. Recommended over `systray` on PyQt 5.14.
#   - libnotify: Shows messages via DBus in a libnotify-compatible way. If DBus isn't available, falls back to `systray` or `messages`, but shows an error message.
#   - systray: Use a notification presenter based on a systray icon. Falls back to `libnotify` or `messages` if not systray is available. This is a reimplementation of the `qt` setting value, but with the possibility to switch to it at runtime.
#   - messages: Show notifications as qutebrowser messages. Most notification features aren't available.
#   - herbe: (experimental!) Show notifications using herbe (github.com/dudik/herbe). Most notification features aren't available.
c.content.notifications.presenter = 'auto'


## Allow JavaScript to read from or write to the clipboard. With
## QtWebEngine, writing the clipboard as response to a user interaction
## is always allowed.
## Type: Bool
# c.content.javascript.can_access_clipboard = False
config.set('content.javascript.enabled', True, 'chrome-devtools://*')
config.set('content.javascript.enabled', True, 'devtools://*')
config.set('content.javascript.enabled', True, 'chrome://*/*')
config.set('content.javascript.enabled', True, 'qute://*/*')

## Allow pdf.js to view PDF files in the browser. Note that the files can
## still be downloaded by clicking the download button in the pdf.js
## viewer.
## Type: Bool
c.content.pdfjs = True


## Load images automatically in web pages.
## Type: Bool
# c.content.images = True
config.set('content.images', True, 'chrome-devtools://*')
config.set('content.images', True, 'devtools://*')
#
# Allow websites to show notifications.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.notifications.enabled', True, 'https://www.reddit.com')
config.set('content.notifications.enabled', True, 'https://www.youtube.com')
#
# Whether to show the origin URL for notifications. Note that URL
# patterns with this setting only get matched against the origin part of
# the URL, so e.g. paths in patterns will never match. Note that with
# the `qt` presenter, origins are never shown.
# Type: Bool
c.content.notifications.show_origin = True


## Allow websites to request persistent storage quota via
## `navigator.webkitPersistentStorage.requestQuota`.
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
c.content.persistent_storage = 'ask'


## Enable plugins in Web pages.
## Type: Bool
c.content.plugins = False


## Open new windows in private browsing mode which does not record
## visited pages.
## Type: Bool
c.content.private_browsing = True


## Proxy to use. In addition to the listed values, you can use a
## `socks://...` or `http://...` URL.
## Type: Proxy
## Valid values:
##   - system: Use the system wide proxy.
##   - none: Don't use any proxy
c.content.proxy = 'system'


## Send DNS requests over the configured proxy.
## Type: Bool
c.content.proxy_dns_requests = True


## Allow websites to register protocol handlers via
## `navigator.registerProtocolHandler`.
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
c.content.register_protocol_handler = 'ask'


## Enable WebGL.
## Type: Bool
c.content.webgl = True


## Limit fullscreen to the browser window (does not expand to fill the
## screen).
## Type: Bool
c.content.fullscreen.window = True


# Enable quirks (such as faked user agent headers) needed to get
# specific sites to work properly.
# Type: Bool
c.content.site_specific_quirks.enabled = True


# Disable a list of named quirks. The js-string-replaceall quirk is
# needed for Nextcloud Calendar < 2.2.0 with QtWebEngine < 5.15.3.
# However, the workaround is not fully compliant to the ECMAScript spec
# and might cause issues on other websites, so it's disabled by default.
# Type: FlagList
# Valid values:
#   - ua-whatsapp
#   - ua-google
#   - ua-slack
#   - ua-googledocs
#   - js-whatsapp-web
#   - js-discord
#   - js-string-replaceall
#   - js-globalthis
#   - js-object-fromentries
#   - misc-krunker
#   - misc-mathml-darkmode
c.content.site_specific_quirks.skip = ['js-string-replaceall']


# How to proceed on TLS certificate errors.
# Type: String
# Valid values:
#   - ask: Ask how to proceed for every certificate error (unless non-overridable due to HSTS).
#   - ask-block-thirdparty: Ask how to proceed for normal page loads, but silently block resource loads.
#   - block: Automatically block loading on certificate errors.
#   - load-insecurely: Force loading pages despite certificate errors. This is *insecure* and should be avoided. Instead of using this, consider fixing the underlying issue or importing a self-signed certificate via `certutil` (or Chromium) instead.
c.content.tls.certificate_errors = 'ask'


## Which interfaces to expose via WebRTC. On Qt 5.10, this option doesn't
## work because of a Qt bug.
## Type: String
## Valid values:
##   - all-interfaces: WebRTC has the right to enumerate all interfaces and bind them to discover public interfaces.
##   - default-public-and-private-interfaces: WebRTC should only use the default route used by http. This also exposes the associated default private address. Default route is the route chosen by the OS on a multi-homed endpoint.
##   - default-public-interface-only: WebRTC should only use the default route used by http. This doesn't expose any local addresses.
##   - disable-non-proxied-udp: WebRTC should only use TCP to contact peers or servers unless the proxy server supports UDP. This doesn't expose any local addresses either.
# c.content.webrtc_ip_handling_policy = 'all-interfaces'

## Monitor load requests for cross-site scripting attempts. Suspicious
## scripts will be blocked and reported in the inspector's JavaScript
## console.
## Type: Bool
c.content.xss_auditing = False


# How navigation requests to URLs with unknown schemes are handled.
# Type: String
# Valid values:
#   - disallow: Disallows all navigation requests to URLs with unknown schemes.
#   - allow-from-user-interaction: Allows navigation requests to URLs with unknown schemes that are issued from user-interaction (like a mouse-click), whereas other navigation requests (for example from JavaScript) are suppressed.
#   - allow-all: Allows all navigation requests to URLs with unknown schemes.
c.content.unknown_url_scheme_policy = 'allow-from-user-interaction'

## Maximum width (in pixels) of tabs (-1 for no maximum). This setting
## only applies when tabs are horizontal. This setting does not apply to
## pinned tabs, unless `tabs.pinned.shrink` is False. This setting may
## not apply properly if max_width is smaller than the minimum size of
## tab contents, or smaller than tabs.min_width.
## Type: Int
# c.tabs.max_width = -1
#
#

## Enable hyperlink auditing (`<a ping>`).
## Type: Bool
# c.content.hyperlink_auditing = False

## Draw the background color and images also when the page is printed.
## Type: Bool
# c.content.print_element_backgrounds = True

## A list of patterns that should always be loaded, despite being ad-
## blocked. Note this whitelists blocked hosts, not first-party URLs. As
## an example, if `example.org` loads an ad from `ads.example.org`, the
## whitelisted host should be `ads.example.org`. If you want to disable
## the adblocker on a given page, use the `content.host_blocking.enabled`
## setting with a URL pattern instead. Local domains are always exempt
## from hostblocking.
## Type: List of UrlPattern
# c.content.host_blocking.whitelist = ['piwik.org']


## Validate SSL handshakes.
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
# c.content.ssl_strict = 'ask'

