#!/usr/bin/python3
# author: bGZoCg
# update: 211205
# requirement.txt
    # selenium@4.1.0
    # argparase

import time
import random

import argparse

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def get_drive_info_from_div_class(driver, findThings):
    try:
        return driver.find_elements(By.CLASS_NAME, findThings)
    except Exception as e:
        print('[Find ' + findThings + ' Failed]')


def get_drive_typeinfo_form_dom_div(driver, findThings):
    try:
        return driver.get_dom_attribute(findThings)
    except Exception as e:
        print('[Find Dom ' + findThings + ' Failed]')


def random_click_some_of_list(list, type):
    try:
        random.choice(list).click()
    except Exception as e:
        print('[Click '+ type + ' Failed]')


def main(url, time, check):
    for t in range(times):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url)

        questions = get_drive_info_from_div_class(driver,'question')
        for question in questions:
            answers = get_drive_info_from_div_class(question, 'init_option')

            if(get_drive_typeinfo_form_dom_div(question, 'questiontype')=='2'): # single
                random_click_some_of_list(answers, '2')

            if(get_drive_typeinfo_form_dom_div(question, 'questiontype')=='3'): # multi
                odd = random.randint(1,len(answers))
                while odd%2==0:
                    odd = random.randint(1,len(answers))
                # NOTE: odd let multi question must choose one.
                for i in range(odd):
                    random_click_some_of_list(answers, '3')

        if check == True:
            time.sleep(30) # Note: check for your random data

        driver.find_element(By.ID, 'next_button').click()
        print('[{}] sucessfully submit!'.format(int(t) + int(1)))

        time.sleep(2)
        driver.close() # TODO: driver.quit() vs driver.close()


if __name__=='__main__':
    parser =argparse.ArgumentParser(description='Wen Juan Wang Script.')
    parser.add_argument('url', metavar='url', type=str,
                    help='input url you want to visit')
    parser.add_argument('-t','-time', dest='t',
                    default='1',
                    help='cnt for loop')
    parser.add_argument('-c','-check', dest='check',
                    action='store_const',
                    default=False, const=True,
                    help='give a minute to check your data.')
    args = parser.parse_args()

    url = args.url
    times = int(args.t)
    check = args.check
    print(check)

    main(url, time, check)