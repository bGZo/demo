# -*- coding: utf-8 -*-
# Python Selenium address : https://pypi.org/project/selenium/
# Test Address: https://www.wenjuan.com/s/6VVJZfT/

from selenium import webdriver
import random
import time

url = str(input('请输入调查问卷url：'))
t = int(input('请输入提交问卷次数：'))

for times in range(t):
    driver = webdriver.Chrome()
    driver.get(url)
    
    questions = driver.find_elements_by_css_selector('.matrix')# locate question's question 

    for answers in questions:
        answer = answers.find_elements_by_css_selector('.icheckbox_div') # locate specific question option
        if not answer: # what to do???
            blank_potion = answers.find_element_by_css_selector('.blank.option')
            blank_potion.send_keys('没有')
            continue
        choose_ans = random.choice(answer)
        choose_ans.click()
    subumit_button = driver.find_element_by_css_selector('#next_button')
    subumit_button.click()
    print('已经成功提交了{}次问卷'.format(int(times) + int(1)))

    time.sleep(1) # add time each survery
    driver.quit()
