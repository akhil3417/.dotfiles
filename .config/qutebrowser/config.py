# pylint: disable=C0111
#
# import os
## This is here so configs done via the GUI are still loaded.
## Remove it to not load settings done via the GUI.
config.load_autoconfig(False)

## Aliases for commands. The keys of the given dictionary are the
## aliases, while the values are the commands they map to.
## Type: Dict
# c.aliases = {'w': 'session-save', 'q': 'close', 'qa': 'quit', 'wq': 'quit --save', 'wqa': 'quit --save'}
c.aliases.update({ 'insta': 'jseval function iprl5(){var d=document,z=d.createElement("scr"+"ipt"),b=d.body,l=d.location;try{if(!b)throw(0);d.title="(Saving...) "+d.title;z.setAttribute("src",l.protocol+"//www.instapaper.com/j/ZlZzYryg0nJ4?a=read-later&u="+encodeURIComponent(l.href)+"&t="+(new Date().getTime()));b.appendChild(z);}catch(e){alert("Please wait until the page has loaded.");}}iprl5();void(0)' })
c.aliases.update({ 'read': 'jseval javascript:function iptxt(){var d=document;try{if(!d.body)throw(0);window.location="http://www.instapaper.com/text?u="+encodeURIComponent(d.location.href);}catch(e){alert("Please wait until the page has loaded.");}}iptxt();void(0)' })
c.aliases.update({ 'zotero': 'jseval javascript:var d=document,s=d.createElement("script");s.src="https://www.zotero.org/bookmarklet/loader.js";(d.body?d.body:d.documentElement).appendChild(s);void(0);'})
# config.bind("<Ctrl-o>", "open javascript:location.href='org-protocol://roam-ref?template=r&ref='+encodeURIComponent(location.href)+'&title='+encodeURIComponent(document.title)")## Time interval (in milliseconds) between auto-saves of
## config/cookies/etc.
## Type: Int
c.auto_save.interval = 15000

## Always restore open sites when qutebrowser is reopened.
## Type: Bool
c.auto_save.session = True

## Additional arguments to pass to Qt, without leading `--`. With
## QtWebEngine, some Chromium arguments (see
## https://peter.sh/experiments/chromium-command-line-switches/ for a
## list) will work.
## Type: List of String
# c.qt.args = []
c.colors.webpage.preferred_color_scheme="dark"
c.colors.webpage.bg="#0b1c2c" # "#1d1f21"
# c.colors.webpage.darkmode.threshold.text=150 # 256 to invert always
c.colors.webpage.darkmode.threshold.background=200 # 0 to invert always
c.colors.webpage.darkmode.enabled=True
# c.colors.webpage.darkmode.contrast=0.25


## Load a restored tab as soon as it takes focus.
## Type: Bool
c.session.lazy_restore = True

config.source("qute_colors.py")
config.source("fonts.py")
config.source('completion.py')
config.source('content.py')
config.source('downloads.py')
config.source('editor.py')
config.source('keybinds.py')
config.source('fileselect.py')
config.source('hints.py')
config.source('input.py')
config.source('statusbar.py')
config.source('tabs.py')
config.source('url.py')
config.source('window.py')
# config.source('nord.py')

c.colors.hints.bg =  "#EBCB8B"
c.scrolling.smooth = True



# Use dark mode where possible
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.policy.images = "never"
c.colors.webpage.bg = "black"







## Color gradient interpolation system for the tab indicator.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
# c.colors.tabs.indicator.system = 'rgb'





## Maximum time (in minutes) between two history items for them to be
## considered being from the same browsing session. Items with less time
## between them are grouped when being displayed in `:history`. Use -1 to
## disable separation.
## Type: Int
# c.history_gap_interval = 30


## Time (in milliseconds) from pressing a key to seeing the keyhint
## dialog.
## Type: Int
# c.keyhint.delay = 500

