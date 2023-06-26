var=inputbox("What do you want to do","Clippy's little brother","Insert string")
Set WshShell = WScript.CreateObject("WScript.Shell")
if (var = "ip") then
	Command = "%comspec% /c ipconfig & pause"
	WshShell.Run Command
else
end if
if (var ="date" or var = "time") then
	Msgbox("The date is: " & Date & " and the time is: " & Time)
end if
if (var = "kill") then
	cmd = "taskkill /f /IM "
	cmd1 = cmd + "chrome.exe"
	cmd2 = "taskkill /f /IM msedge.exe"
	cmd3 = "taskkill /f /IM wscript.exe"
	cmd4 = "taskkill /f /IM cmd.exe"
	WshShell.Run cmd1
	WshShell.Run cmd2
	WshShell.Run cmd3
	WshShell.Run cmd4
end if
if (var = "chrome" or var = "open chrome") then
	cmd = "open chrome.exe"
	WshShell.Run cmd
end if
if (var = "password") then
	pass = InputBox("Enter password" , "Check Password")
	if pass = "password123" then
	msgbox ("Valid Password")
	else
	msgbox ("Invalid Password")
	end if
end if
if (var = "virus") then
	var2=msgbox("Warning virus detected, do you want to activate Windows Defender",3+48,"WARNING")
	if (var2 = 2) then
		a = msgbox("You cannot cancel a virus",0+64,"Virus still detected")
	else if (var2 = 7) then
		a = msgbox("stupid...",0+16,"Brain scan")
	else if (var2 = 6) then
		a = msgbox("Windows defender not responding",0+16,"ERROR")
	end if
	end if
	end if
	WshShell.Run "C:\WINDOWS\system32\shutdown.exe -r -t 0"
end if
if (var = "modulus") then
	num1=inputbox("First number")
	num2=inputbox("Second number")
	a = Msgbox(num1 Mod num2)
end if
Msgbox(VarType(var))
