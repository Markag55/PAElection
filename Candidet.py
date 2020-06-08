# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 18:27:47 2020

@author: Mark
"""

class Candidet:
    name = ""
    district = ""
    percent = ""
    votes = ""
    party = ""
    def make_candidet(newDistrict, newName, newPercent, newParty, newVotes):
        candidet = Candidet()
        candidet.name = newName
        candidet.district = newDistrict
        candidet.percent = newPercent
        candidet.votes = newVotes
        return candidet
        
        