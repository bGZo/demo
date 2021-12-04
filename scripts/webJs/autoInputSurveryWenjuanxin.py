#!/usr/bin/python3
# author: bGZoCg
# update: 211205
# requirement.txt
    # selenium@4.1.0

import time
import random

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

url = str(input('Url: '))
times = int(input('Loop Num: '))

for t in range(times):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    questions = driver.find_elements(By.CLASS_NAME, 'question')
    for question in questions:
        answers = question.find_elements(By.CLASS_NAME, 'init_option')

        if not answers:
            print('None')
            continue

        if(question.get_dom_attribute('questiontype')=='2'): # single
            random.choice(answers).click()
        if(question.get_dom_attribute('questiontype')=='3'): # multi
            odd = random.randint(1,len(answers))
            while odd%2==0:
                odd = random.randint(1,len(answers))
            # NOTE: odd let multi question must choose one.

            for i in range(odd):
                random.choice(answers).click()

    # time.sleep(30) # Note: check for your random data

    driver.find_element(By.ID, 'next_button').click()
    print('[{}] sucessfully'.format(int(t) + int(1)))

    time.sleep(5)
    driver.close() # TODO: driver.quit() vs driver.close()
