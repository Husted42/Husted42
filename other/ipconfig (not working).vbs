var=inputbox("Who do you want to ping?","Ping master 2000","Insert string")
Set WshShell = WScript.CreateObject("WScript.Shell")
Command = "%comspec% /c ipconfig & pause"
WshShell.Run Command
