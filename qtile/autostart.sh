#!/bin/bash

$HOME/.screenlayout/2k.sh &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & 
eval $(gnome-keyring-daemon -s --components=pkcs11,secrets,ssh,gpg) &
nm-applet --indicator & 
# variety &
feh --bg-fill --randomize $HOME/.config/variety/Downloaded/Bing/* &
pnmixer &
# nextcloud  --background &
xfce4-power-manager &
ibus-daemon -drxR &
picom &