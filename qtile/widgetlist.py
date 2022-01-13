from libqtile import widget, bar
from libqtile.lazy import lazy
from libqtile import qtile

def get_colors():
    colors = {
        "greish-black-1"    : "#282c34",
        "greish-black-2"    : "#434758",
        "white"             : "#ffffff",
        "light-red"         : "#ff5555",
        "darkish-blue"      : "#215578",
        "purple"            : "#74438f",
        "purplish-pink"     : "#e1acff",
        "green"             : "#00a600",
        "red"               : "#ff0000",
        "grey"              : "#212121",
        "light-grey"        : "#505050",
        "black"             : "#000000",
        "fern"             : "#66bb6a"  
    }
    return colors

def get_default_widget_list(visible_groups_list):
    colors = get_colors()
    widget_list = [
        widget.GroupBox(
            highlight_method = "line",
            #highlight_color = ['000000', '215578'],
            highlight_color = colors['greish-black-2'],
            #this_current_screen_border = colors['blue'],
            active = colors['white'],
            inactive = colors['white'],
            font = 'Inconsolata Regular',
            #padding_x = 5,
            padding_y = 15,
            #margin_y = 7,
            disable_drag = True,
            #background = colors["greish-black-1"],
            center_aliged = True,
            borderwidth = 6,
            fontsize = 14,
            visible_groups = visible_groups_list,
        # hide_unused = True 
        ),
        widget.TaskList(
            #background = colors["greish-black-1"],
            max_title_width = 0,
            highlight_method = "block",
            #border = "66bb6a",
            font = "Inconsolata Regular",
            fontsize = 12,
            icon_size = 16,
            #padding_x = 10,
            padding_y = 5,
            #borderwidth = 5,
            #border = '282c34',
            title_width_method = 'uniform',
            unfocused_border = '505050'
        ), 
        widget.Systray(
            background = colors ["greish-black-1"],
            opacity = 0.5,
        ),
        widget.Clock(
            #format='%H:%M\n%a %d-%b-%Y',
            format='%a %d-%b %H:%M',
            foreground = colors ["white"],
            background = colors ["greish-black-1"],
            font = 'Inconsolata Regular',
            fontsize = 15,
            padding = 15,
            mouse_callbacks = {"Button1": lazy.spawn("yad --calendar")},

        ),
        widget.CurrentLayoutIcon(
            #background = colors["greish-black-1"],
            #background = colors ["grey"],
            foreground = colors["darkish-blue"],
            padding = 5,
            font = 'Inconsolata Regular',
            scale = 0.5
        ),
        
    ]
    
    return widget_list
    

def init_screen1_widgets():
    screen1_widgets = get_default_widget_list(visible_groups_list=['5','6','7'])
    screen1_widgets.pop(2) # Pop out the systray widget
    return screen1_widgets

def init_screen2_widgets():
    screen2_widgets = get_default_widget_list(visible_groups_list=['1','2','3','4'])
    return screen2_widgets