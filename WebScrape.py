# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:16:35 2020

@author: Mark
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Candidet import Candidet
import re
import json

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options = op)
driver.get('https://www.electionreturns.pa.gov/General/OfficeResults?OfficeID=13&ElectionID=63&ElectionType=G&IsActive=0')

try:
    main = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "col-xs-12"))
            )
    curr = main.text
    
    ln = re.split('\n', curr)
    
    
except:
    driver.quit()

driver.quit()
title = ln[0]
candidets = []
currDistrict = ""
currCandidet = ""
currParty = ""
currPercent = ""
currVotes = ""
for i in range(1,len(ln)):
    if("District" in ln[i]):
        currDistrict = ln[i]
        #print(currDistrict)
    if("County Breakdown" in ln[i]):
        continue
    if("," in ln[i] and not "Votes:" in ln[i]):
        currCandidet = ln[i]
        #print(currCandidet)
    if("(DEM)" in ln[i] or "(REP)" in ln[i] or "(D/R)" in ln[i] or "(LIB)" in ln[i] or "(NOA)" in ln[i] or "(IND)" in ln[i] or "(GRN)" in ln[i]):
        currParty = ln[i]
        #print(currParty)
    if("%" in ln[i]):
        currPercent = ln[i]
        #print(currPercent)
    if("Votes:" in ln[i]):
        currVotes = ln[i]
        #print(currVotes)
        newCandidet = Candidet.make_candidet(currDistrict, currCandidet, currPercent, currParty, currVotes)
        candidets.append(vars(newCandidet))
with open("data.txt", "w") as file:
    json.dump(candidets, file)
        