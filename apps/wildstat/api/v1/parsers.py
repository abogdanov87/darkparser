from bs4 import BeautifulSoup
import requests
import time
import re
    

def get_match_results(url, delay=0):
    time.sleep(delay)
    
    resp = requests.get(url)
    content = BeautifulSoup(resp.text, 'html.parser')

    results = []
    tour = None
    match_date = None
    match_time = None
    place = None
    home_team = None
    away_team = None
    home_team_id = None
    away_team_id = None
    home_team_score = None
    away_team_score = None

    boxes = content.findAll('div', class_='box')
    for box in boxes:
        if box.find('div', class_='tour'):
            tour = box.find('div', class_='tour').text
        trs = box.findAll('tr')
        for tr in trs:
            try:
                match_time = tr.findAll('td')[1].find('span').text.replace('\xa0','')
                match_date = tr.findAll('td')[1].find('a').text.replace('\xa0','')
                home_team = tr.findAll('td')[3].find('a').text.replace('\xa0','')
                away_team = tr.findAll('td')[5].find('a').text.replace('\xa0','')
                home_team_id = tr.findAll('td')[3].find('a')['href'].split('/').pop()
                away_team_id = tr.findAll('td')[5].find('a')['href'].split('/').pop()
                home_team_score = tr.findAll('td')[7].find('b').text.split(':')[0]
                away_team_score = tr.findAll('td')[7].find('b').text.split(':')[1]
                if tr.findAll('td')[7].find('span').text.__contains__('д.в.'):
                    txt = tr.findAll('td')[7].find('span').text
                    score = re.findall(r'.*?\(([^)]*)\).*', txt).pop().replace(' ', '').split(',').pop()
                    home_team_score = score.split(':')[0]
                    away_team_score = score.split(':')[1]
                place = tr.findAll('td')[1].findAll('div')[0].text.replace('\xa0','')
            except:
                pass
            try:
                place = tr.findAll('td')[1].findAll('div')[0].text.replace('\xa0','')
            except: 
                continue
            results.append({
                'tour': tour,
                'match_date': match_date,
                'match_time': match_time,
                'place': place,
                'home_team_title': home_team,
                'away_team_title': away_team,
                'home_team_id': home_team_id,
                'away_team_id': away_team_id,
                'home_team_score_ft': home_team_score,
                'away_team_score_ft': away_team_score,
            })
    
    return results
