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

# With bluez-tools
`sudo apt-get install bluez-tools`

`bt-device -l`
 