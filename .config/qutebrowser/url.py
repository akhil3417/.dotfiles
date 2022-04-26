# pylint: disable=C0111
from qutebrowser.config.configfiles import ConfigAPI  # noqa: F401
from qutebrowser.config.config import ConfigContainer  # noqa: F401
config: ConfigAPI = config  # noqa: F821 pylint: disable=E0602,C0103
c: ConfigContainer = c  # noqa: F821 pylint: disable=E0602,C0103


## What search to start when something else than a URL is entered.
## Type: String
## Valid values:
##   - naive: Use simple/naive check.
##   - dns: Use DNS requests (might be slow!).
##   - never: Never search automatically.
c.url.auto_search = 'naive'

## Page to open if :open -t/-b/-w is used without URL. Use `about:blank`
## for a blank page.
## Type: FuzzyUrl
# c.url.default_page = 'https://start.duckduckgo.com/'

## URL segments where `:navigate increment/decrement` will search for a
## number.
## Type: FlagList
## Valid values:
##   - host
##   - port
##   - path
##   - query
##   - anchor
c.url.incdec_segments = ['path', 'query']

## Open base URL of the searchengine if a searchengine shortcut is
## invoked without parameters.
## Type: Bool
c.url.open_base_url = False

## Search engines which can be used via the address bar. Maps a search
## engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}`
## placeholder. The placeholder will be replaced by the search term, use
## `{{` and `}}` for literal `{`/`}` signs. The search engine named
## `DEFAULT` is used when `url.auto_search` is turned on and something
## else than a URL was entered to be opened. Other search engines can be
## used by prepending the search engine name to the search term, e.g.
## `:open google qutebrowser`.
## Type: Dict
c.url.searchengines = {'s': 'http://searx.thegpm.org/?preferences=eJxtVU2P4zYM_TX1xUjRdg89-VC0KLrAArPYZHsVaIm2uZZEryQn4_76UrGdyDN7SAJR_Hh8emQCxtmmqNgrjzeVoG0uYcbKMKmAke0VQxM1nYa5_TndKgu-n6HHBv3p67myrMHmQ2UoQmvRqMnOPfnY_EvuZGlENXAacYk__fbnR9-Rp4Qq6sDWiuVlQq_-0BpjVH-9fJSStyAOFTmpoabAr0vzN9iIFcyJNbvJYsKmZ-4tVhE6jAhBD80vVRrQYcNRQ6jQH7Gc0XZKqnNwkIh93EuHe_vKkh8fHLSBbxFD5iL7_XO5fD7vwOR8CaBHuf765ZNYHQtBYj3fYeQUGhL2HBYV0aJOT2LQCxaMTRcQ68hdukHA2lAQr-yvKEmiK0NSKrImsLVDQyBG8qDUlQxyRjT7OFmIg0RkmrJpJaQW81LDNEWlOrL3G0N9m57HybQo6TWh17mbnnpBB1FcevQYIL-KpTZAWOpsiRTLq84EJvPM5xeAAoeZ9Zg_PZdBJTo3R9JK3X_kagFv8LV0DmgMHeD0iGMih3GjaK25Z3AkYsp01qDBoMvZi_7W0it3BYcHSHwlLC9_fT20ZEQoBRzQfeS58PCT25DtVzs7KFLKbL2jYo0tcnQQWDgT_eXTAPIA-WvPK9qiq4TFHwHZmWgptcI9pi1qgYEP79AF0TmBLuomHhdOHAcewT9TbXCeoZgWx17mBA8IprF2FALvQLsADrJ8cDO4xcmMiJZSAB-tzMaBDsff5HFLC8tYBpy4kPDGWebmwdBTaO-5_H4DfxDQKpg3E7G3-oaB3Svifx5cmUU2iw91TGHWaQ654lNm6xbSbLDOX1vzMUFIU95kRRpj-trgfRHmTVRejaRHkE24YntssX1xaK1P6Vro9OG_g37Ty8NxV8rDsA_Zmz2zMn1Au5L1LnB7hgeCh8PK9XOUPnz4_bWcO0oW2o2fPdn6cpXDNLBpPr-cL9W2RWUumw1MdV_tp5gW-cOx3FMm-vo_dAyKlA==&q={}',
                       'DEFAULT': 'https://duckduckgo.com/?q={}',
                       'r': 'https://old.reddit.com/r/{}',
                       'gs': 'https://scholar.google.com/scholar?q={}',
                       'n': 'https://nitter.net/{}',
                       'aw': 'https://wiki.archlinux.org/index.php?search={}',
                       'b': 'https://search.brave.com/search?q={}',
                       'hn': 'https://hn.algolia.com/?dateRange=all&prefix=false&query={}&sort=byDate',}

## Page(s) to open at the start.
## Type: List of FuzzyUrl, or FuzzyUrl
# c.url.start_pages = ['https://start.duckduckgo.com']

## URL parameters to strip with `:yank url`.
## Type: List of String
# c.url.yank_ignored_parameters = ['ref', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content']
# URL parameters to strip with `:yank url`.
# Type: List of String
c.url.yank_ignored_parameters = [
    'ref',
    'utm_source',
    'utm_medium',
    'utm_campaign',
    'utm_term',
    'utm_content'
]
