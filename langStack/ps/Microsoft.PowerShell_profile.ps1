#--------------------------------+
#                  __ _ _        |
#  _ __  _ __ ___  / _(_) | ___  |
# | '_ \| '__/ _ \| |_| | |/ _ \ |
# | |_) | | | (_) |  _| | |  __/ |
# | .__/|_|  \___/|_| |_|_|\___| |
# |_|                            |
#--------------------------------|
# more via https://docs.microsoft.com/zh-cn/powershell/module/microsoft.powershell.core/about/about_profiles
# https://www.cnblogs.com/dreamer-fish/p/3738513.html
# FIXME: how to run  $profile...

# +------+
# |Import|
# +------+
Import-Module posh-git
Import-Module oh-my-posh
Import-Module PSReadLine

# +------+
# |Config|
# +------+

# support Oh My Posh
Set-PoshPrompt powerline

# enable history auto predict
Set-PSReadLineOption -PredictionSource History

