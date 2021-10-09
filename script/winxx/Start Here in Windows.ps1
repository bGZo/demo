Set-PSDebug -Trace 0

# +----+
# |Data|
# +----+

$data=@(
    @{name='logseq';isUWP='n';priority=1;isPath='y';path='C:\Users\15517\scoop\apps\logseq\current\Logseq.exe'},
    @{name='vscode';isUWP='n';priority=1;isPath='y';path='C:\Users\15517\scoop\apps\vscode\current\Code.exe'},

    @{name='iTunes';isUWP='y';priority=0;isPath='n'},
    @{name='Microsoft To do';isUWP='y';priority=0;isPath='n'},
    @{name='Windows Terminal Preview';isUWP='y';priority=0;isPath='n'}
)

$webData =@(
    '"https://leetcode-cn.com/problemset/all/"',
    '"https://oi-wiki.org"'
)


# +--------+
# |Function|
# +--------+

function openUwp {
    Param($name)
    start "shell:AppsFolder\$(Get-StartApps $name | select -ExpandProperty AppId | sort -Unique)"
    # via https://stackoverflow.com/questions/46893260/how-to-start-a-universal-windows-app-uwp-from-powershell-in-windows-10
}
function openNonUwp {
    Param($path)
    start $path
}

# +----+
# |Main|
# +----+

# sort data
$tempData=$data | sort-object -Property priority

#open software
foreach($i in $tempData){
    if($i.isUWP -eq 'y'){
        openUwp($i.name)
    }else{
        openNonUwp($i.path)
    }
}

# open web site
foreach($i in $webData){
    ## start -FilePath  $i
    start  'C:\Users\15517\scoop\apps\vivaldi\current\Application\vivaldi.exe ' $i # same function
}
