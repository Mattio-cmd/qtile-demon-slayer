#####################################
#        DEMON SLAYER QTILE         # 
#####################################
from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder

import re
import socket
import subprocess
import os
import psutil
from libqtile.widget import KeyboardLayout, BatteryIcon, Memory

#####################################
#   My custom keybinds variable     # 
#####################################
mod = "mod4"
terminal = "kitty"
brave = "brave" 
firefox = "firefox"
dmenu = "dmenu_run -i -fn 'Ubuntu Bold-13' -p 'Run' -sb '#689d6a' -sf '#1d2021'"
libreoffice = "libreoffice"
pcmanfm = "pcmanfm"
cmus = "kitty -e 'cmus'"
obs = "obs"
vbx = "virtualbox"
discord = "discord"
shutdown = "shutdown now"
screenshot = "screenshot.sh"
reboot = "reboot"
es_keyboard = "setxkbmap es"
xplr = "kitty -e 'xplr'"
htop = "kitty -e 'htop'"

#####################################
#          Keybinds                 # 
#####################################
keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "q", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    #Media keys:
    # Sound with amixer
   ###########################(Dont uncoment, idk how this works)  Key([], "XF86AudioMute", lazy.spawn("amixer sset Master toggle")),
     Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset Master 5%-")),
     Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master 5%+")),
    # Screen brightness controls with xbacklight idk why tf not working
      Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 10")),
      Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 10")),
   
    # Brightness keys doesnt work either
      Key ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
      Key ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Goes to next keyboard layout"),
    #Custom keys
#####################################
#          Custom keybinds          # 
#####################################
    Key([mod], "p", lazy.spawn(firefox), desc="Opens firefox"),
    Key([mod], "r", lazy.spawn(dmenu), desc="Opens dmenu"),
    Key([mod], "t", lazy.spawn(pcmanfm), desc="Opens pcmanfm"),
    Key([mod], "o", lazy.spawn(obs), desc="Opens obs"),
    Key([mod], "v", lazy.spawn(vbx), desc="Opens vbx"),
    Key([mod], "d", lazy.spawn(discord), desc="Opens discord"),
    Key([mod], "i", lazy.spawn(libreoffice), desc="Opens libreoffice"),
    Key([mod], "e", lazy.spawn(es_keyboard), desc="Changes the keyboard for spanish"),
    Key([mod], "c", lazy.spawn(cmus), desc="Opens cmus"),
    Key([mod], "s", lazy.spawn(screenshot), desc="Takes a screenshot"),
    Key([mod, "shift"], "t", lazy.spawn(xplr), desc="Opens xplr"),
    Key([mod, "shift"], "r", lazy.spawn(reboot), desc="Reboots the computer"),
    Key([mod, "shift"], "s", lazy.spawn(shutdown), desc="Shutdowns the computer"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc='toggle floating'),
]

