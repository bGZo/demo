#!/bin/sh
## Usage: myscript [options] ARG1
##
## Options:
##   -h, --help    Display this message.
##   -n            Dry-run; only show what would be done.
##

usage() {
  [ "$*" ] && echo "$0: $*"
  sed -n '/^##/,/^$/s/^## \{0,1\}//p' "$0"
  exit 2
} 2>/dev/null

main() {
  while [ $# -gt 0 ]; do
    case $1 in
    (-n) DRY_RUN=1;;
    (-h|--help) usage 2>&1;;
    (--) shift; break;;
    (-*) usage "$1: unknown option";;
    (*) break;;
    esac
  done
  : do stuff.
}

main "$@"
