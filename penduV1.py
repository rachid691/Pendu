#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 08:05:12 2021

@author: rachid.emziane
"""

import random as rd

def choix_mot():
    
    fichier = open('mots.txt','r')
    liste = []
    for mot in fichier:
        mot=mot.lower()
        mot = mot[:-1]
        liste += [mot]
    i = rd.randint(0,len(liste)-1)
    choix = liste[i]
    fichier.close()
    return choix
    

def jeu(choix,mot_dev,l):
    tour = 1
    score = 0
    lettre = [l]
    mot_devine = mot_dev
    while mot_devine != choix:
        for j in range(1,len(choix)):
            if l == choix[j]:
                mot_devine = mot_devine[:j] + l + mot_devine[j+1:]
                print(mot_devine)
                
        tour+=1
        print('Vous êtes au tour',tour)
        if mot_devine==choix:
            score +=1
            print ('Bien joué! Votre score est')
            break
        elif tour == 8:
            score -=1
            print ('C est perdu! Le bon mot était ',choix,' et votre score est ', score)
            break
        else :
            l = input("Saisissez une lettre: ")
            while l in lettre :
                l = input("Vous avez déjà saisi cette lettre.\nChoisissez une autre: ")
            lettre += [l]

def main():
    choix = choix_mot()
    mot_dev = choix[0]+'_'*((len(choix)-1))
    print('Le mot a trouvé est :',mot_dev)
    lettre = input("Saisissez une lettre: ")
    jeu(choix,mot_dev,lettre)
    replay = input("Saisissez 1 pour rejouer et 0 pour quitter: ")
    if replay == '1':
        main()


a=main()
print(a)
