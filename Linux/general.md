# Audio
For audio control install pavucontrol

# File manegement
Create a file
```
touch <filename>
```

Remove a file or dictonary
```
rm -f <filename>
rm -r <directoryname>
```

Move a file
```
mv <src> <dest>
```

File manager
 - Just open nautilus

# Package mangement
Install package
```
sudo dpkg -i <file.deb>
```

Solve missing dependencies
```
sudo apt-get install -f
```

# Bluetooth
### i3 Config
First we need to make sure that the poper D-Bus session is started by added the followint to i3-config
`exec --no-startup-id eval "$(dbus-launch --sh-syntax)"`

### Connect
*Check if controller is installed*
`bluetoothctl list`

*Turn on bluetooh*
`bluetoothctl power on`
If this failed with Failed to set power on: org.bluez.Error.Failed it can be restarted with

```
rfkill block bluetooth
rfkill unblock bluetooth

systemctl stop bluetooth.service
systemctl start bluetooth.service
```

*Scan for devices*
`bluetoothctl scan on` 

### blueman
Okay.. It can be found this way but an easier fix was just to install blueman-applet
`sudo apt install bluemann`

And then add it the following to i3 config
exec --no-startup-id blueman-applet

# Wifi setup 
### Show list of wifi
```
nmcli dev wifi
```

### Turn on wifi
Check if turned on
```
nmcli radio wifi
```

Turn on 
```
nmcli radio wifi on
```

### Connecto to wifi
```
nmcli device wifi connect APname password password
```

### Turn on wifi
```
sudo rfkill unblock wifi
nmcli networking on
```

### Show current wifi
```
nmcli connection show
```





