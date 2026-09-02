#!/usr/bin/bash
echo "Pick an option:"
echo "   1 - Extend using usb-c (work)"
echo "   2 - Duplicate HDMI (School presentation)"
read conf

if [ "$conf" -eq 1 ]; then
    echo "You picked 1"
    xrandr \
    	--dpi 282 \
	--fb 2560x1440 \
	--output eDP --primary --mode 3200x200 --pos 0x0 \
	--output DP-1-1 --mode 2560x1440 --right-of eDP-1 

elif [ "$conf" -eq 2 ]; then
    echo "You picked 2"
else
    echo "Error"
fi

eDP-1 connected primary 3200x2000
