Set-PSDebug -Trace 0 3

$winXX = @(
    'C:\Users\15517\scoop\apps\logseq\current\Logseq.exe',
    'C:\Users\15517\scoop\apps\vscode\current\Code.exe'
    # C:\Users\15517\scoop\apps\yesplaymusic\current\YesPlayMusic.exe
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
    # default browser open url, via https://www.pstips.net/opening-webpages-from-powershell.html
    # start  'C:\Users\15517\scoop\apps\vivaldi\current\Application\vivaldi.exe ' $i
    # NOTE: please don't use string to construct command, like `+$i`
}

