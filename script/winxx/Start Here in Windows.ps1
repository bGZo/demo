Set-PSDebug -Trace 0

$winXX = @(
    'C:\Users\15517\scoop\apps\logseq\current\Logseq.exe',
    'C:\Users\15517\scoop\apps\vscode\current\Code.exe'
)

$uwp = @(
    'iTunes',
    'Microsoft To do',
    'Windows Terminal Preview'
)

$webPrepare =@(
    '"https://leetcode-cn.com/problemset/all/"',
    '"https://oi-wiki.org"'
)


foreach($i in $winXX){
    start $i
}

foreach($i in $uwp){
    start "shell:AppsFolder\$(Get-StartApps $i | select -ExpandProperty AppId | sort -Unique)"
    # via https://stackoverflow.com/questions/46893260/how-to-start-a-universal-windows-app-uwp-from-powershell-in-windows-10
}

foreach($i in $webPrepare){
    start -FilePath  $i
    #start  'C:\Users\15517\scoop\apps\vivaldi\current\Application\vivaldi.exe ' $i # same function
}