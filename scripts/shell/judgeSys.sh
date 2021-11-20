# Quote the system bin
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin

# Judge System Release
cat /etc/issue | grep -q -E -i "ubuntu" # debain / centos 
cat /proc/version | grep -q -E -i "ubuntu" # centos|redhat|red hat / debain

if [[ -f /etc/redhat-release ]]; then
    release="centos"
