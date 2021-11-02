from os import read
import selenium
from selenium import webdriver
from selenium.webdriver.common import keys
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver.v2 as us
import pytesseract

def khoitao():
    return us.Chrome()

def login(acc,pas) : 
    driver = khoitao()
    driver.get("https://accounts.google.com/")
    time.sleep(2)
    driver.find_element_by_id("identifierId").send_keys(acc)
    driver.find_element_by_id("identifierId").send_keys(Keys.ENTER)
    time.sleep(5)
    driver.find_element_by_name("password").send_keys(pas)
    driver.find_element_by_name("password").send_keys(Keys.ENTER)
    time.sleep(5)
    driver.get("https://pay.google.com/gp/w/u/0/home/activity")
    time.sleep(5)

    driver.save_screenshot("img.png")
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
    about = pytesseract.image_to_string('img.png')
    if "No activity yet" in about:
        r = open("kq.txt","r", encoding="utf-8")
        r = r.read()
        r += acc + " : Chưa thanh toán. \n"
        w = open("kq.txt","w", encoding="utf-8")
        w.write(r)
    else :
        r = open("kq.txt","r", encoding="utf-8")
        r = r.read()
        r += acc + " : Đã thanh toán. \n"
        w = open("kq.txt","w", encoding="utf-8")
        w.write(r)
    driver.close()

def star1() :
    f = open("mail.csv" ,"r", encoding="utf-8")
    f = f.read()
    lst = f.splitlines()
    for i in lst : 
        li = i.split(",")
        acc = li[0]
        pas = li[1]
        login(acc, pas)
star1()





