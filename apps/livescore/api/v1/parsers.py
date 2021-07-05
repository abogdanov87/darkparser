from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import re
    

def get_match_results(url, delay=0):
    try:
        driver = webdriver.Safari()
        driver.get(url)
        import pdb; pdb.set_trace()
        container = driver.find_element_by_class_name('sportName soccer')
        content = BeautifulSoup(container.get_attribute('innerHTML'), 'html.parser')
        driver.close()
    except:
        pass
    return True
