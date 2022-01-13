from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal


def get_mod_key():
    return "mod4"

def get_terminal():
    return guess_terminal()

def init_key_bindings():
    mod = get_mod_key()
    terminal = get_terminal()
    
    keys = [
        # Switch between windows
        Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
        Key(["mod1"], "Tab", lazy.layout.next(), desc="Move window focus to other window"),

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

        # Toggle between different layouts as defined below
        Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
        
        Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
        Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
        Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

        # Spawn user applications
        Key(
            [mod], 
            "r", 
            lazy.spawn("rofi -show combi"), 
            desc="Launch rofi"
        ),
        Key(
            [mod], 
            "x", 
            lazy.spawn('terminator -p Darkside'), 
            desc="Launch terminal"
        ),
        Key(
            [mod], 
            "b", 
            lazy.spawn("/opt/brave.com/brave/brave-browser"), 
            desc="Launch Brave Browser"
        ),
        Key(
            [mod], 
            "f", 
            lazy.spawn("firefox"), 
            desc="Launch Firefox"
        ),
        Key(
            [mod], 
            "c",
            lazy.spawn("vscodium"), 
            desc="Launch VSCodium"
        ),
        Key(
            [mod], 
            "s", 
            lazy.spawn("scrcpy --turn-screen-off"), 
            desc="Launch Scrcpy"
        ),
        Key(
            [mod], 
            "i", 
            lazy.spawn("/opt/Citrix/ICAClient/selfservice"), 
            desc="Launch Citrix Selfservice"
        ),
        Key(
            [mod], 
            "p", 
            lazy.spawn("keepassxc"), 
            desc="Launch Keepassxc"
        ),    
        Key(
            [mod], 
            "e", 
            lazy.spawn("terminator -e vifm"), 
            desc="Launch vifm"
        ),    
        Key(
            [mod], 
            "m", 
            lazy.spawn("signal-desktop --%u"), 
            desc="Launch Signal Private Messenger"
        ),    
        Key(
            [mod, "shift"], 
            "m", 
            lazy.group["5"].toscreen(), 
            lazy.spawn('/opt/brave.com/brave/brave-browser --profile-directory=Default --app-id=kfmbdbdmeghpmahfeemlipiboapibogp'), 
            desc="Launch Jitsi Meet in Brave"
        ),    
        Key(
            [mod, "shift"], 
            "s", 
            lazy.spawn("/home/k/Programs/anaconda3/bin/spyder"), 
            desc="Launch Spyder"
        ),
        Key(
            [mod, "shift"], 
            "d", 
            lazy.spawn("/home/k/Programs/anaconda3/bin/designer"), 
            desc="Launch Qt Designer"
        ),
        
        # OFFICE APPLICATIONS
        Key(
            [mod], 
            "t", 
            lazy.spawn('/opt/brave.com/brave/brave-browser --profile-directory=Default --app-id=fapmifdifgkcdpplobdkgikmoocopiic'), 
            desc="Launch Microsoft Teams in Brave"
        ),    
        Key(
            [mod], 
            "o", 
            lazy.spawn('/opt/brave.com/brave/brave-browser --profile-directory=Default --app-id=lkkahpbimdkjdjjiijflmhaeameegbcm'), 
            desc="Launch outlook in Brave"
        ),    
        Key(
            [mod, "shift"], 
            "t", 
            lazy.spawn('/opt/brave.com/brave/brave-browser "--profile-directory=Profile 1" --app-id=hlbcffjbcggpimahbjeaenckgipcchde'), 
            desc="Launch Microsoft Teams in Brave"
        ),    
        Key(
            [mod, "shift"], 
            "o", 
            lazy.spawn('/opt/brave.com/brave/brave-browser "--profile-directory=Profile 1" --app-id=lkkahpbimdkjdjjiijflmhaeameegbcm'), 
            desc="Launch outlook in Brave"
        ), 
          
        # SYSTEM COMMANDS
        Key(
            [mod, "control"], 
            "s", 
            lazy.spawn("shutdown -P"), 
            desc="Shutdown the system"
        ),
    ]

    return keys
