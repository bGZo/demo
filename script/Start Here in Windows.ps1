Set-PSDebug -Trace 0
start explorer.exe

$winxx = @(
'C:\Users\15517\scoop\apps\vivaldi\current\Application\vivaldi.exe', 
'C:\Users\15517\scoop\apps\logseq\current\Logseq.exe',
'C:\Users\15517\scoop\apps\vscode\current\Code.exe'
)

$uwp=@(
'iTunes',
'Windows Terminal Preview'
)

foreach($i in $winxx){
	start $i
}

foreach($i in $uwp){
    start "shell:AppsFolder\$(Get-StartApps $i | select -ExpandProperty AppId | sort -Unique)"
    # via https://stackoverflow.com/questions/46893260/how-to-start-a-universal-windows-app-uwp-from-powershell-in-windows-10
}