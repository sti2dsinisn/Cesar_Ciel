# Créé par JDP, le 9/03/2024 en Python 3

from tkinter import * #import de la bibliothèque graphique

Alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def codage_cesar():
    cle=int(cl.get())
    mot_a_coder=m.get()
    code=""                                 
    for caractere in mot_a_coder:             
        if caractere in Alphabet:         
            x = Alphabet.index(caractere) 
            y = (cle+x)%26                 
            code += Alphabet[y]           
        else:                            
            code += " "                   
    # Création d'un widget Label (texte 'coût estimé')
    Label_resultat = Label(Mafenetre, text = 'Mot codé : '+code, font="'arial',15,bold",bg='pink',fg = 'blue')
    # Positionnement du widget avec la méthode grid()
    Label_resultat.grid(row=5, column=0,columnspan=2)
                                          


# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title('César')
Mafenetre.geometry('233x150+300+300')
Mafenetre.config(background="yellow")

# Création d'un widget Label (texte 'titre de la fenetre : Codage César')
Label1 = Label(Mafenetre, text = 'Codage César',  fg = 'red')
Label1.grid(row=0, column=0, columnspan=2,sticky='ew') #occupation de toute la largeur avec sticky=ew

# Création d'un widget Label (texte 'demande clé')
Label_demandecle = Label(Mafenetre, text = 'Clé', bg='coral',fg = 'blue')
Label_demandecle.grid(row=2, column=0)

# Création d'un widget Entry (champ de saisie pour la clé)
cl=StringVar()
zone1 = Entry(Mafenetre, textvariable= cl, bg ='yellow', fg='maroon')
zone1.grid(row=2, column=1)

# Création d'un widget Label (texte 'demande mot_a_coder')
Label_demandemot_a_coder = Label(Mafenetre, text = 'mot à coder', bg='coral',fg = 'blue')
Label_demandemot_a_coder.grid(row=3, column=0)

# Création d'un widget Entry (champ de saisie)
m=StringVar()
zone2 = Entry(Mafenetre, textvariable= m, bg ='yellow', fg='maroon')
zone2.grid(row=3, column=1)

# Création d'un widget Button (bouton coder)
Bouton_calcul = Button(Mafenetre, text = 'Coder !', command = codage_cesar) #envoi vers la fonction calcul
Bouton_calcul.grid(row=4, column=0,columnspan=2)

# Création d'un widget Button (bouton Quitter)
Bouton1 = Button(Mafenetre, text = 'Quitter', command = Mafenetre.destroy)
Bouton1.grid(row=6, column=0,columnspan=2)

# Lancement du gestionnaire d'événements
Mafenetre.mainloop()
