from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os
import requests
import time
import re
from config.settings import SERVER
    

def get_match_results(url, delay=0):
    results = []
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(executable_path=binary_path)
    try:
        driver.get(url)
        container = driver.find_element_by_id('live-table')
        content = BeautifulSoup(container.get_attribute('innerHTML'), 'html.parser')
        matches = content.findAll(attrs={'title': 'Подробности матча!'})
        # import pdb; pdb.set_trace()
        match_link = ''
        home_team = ''
        away_team = ''
        score_home = None
        score_away = None
        for match in matches:
            # import pdb; pdb.set_trace()
            match_link = match['id'].split('_').pop()
            try:
                home_team = match.find('div', class_='event__participant event__participant--home').text
            except:
                home_team = match.find('div', class_='event__participant event__participant--home fontBold').text
            try:
                away_team = match.find('div', class_='event__participant event__participant--away').text
            except:
                away_team = match.find('div', class_='event__participant event__participant--away fontBold').text
            try:
                if match.find('div', class_='event__scores fontBold').find('div', class_='event__part'):
                    match_part = match.find('div', class_='event__scores fontBold').find('div', class_='event__part')
                    score_home = match_part.text.replace('(', '').replace(')', '').replace(' ', '').replace('\xa0', '').split('-')[0]
                    score_away = match_part.text.replace('(', '').replace(')', '').replace(' ', '').replace('\xa0', '').split('-')[1]
                else:
                    score_home = match.find('div', class_='event__scores fontBold').text.replace('\xa0', '').split('-')[0]
                    score_away = match.find('div', class_='event__scores fontBold').text.replace('\xa0', '').split('-')[1]
            except:
                score_home = None
                score_away = None
            results.append({
                'match_link': match_link,
                'tour': None,
                'match_date': None,
                'match_time': None,
                'place': None,
                'home_team_title': home_team,
                'away_team_title': away_team,
                'home_team_id': None,
                'away_team_id': None,
                'home_team_score_ft': score_home,
                'away_team_score_ft': score_away,
            })
    except:
        pass
    try:
        driver.close()
    except:
        pass
    return results
