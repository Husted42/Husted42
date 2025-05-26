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