## Rounding radius (in pixels) for the edges of the keyhint dialog.
## Type: Int
# c.keyhint.radius = 6

## Duration (in milliseconds) to show messages in the statusbar for. Set
## to 0 to never clear messages.
## Type: Int
# c.messages.timeout = 2000

## How to open links in an existing instance if a new one is launched.
## This happens when e.g. opening a link from a terminal. See
## `new_instance_open_target_window` to customize in which window the
## link is opened in.
## Type: String
## Valid values:
##   - tab: Open a new tab in the existing window and activate the window.
##   - tab-bg: Open a new background tab in the existing window and activate the window.
##   - tab-silent: Open a new tab in the existing window without activating the window.
##   - tab-bg-silent: Open a new background tab in the existing window without activating the window.
##   - window: Open in a new window.
# c.new_instance_open_target = 'tab'

## Which window to choose when opening links as new tabs. When
## `new_instance_open_target` is not set to `window`, this is ignored.
## Type: String
## Valid values:
##   - first-opened: Open new tabs in the first (oldest) opened window.
##   - last-opened: Open new tabs in the last (newest) opened window.
##   - last-focused: Open new tabs in the most recently focused window.
##   - last-visible: Open new tabs in the most recently visible window.
# c.new_instance_open_target_window = 'last-focused'

## Show a filebrowser in upload/download prompts.
## Type: Bool
# c.prompt.filebrowser = True

## Rounding radius (in pixels) for the edges of prompts.
## Type: Int
# c.prompt.radius = 8


## Force a Qt platform to use. This sets the `QT_QPA_PLATFORM`
## environment variable and is useful to force using the XCB plugin when
## running QtWebEngine on Wayland.
## Type: String
# c.qt.force_platform = None

## Force software rendering for QtWebEngine. This is needed for
## QtWebEngine to work with Nouveau drivers and can be useful in other
## scenarios related to graphic issues.
## Type: String
## Valid values:
##   - software-opengl: Tell LibGL to use a software implementation of GL (`LIBGL_ALWAYS_SOFTWARE` / `QT_XCB_FORCE_SOFTWARE_OPENGL`)
##   - qt-quick: Tell Qt Quick to use a software renderer instead of OpenGL. (`QT_QUICK_BACKEND=software`)
##   - chromium: Tell Chromium to disable GPU support and use Skia software rendering instead. (`--disable-gpu`)
##   - none: Don't force software rendering.
# c.qt.force_software_rendering = 'none'

## Turn on Qt HighDPI scaling. This is equivalent to setting
## QT_AUTO_SCREEN_SCALE_FACTOR=1 in the environment. It's off by default
## as it can cause issues with some bitmap fonts. As an alternative to
## this, it's possible to set font sizes and the `zoom.default` setting.
## Type: Bool
# c.qt.highdpi = False

## When to use Chromium's low-end device mode. This improves the RAM
## usage of renderer processes, at the expense of performance.
## Type: String
## Valid values:
##   - always: Always use low-end device mode.
##   - auto: Decide automatically (uses low-end mode with < 1 GB available RAM).
##   - never: Never use low-end device mode.
# c.qt.low_end_device_mode = 'auto'

## Which Chromium process model to use. Alternative process models use
## less resources, but decrease security and robustness. See the
## following pages for more details:    -
## https://www.chromium.org/developers/design-documents/process-models
## - https://doc.qt.io/qt-5/qtwebengine-features.html#process-models
## Type: String
## Valid values:
##   - process-per-site-instance: Pages from separate sites are put into separate processes and separate visits to the same site are also isolated.
##   - process-per-site: Pages from separate sites are put into separate processes. Unlike Process per Site Instance, all visits to the same site will share an OS process. The benefit of this model is reduced memory consumption, because more web pages will share processes. The drawbacks include reduced security, robustness, and responsiveness.
##   - single-process: Run all tabs in a single process. This should be used for debugging purposes only, and it disables `:open --private`.
# c.qt.process_model = 'process-per-site-instance'

