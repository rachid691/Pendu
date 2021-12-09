#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 08:05:12 2021

@author: rachid.emziane
"""

import random as rd
# from tkinter import Tk, Label, Button, Canvas, PhotoImage, StringVar

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
        for i in range(1,len(choix)):
            if l == choix[i]:
                mot_devine = mot_devine[:i] + l + mot_devine[i+1:]
                print(mot_devine)                
        tour+=1
        print('Vous êtes au tour',tour)
        if mot_devine==choix:
            score +=1
            print ('Bien joué! Votre score est',score)
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

# def rejouer():
#     replay = input("Saisissez 1 pour rejouer et 0 pour quitter: ")
#     if replay == '1':
#         main()
        
# def affichage_mot():
#     choix = choix_mot()
#     mot_dev = choix[0]+'_'*((len(choix)-1))
#     print('Le mot a trouvé est :',mot_dev)
    
def main():
    print("Vous avez 8 chaces pour trouver le mot")
    choix = choix_mot()
    mot_dev = choix[0]+'_'*((len(choix)-1))
    print('Le mot a trouvé est :',mot_dev)
    letters = tuple("abcdefghijklmnopqrstuvwxyz")
    lettre = input("Saisir une lettre : ")
    while lettre not in letters:
        print("Votre saisie n'est pas valide, réessayez...")
        lettre = input("Saisir une lettre : ")
    jeu(choix,mot_dev,lettre)
    replay = input("Saisissez 1 pour rejouer et 0 pour quitter: ")
    if replay == '1':
        main()

a=main()
print()

# fenetre = Tk()
# fenetre.title("Jeu du pendu")


# image1=PhotoImage(master=fenetre,file='bonhomme1.gif')
# image2=PhotoImage(master=fenetre,file='bonhomme2.gif')
# image3=PhotoImage(master=fenetre,file='bonhomme3.gif')
# image4=PhotoImage(master=fenetre,file='bonhomme4.gif')
# image5=PhotoImage(master=fenetre,file='bonhomme5.gif')
# image6=PhotoImage(master=fenetre,file='bonhomme6.gif')
# image7=PhotoImage(master=fenetre,file='bonhomme7.gif')
# image8=PhotoImage(master=fenetre,file='bonhomme8.gif')

# Largeur = 1000
# Hauteur= 800
# Canevas = Canvas(fenetre, width = Largeur, height =Hauteur)
# item=Canevas.create_image(700,300,image=image1)
# Canevas.pack()


# labelMotRech=Label(fenetre, textvariable=affichage_mot() ,fg='black')
# labelMotRech.pack()


# labelHello = Label(fenetre, text = "Hello World !", fg='blue')
# labelHello.pack()

# buttonrejouer=Button(fenetre, text="QUITTER", fg= 'red', command= fenetre.destroy)
# buttonrejouer.pack()

# fenetre.mainloop()
