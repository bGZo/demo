#!/data/data/com.termux/files/usr/bin/bash
# reference
# 1. https://github.com/zsxwz/zstermux

pkgList=("git" "nodejs")
pkg update
for i in $pkgList
do
  pkg install $i
done