from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import threading
import os
import tarfile
import gzip
import time


loggin = 'froztest'
loggin1 = 'letusenter'
password = '12123434Qq'
url = 'https://www.bet365.com.cy/en/'

def browser_setup():
    # chromeOptions = webdriver.ChromeOptions()  might use later
    browser = webdriver.Chrome(executable_path = '/Users/frozmannik/PycharmProjects/betting/files/mac/chromedriver')  # fake Chrome browser mac
    # browser = webdriver.Chrome('C:\\Users\Frozm\PycharmProjects\\biologyScrapeData\\files\win\chromedriver.exe')
    return browser

def open_url(url):
    browser = browser_setup()
    browser.get(url)
    login(browser)
    while True:
        pass


def accept_terms(browser):
    while True:
        try:
            accept_btn = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'css-oe4so')))
            #myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.NAME, 'q')))
            print("Terms are accepted")
            accept_btn.click()
        except TimeoutException:
            print ("Cant accept terms")
            browser.refresh()
            continue
        break

def login(browser):
    while True: # click button
        try:
            banner_btn = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'lpgb')))
            banner_btn.click()

        except TimeoutException: # if internet sucks
            print("cant load the page")
            browser.refresh()
            continue
        break

    #log_form = WebDriverWait(browser, 50).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'input')))
    log_form = WebDriverWait(browser, 50).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'input')))

    #print(log_form)
   # log_form.clear()
   # WebDriverWait.send_keys_to_element(log_form[0],login)
   # WebDriverWait.send_keys_to_element(log_form[1], password)
    log_form[1].send_keys(password)

    log_form[0].send_keys(loggin)
    btn_go = WebDriverWait(browser, 50).until(EC.presence_of_element_located((By.CLASS_NAME, 'hm-Login_LoginBtn ')))
    btn_go.click()

    time.sleep(5)
    print(browser)
    frame = WebDriverWait(browser, 50).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'iframe')))
    print(frame)
    browser.switch_to.frame(frame[1])
    print("switched")
    print(browser)
    #this is temporary

    # check if its error log in again
    while True:
        print("here")
        try:

            btn_verify = WebDriverWait(browser, 50).until(EC.presence_of_element_located((By.ID, 'remindLater')))
            print(btn_verify)
            btn_verify.click()
            browser.switch_to.default_content()
        except Exception as e:
            print(str(e))
            browser.refresh()
            continue
        print("ffff")
        break



    print("hhh")
    error_lbl = WebDriverWait(browser, 100).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'wl-FailedLogin_Redblurb ')))
    print(error_lbl)



    #log_form[0].send_keys('froztest')
    # log_form[0].send_keys('test')

    #log_form[1].send_keys('1212')
    #log_form[1].send_keys('3434')
    #log_form[1].send_keys('Qq')
    #log_form[2].send_keys('tete')
    #log_form = browser.find_elements_by_class_name('hm-Login_InputField ')
    #test=browser.execute_script("document.getElementsByClassName('hm-Login_UserNameWrapper ').innerHTML = 'ttttt'; ")

   # log_form.send_keys(login)
   # browser.find_elements_by_class_name('hm-Login_InputField ').clear()
   # browser.find_elements_by_class_name('hm-Login_InputField ').send_keys(password)
    #print(browser)






def main():
    open_url(url)

if __name__ == '__main__':
    main()
