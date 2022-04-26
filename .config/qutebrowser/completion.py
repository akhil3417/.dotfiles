# pylint: disable=C0111
from qutebrowser.config.configfiles import ConfigAPI  # noqa: F401
from qutebrowser.config.config import ConfigContainer  # noqa: F401
config: ConfigAPI = config  # noqa: F821 pylint: disable=E0602,C0103
c: ConfigContainer = c  # noqa: F821 pylint: disable=E0602,C0103
## Number of commands to save in the command history. 0: no history / -1:
## unlimited
## Type: Int
# c.completion.cmd_history_max_items = 100

## Delay (in milliseconds) before updating completions after typing a
## character.
## Type: Int
c.completion.delay = 150

## Height (in pixels or as percentage of the window) of the completion.
## Type: PercOrInt
c.completion.height = '50%'

## Minimum amount of characters needed to update completions.
## Type: Int
c.completion.min_chars = 2

## Which categories to show (in which order) in the :open completion.
## Type: FlagList
## Valid values:
##   - searchengines
##   - quickmarks
##   - bookmarks
##   - history
# c.completion.open_categories = ['searchengines', 'quickmarks', 'bookmarks', 'history']
#
c.completion.open_categories = [
    'searchengines',
    'quickmarks',
    'bookmarks',
    'history',
    'filesystem'
]

## Move on to the next part when there's only one possible completion
## left.
## Type: Bool
c.completion.quick = True

## Padding (in pixels) of the scrollbar handle in the completion window.
## Type: Int
c.completion.scrollbar.padding = 1 #defval 2

## Width (in pixels) of the scrollbar in the completion window.
## Type: Int
c.completion.scrollbar.width = 5 #defval 12
#
# Default filesystem autocomplete suggestions for :open. The elements of
# this list show up in the completion window under the Filesystem
# category when the command line contains `:open` but no argument.
# Type: List of String
c.completion.favorite_paths = []

## When to show the autocompletion window.
## Type: String
## Valid values:
##   - always: Whenever a completion is available.
##   - auto: Whenever a completion is requested.
##   - never: Never.
c.completion.show = 'always'

## Shrink the completion to be smaller than the configured size if there
## are no scrollbars.
## Type: Bool
c.completion.shrink = True #def false

## Format of timestamps (e.g. for the history completion). See
## https://sqlite.org/lang_datefunc.html for allowed substitutions.
## Type: String
# c.completion.timestamp_format = '%Y-%m-%d'
c.completion.timestamp_format = '%Y-%m-%d %H:%M'

## Execute the best-matching command on a partial match.
## Type: Bool
# c.completion.use_best_match = False
c.completion.use_best_match = True

## A list of patterns which should not be shown in the history. This only
## affects the completion. Matching URLs are still saved in the history
## (and visible on the qute://history page), but hidden in the
## completion. Changing this setting will cause the completion history to
## be regenerated on the next start, which will take a short while.
## Type: List of UrlPattern
c.completion.web_history.exclude = []

## Number of URLs to show in the web history. 0: no history / -1:
## unlimited
## Type: Int
# c.completion.web_history.max_items = -1

## Font used in the completion categories.
## Type: Font
c.fonts.completion.category = 'bold 11pt monospace'

## Font used in the completion widget.
## Type: Font
c.fonts.completion.entry = '11pt monospace'
# c.fonts.completion.entry = '11pt "Source Code Pro"'
