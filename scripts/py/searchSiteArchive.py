#!/usr/bin/python3
# author: bGZoCg
# update: 211120
# using api offered by arhive.org, refer to 
# https://archive.org/help/wayback_api.php

import argparse
import requests
import json

def search_archive_of_site(site):
    requestUrl='https://archive.org/wayback/available?url=' + site
    respond=requests.get(requestUrl)
    data = (json.loads(respond.text))['archived_snapshots']
    if data:
        print(data['closest']['url'])
    else:
        print('the site [' + site +'] not archive, so go https://web.archive.org/save to archive!')

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='read url')
    parser.add_argument('str', metavar='N', type=str, nargs='+',
                        help='url you wanna search, use space to discriminate')
    args = parser.parse_args()

    for site in args.str:
        search_archive_of_site(site);
