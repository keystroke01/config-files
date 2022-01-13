from libqtile.config import Group, Match

def init_group_names():
    return [
        ("1", {'layout': 'columns', 'matches': [Match(wm_class=["codium"])]}),
        ("2", {'layout': 'columns'}),
        ("3", {'layout': 'columns'}),
        ("4", {'layout': 'columns', 'matches': [Match(wm_class=["lxappearance"])]}),
        ("5", {'layout': 'columns', 'matches':[Match(wm_class=['signal'])]}),
        ("6", {'layout': 'columns', 'matches':[Match(wm_class=['keepassxc'])] }),
        ("7", {'layout': 'columns'}),
     
    ]

def init_groups():
    return [Group(name, **kwargs) for name, kwargs in init_group_names()]
