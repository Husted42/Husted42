# i3 Config
First we need to make sure that the poper D-Bus session is started by added the followint to i3-config
`exec --no-startup-id eval "$(dbus-launch --sh-syntax)"`

# Connect

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


Okay.. It can be found this way but an easier fix was just to install blueman-applet
`sudo apt install bluemann`

And then add it the following to i3 config
exec --no-startup-id blueman-applet