#####################################
#          Groups                   # 
#####################################
group_names = [
               ("一", {'layout': 'monadtall'},),
               ("二", {'layout': 'monadtall'}),
               ("三", {'layout': 'monadtall'}),
               ("四", {'layout': 'monadtall'}),
               ("五", {'layout': 'monadtall'}),
               ("六", {'layout': 'monadtall'}),
               ("七", {'layout': 'monadtall'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

#####################################
#          Layouts                  # 
#####################################
layout_theme = {"border_width": 2,
                "margin": 3,
                "border_width": 2,
                "border_focus": "b0e3e5",
                "border_normal": "#b0e3e5"
                }


layouts = [
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

#####################################
#          Widgets                  # 
#####################################
widget_defaults = dict(
    font='Ubuntu Bold',
    fontsize=12,
    padding=2,
)
extension_defaults = widget_defaults.copy()
screens = [
    Screen(
        top=bar.Bar(
            [
   #             widget.CurrentLayout(),
                 widget.Image(
                    filename = "~/qtile-demon-slayer/qtile/icon/icon.png",
                    scale = "True",
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal)}
                    ),
                widget.GroupBox(
                    font="mononoki",
                    highlight_color="#689d6a",
                  #  highlight_metod="block",
                    inactive="#c64486",
                    active="#c64486",
                    disable_drag = True, 
                    block_highlight_text_color="#689d6a",
                    foreground="1d2021",
                    background="#b0e3e5",
                    padding=10,
                    border_width=0,
                    spacing=0
                    ),
               # widget.Prompt(),
                widget.WindowName(
                    background="#b0e3e5",
                    foreground="#1d2021",
                    paddind=10
                    ),
  #              widget.TextBox(
   #                  text='[',
    #                 background = "#1d2021",
     #                foreground = "#fbf1c7",
      #               padding = 5,
       #              fontsize = 20
        #             ),
#                widget.CheckUpdates(
 #                   update_interval = 604800,
  #                  distro = "Arch_checkupdates",
   #                 display_format = "{updates} Updates",
   #                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syu')},
   #                 background = "#1d2021",
    #                foreground = "#fbf1c7"
   #                 ),
     #           widget.TextBox(
      #               text=']',
       #              background = "#1d2021",
        #             foreground = "#fbf1c7",
         #            padding = 5,
         #            fontsize = 20
         #            ),
                widget.Chord(
                    chords_colors={
                        'launch': ("#2E3440", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                #ZZZZ   Hi r/unixporn :)
                widget.TextBox(
                     text='[',
                     background = "#b0e3e5",
                     foreground = "#1d2021",
                     padding = 5,
                     fontsize = 20
                     ),
                widget.Systray(
                     background="#b0e3e5",
                     foreground="#1d2021",
                     padding=5
                     ),
                widget.TextBox(
                     text=']',
                     background = "#b0e3e5",
                     foreground = "#1d2021",
                     padding = 5,
                     fontsize = 20
                     ),
                widget.TextBox(
                     text='[',
                     background = "#b0e3e5",
                     foreground = "#1d2021",
                     padding = 5,
                     fontsize = 20
                     ),
     #           widget.TextBox(
    #                text = " 🖬",
   #                 foreground = "#fbf1c7",
  #                  background = "#1d2021",
 #                   padding = 0,
#                    fontsize = 14
#                    ),
                widget.Memory(
                    background="#b0e3e5",
                    foreground="#1d2021",
                    fontsize=13,
                    measure_mem="M",
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                    padding=0
                    ),
                widget.TextBox(
                     text=']',
                     background = "#b0e3e5",
                     foreground = "#1d2021",
                     padding = 5,
                     fontsize = 20
                     ),
                widget.TextBox(
                     text='[',
                     background = "#b0e3e5",
                     foreground = "#1d2021",
                     padding = 5,
                     fontsize = 20
                     ),
                widget.CPU(
                    foreground = "#1d2021",
                    background = "#b0e3e5",
                    padding=0
                     ),
                widget.TextBox(
                     text=']',
                     background = "#b0e3e5",
                     foreground = "#1d2021",
                     padding = 5,
                     fontsize = 20
                     ),
                widget.TextBox(
                     text='[',
                     background = "#b0e3e5",
                     foreground = "#1d2021",
                     padding = 5,
                     fontsize = 20
                     ),
                widget.KeyboardLayout(
                    background="#b0e3e5",
                    foreground="#1d2021",
                    configured_keyboards=['us', 'es'],
                    padding=0
                    ),
                widget.TextBox(
                     text=']',
                     background = "#b0e3e5",
                     foreground = "#1d2021",
                     padding = 5,
                     fontsize = 20
                     ),
                widget.TextBox(
                     text='[',
                     background = "#b0e3e5",
                     foreground = "#1d2021",
                     padding = 5,
                     fontsize = 20
                     ),
                widget.Volume(
                        background="#b0e3e5",
                        foreground="#1d2021",
                        padding=0
                        ),
                widget.TextBox(
                     text=']',
                     background = "#b0e3e5",
                     foreground = "#1d2021",
                     padding = 5,
                     fontsize = 20
                     ),
                widget.TextBox(
                     text='[',
                     background = "#b0e3e5",
                     foreground = "#1d2021",
                     padding = 5,
                     fontsize = 20
                     ),
                widget.Clock(
                     format='%I:%M %d/%m/%Y',   
                 #   format='%Y-%m-%d %a %I:%M %p',
                    background="#b0e3e5",
                    foreground="#1d2021",
                    padding=0
                    ),
                widget.TextBox(
                     text=']',
                     background = "#b0e3e5",
                     foreground = "#1d2021",
                     padding = 5,
                     fontsize = 20
                     ),
                widget.TextBox(
                     text='[',
                     background = "#b0e3e5",
                     foreground = "#1d2021",
                     padding = 5,
                     fontsize = 20
                     ),
                widget.Battery(energy_now_file = "charge_now",
                    energy_full_file = "charge_full",
                     power_now_file = "current_now",
                     update_delay = 5,
                     foreground = "1d2021",
                     background = "#b0e3e5",
                     charge_char = u'↑',
                     discharge_char = u'↓'
                     ),
                widget.TextBox(
                     text=']',
                     background = "#b0e3e5",
                     foreground = "#1d2021",
                     padding = 5,
                     fontsize = 20
                     ),
               #  widget.CPUGraph(
                #     border_color="#fbf1c7",
                 #    graph_color="#689d6a",
                  #   border_width=1,
                   #  line_width=1,
                    # type="line",
                     #width=50
                    # ),
               # widget.QuickExit(
                       # background="#e1acff",
                      #  padding=20
                     #   ),
            ],
            26,
            background="#b0e3e5",
            opacity=1,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

#####################################
#           Custom array            # 
#####################################
cmd = [
#        "feh --bg-fill .config/qtile/snowforest.png",
        "nm-applet &",
        "nitrogen --restore &",
        "picom &"
]
for x in cmd:
    os.system(x)