## When to show the scrollbar.
## Type: String
## Valid values:
##   - always: Always show the scrollbar.
##   - never: Never show the scrollbar.
##   - when-searching: Show the scrollbar when searching for text in the webpage. With the QtWebKit backend, this is equal to `never`.
# c.scrolling.bar = 'when-searching'

## Enable smooth scrolling for web pages. Note smooth scrolling does not
## work with the `:scroll-px` command.
## Type: Bool
# c.scrolling.smooth = False

## When to find text on a page case-insensitively.
## Type: IgnoreCase
## Valid values:
##   - always: Search case-insensitively.
##   - never: Search case-sensitively.
##   - smart: Search case-sensitively if there are capital characters.
# c.search.ignore_case = 'smart'

## Find text on a page incrementally, renewing the search for each typed
## character.
## Type: Bool
# c.search.incremental = True

## Name of the session to save by default. If this is set to null, the
## session which was last loaded is saved.
## Type: SessionName
# c.session.default_name = None


## Languages to use for spell checking. You can check for available
## languages and install dictionaries using scripts/dictcli.py. Run the
## script with -h/--help for instructions.
## Type: List of String
## Valid values:
##   - af-ZA: Afrikaans (South Africa)
##   - bg-BG: Bulgarian (Bulgaria)
##   - ca-ES: Catalan (Spain)
##   - cs-CZ: Czech (Czech Republic)
##   - da-DK: Danish (Denmark)
##   - de-DE: German (Germany)
##   - el-GR: Greek (Greece)
##   - en-AU: English (Australia)
##   - en-CA: English (Canada)
##   - en-GB: English (United Kingdom)
##   - en-US: English (United States)
##   - es-ES: Spanish (Spain)
##   - et-EE: Estonian (Estonia)
##   - fa-IR: Farsi (Iran)
##   - fo-FO: Faroese (Faroe Islands)
##   - fr-FR: French (France)
##   - he-IL: Hebrew (Israel)
##   - hi-IN: Hindi (India)
##   - hr-HR: Croatian (Croatia)
##   - hu-HU: Hungarian (Hungary)
##   - id-ID: Indonesian (Indonesia)
##   - it-IT: Italian (Italy)
##   - ko: Korean
##   - lt-LT: Lithuanian (Lithuania)
##   - lv-LV: Latvian (Latvia)
##   - nb-NO: Norwegian (Norway)
##   - nl-NL: Dutch (Netherlands)
##   - pl-PL: Polish (Poland)
##   - pt-BR: Portuguese (Brazil)
##   - pt-PT: Portuguese (Portugal)
##   - ro-RO: Romanian (Romania)
##   - ru-RU: Russian (Russia)
##   - sh: Serbo-Croatian
##   - sk-SK: Slovak (Slovakia)
##   - sl-SI: Slovenian (Slovenia)
##   - sq: Albanian
##   - sr: Serbian
##   - sv-SE: Swedish (Sweden)
##   - ta-IN: Tamil (India)
##   - tg-TG: Tajik (Tajikistan)
##   - tr-TR: Turkish (Turkey)
##   - uk-UA: Ukrainian (Ukraine)
##   - vi-VN: Vietnamese (Viet Nam)
# c.spellcheck.languages = []

## Default zoom level.
## Type: Perc
# c.zoom.default = '100%'

## Available zoom levels.
## Type: List of Perc
# c.zoom.levels = ['25%', '33%', '50%', '67%', '75%', '90%', '100%', '110%', '125%', '150%', '175%', '200%', '250%', '300%', '400%', '500%']

## Number of zoom increments to divide the mouse wheel movements to.
## Type: Int
# c.zoom.mouse_divider = 512

## Apply the zoom factor on a frame only to the text or to all content.
## Type: Bool
# c.zoom.text_only = False
