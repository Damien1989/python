def afficher_informations_personne(nom, age):
    print()
    print("Vous vous appelez " + nom + " et vous avez " + str(age) + " ans ")
    print("L'an prochain vous aurez " + str(age+1) + " ans")


    if age >= 60:
        print("Vous êtes senior")
    elif age >= 18:
        print("Vous êtes majeur")
    elif age == 18:
        print("Félicitations ! Tu peux fuir tes parents !")
    elif age <= 10:
        print("Vous êtes enfant")
    else:
        print("Vous êtes mineur")


def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ?")
        return reponse_nom

def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + "Quel est votre âge? ")
        try: 
            age_int = int(age_str)
        except:
            print("ERREUR")
        return age_int

# demander nom
nom1 = demander_nom()
nom2 = demander_nom()

# demander age
age1 = demander_age(nom1)
age2 = demander_age(nom2)

# afficher résultats 

afficher_informations_personne(nom1, age1)
afficher_informations_personne(nom2, age2)