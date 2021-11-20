#!/usr/bin/env python3
# via: https://github.com/mo-han/mo-han-toolbox/blob/f429a7d89d/__dump__/#open-new-console.py

import os

# set run path
os.environ['pythonpath'] = '.'

commandDict = {
    'nt': 'start powershell',
    'posix': 'bash'
}
os.system(commandDict[os.name])
