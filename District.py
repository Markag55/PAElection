# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 18:19:04 2020

@author: Mark
"""

from Candidet import Candidet
class District:
    name = ""
    candidet1 = Candidet()
    candidet2 = Candidet()
    def District(newName, candidet1, candidet2):
        District.name = newName
        candidet1 = Candidet(candidet1)
        if(candidet2 != ""):
            candidet2 = Candidet(candidet2)
    
        