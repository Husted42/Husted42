# i3status
### Error : buffer overflow detected
```
i3status: trying to auto-detect output_format setting
i3status: auto-detected "term"
*** buffer overflow detected ***: terminated
Aborted (core dumped)
```

This error comes from connecting to an wifi that has a name longer than 30 charectors long. I fixed this by changing the name of my network.

