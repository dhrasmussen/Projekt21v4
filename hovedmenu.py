#https://github.com/Klybech/Projekt-2.1.git

import fibersm
import fibermm
import udgravningby
import dok
import time



def prmenu():
    print("1) Single Mode, MAX 50km ") #
    print("2) Multi Mode, MAX 2km ") #
    print("3) Kabel nedgravning ") #
    print("10) DOK")# OBS OBS OBS OBS
    print("4) Afslut program") # afslutter programmet
    print("")

prmenu()
taller=int(input())

while True:
    if taller==1:
        fibersm.udregnsm()
        prmenu()
        taller=int(input())
    if taller==2:
        fibermm.udregnmm()
        prmenu()
        taller=int(input())
    if taller==3:
        udgravningby.gravby()
        prmenu()
        taller=int(input())
    if taller==10:              #OBS OBS OBS
        dok.dok()
        prmenu()
        taller=int(input())
    if taller ==4:
        print("Programmet afsluttes!!!")
        break
    else:
        print("tastefejl, prøv igen!")
        prmenu()
