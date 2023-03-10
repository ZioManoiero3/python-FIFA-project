import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import json
import pandas as pd
import csv
import time
count = 2

dfPT = pd.DataFrame(columns = ['Name', 'mainPosition', 'mainRating', 'rLW', 'rST', 'rRW', 'rLF', 'rCF', 'rRF', 'rCAM', 'rLM', 'rCM', 'rRM', 'rCDM', 'rLWB', 'rRWB', 'rLB', 'rCB', 'rRB'])
dfGK = pd.DataFrame(columns = ['Name', 'mainPosition', 'mainRating'])

playerTable = []
gkTable = []

options = Options()
options.headless = True

while count < 1024:

    PATH = 'C:\Program Files (x86)\chromedriver.exe'
    driver = webdriver.Chrome(PATH, options=options)
    url = 'https://www.futhead.com/23/players/'

    if requests.get(url + str(count)).status_code != 200:
            count = count + 1
            continue
    
    driver.get('https://www.futhead.com/23/players/' + str(count))

    html= requests.get(url + str(count)).text
    soup = BeautifulSoup(html, 'lxml')

    nameSet = soup.find_all('span', itemprop = 'title')
    name = nameSet[-1].text

    mainRating = soup.find('div', 'playercard-rating').text.replace(' ', '').strip()

    mainPosition = soup.find('div', 'playercard-position').text.replace(' ', '').strip()

    if mainPosition == 'GK':
          gk = [name, mainRating, mainPosition]
          gkTable.append(gk)
          count = count +1
          continue

    rLW = driver.find_element('xpath', './html/body/div[3]/div[3]/div[1]/div[2]/ul/li/div[2]/div[2]/div[1]/div[1]/span[1]').text

    rST = driver.find_element('xpath', './html/body/div[3]/div[3]/div[1]/div[2]/ul/li/div[2]/div[2]/div[1]/div[2]/span[1]').text

    rRW = driver.find_element('xpath', './html/body/div[3]/div[3]/div[1]/div[2]/ul/li/div[2]/div[2]/div[1]/div[3]/span[1]').text

    rLF = driver.find_element('xpath', './html/body/div[3]/div[3]/div[1]/div[2]/ul/li/div[2]/div[2]/div[2]/div[1]/span[1]').text

    rCF = driver.find_element('xpath', './html/body/div[3]/div[3]/div[1]/div[2]/ul/li/div[2]/div[2]/div[2]/div[2]/span[1]').text

    rRF = driver.find_element('xpath', './html/body/div[3]/div[3]/div[1]/div[2]/ul/li/div[2]/div[2]/div[2]/div[3]/span[1]').text

    rCAM = driver.find_element('xpath', './html/body/div[3]/div[3]/div[1]/div[2]/ul/li/div[2]/div[2]/div[3]/div/span[1]').text

    rLM = driver.find_element('xpath', './html/body/div[3]/div[3]/div[1]/div[2]/ul/li/div[2]/div[2]/div[4]/div[1]/span[1]').text

    rCM = driver.find_element('xpath', './html/body/div[3]/div[3]/div[1]/div[2]/ul/li/div[2]/div[2]/div[4]/div[2]/span[1]').text

    rRM = driver.find_element('xpath', './html/body/div[3]/div[3]/div[1]/div[2]/ul/li/div[2]/div[2]/div[4]/div[3]/span[1]').text

    rCDM = driver.find_element('xpath', './html/body/div[3]/div[3]/div[1]/div[2]/ul/li/div[2]/div[2]/div[5]/div/span[1]').text

    rLWB = driver.find_element('xpath', './html/body/div[3]/div[3]/div[1]/div[2]/ul/li/div[2]/div[2]/div[6]/div[1]/span[1]').text

    rRWB = driver.find_element('xpath', './html/body/div[3]/div[3]/div[1]/div[2]/ul/li/div[2]/div[2]/div[6]/div[2]/span[1]').text

    rLB = driver.find_element('xpath', './html/body/div[3]/div[3]/div[1]/div[2]/ul/li/div[2]/div[2]/div[7]/div[1]/span[1]').text

    rCB = driver.find_element('xpath', './html/body/div[3]/div[3]/div[1]/div[2]/ul/li/div[2]/div[2]/div[7]/div[2]/span[1]').text

    rRB = driver.find_element('xpath', './html/body/div[3]/div[3]/div[1]/div[2]/ul/li/div[2]/div[2]/div[7]/div[3]/span[1]').text

    player = [name, mainPosition, mainRating, rLW, rST, rRW, rLF, rCF, rRF, rCAM, rLM, rCM, rRM, rCDM, rLWB, rRWB, rLB, rCB, rRB]
    playerTable.append(player)

    print("Player " + name + ", #" + str(count) + " is done")

    count = count + 1

dfPlayerTable = pd.DataFrame(playerTable)
dfPlayerTable.columns = ['Name', 'Position', 'Rating', 'LW Rating', 'ST Rating','RW Rating','LF Rating','CF Rating','RF Rating','CAM Rating','LM Rating','CM Rating','RM Rating','CDM Rating','LWB Rating','RWB Rating','LB Rating','CB Rating','RB Rating',]
dfPlayerTable.to_csv('FIFA Player Ratings.csv')
    
dfGKTable = pd.DataFrame(gkTable)
dfGKTable.columns = ['Name', 'Position', 'Rating']
dfGKTable.to_csv('FIFA GK Ratings.csv')