# ------------------------------- Information --------------------------------- #
"""
Titel: Bussen
Författare: Joel, Lukas
Datum: 2025-01-16
Det här är ett program för hantering av passagerare på en buss. Programmet
lagrar passagerare i en lista.
"""

# Importera random för att generera slumpmässiga reaktioner
import random as rand

# ----------------------------- Klassdefinitioner ---------------------------- #
class Person:
   
    def __init__(self, namn, ålder):
        self.namn = namn
        self.ålder = ålder

    def __str__(self):
        return f"{self.namn}, {self.ålder} år gammal."

    def setNamn(self, nyttNamn):
        self.namn = nyttNamn

    def setÅlder(self, nyÅlder):
        self.ålder = nyÅlder

    def getNamn(self):
        return self.namn

    def getÅlder(self):
        return self.ålder

# ------------------------- Funktionsdefinitioner ---------------------------- #
# En lista för att lagra passagerare
buss = []

def validName(namn):        #Kontrollerar att namnet endast inehåller bokstäver
    return namn.isalpha()

def validAge(ålder):        #Kontrollerar att ålder endast skrivs med siffror
    try:
        ålder = int(ålder)
        return ålder<0
    except ValueError:
        return False

def plockaUpp():
    
    if len(buss) >= 25:
        print("Bussen är full.")
        return

    namn = input("Ange förnamn:")
    while not validName(namn):
        print("Skriv ditt namn med endast bokstäver!")
        namn = input("Ange namn: ")
    
    ålder = int(input("Ange ålder: "))
    while not validAge(ålder):
        print("Skriv ålder med siffror!")

        person = Person(namn.capitalize(), int(ålder))
        buss.append(person)
        print(f"{namn.capitalize()} har stigit på bussen.")
    else:
        print("Bussen är full.")

def gåAv():
    
    namn = input("Ange namn på passageraren som ska gå av: ")
    for person in buss:
        if person.getNamn().lower() == namn.lower:
            buss.remove(person)
            print(f"{namn} har gått av bussen.")
            return
    print(f"{namn} finns inte på bussen.")

def skrivUt():
    
    if buss:
        for person in buss:
            print(person)
    else:
        print("Inga passagerare på bussen.")

def sammanlagdÅlder():
    if buss:
        total = sum(person.getÅlder() for person in buss)
        print(f"Sammanlagd ålder: {total} år.")
        return total

    else:
        print("Inga passagerare på bussen")
        return 0

def medelÅlder():
    
    if buss:
        total = sammanlagdÅlder()
        medel = round(total / len(buss))
        print(f"Medelålder: {medel} år.")
        return medel
    else:
        print("Inga passagerare på bussen.")

def äldst():
   
    if buss:
        äldsta = max(buss, key=lambda person: person.getÅlder())
        print(f"Den äldsta passageraren är {äldsta}")
    else:
        print("Inga passagerare på bussen.")

def busSort():
   
    if buss:
        buss.sort(key=lambda person: person.getNamn())
        print("Passagerarna har sorterats i alfabetisk ordning.")
    else:
        print("Inga passagerare på bussen")

def hittaPassagerare():
    
    if not buss:
        print("Inga passagerare på bussen.")
        return

    print("""
    Välj ett åldersspann:
    1. 0-20
    2. 21-40
    3. 41-60
    4. 61-70
    5. 71+
    """)
    val = input("-> ")

    if val == "1":
        min_ålder, max_ålder = 0, 20
    elif val == "2":
        min_ålder, max_ålder = 21, 40
    elif val == "3":
        min_ålder, max_ålder = 41, 60
    elif val == "4":
        min_ålder, max_ålder = 61, 70
    elif val == "5":
        min_ålder, max_ålder = 71, 110
    else:
        print("Ogiltigt val. Försök igen.")
        return

    resultat = [person for person in buss if min_ålder <= person.getÅlder() <= max_ålder]
    
    if resultat:
        print(f"Passagerare mellan {min_ålder} och {max_ålder} år:")
        for person in resultat:
            print(person)
    else:
        print(f"Finns inga passagerare mellan {min_ålder} och {max_ålder} år.")

def peta():
    if not buss:
        print("Inga passagerare på bussen")
        return
   
    namn = input("Ange namn på passageraren att peta på: ")
    for person in buss:
        if person.getNamn() == namn:
            reaktioner = ["suckar", "ler", "ignorerar dig", "tittar argt på dig", "svarar med 'What the sigma'"]
            reaktion = rand.choice(reaktioner)
            print(f"{namn} {reaktion}.")
   

# ------------------------------ Huvudprogram --------------------------------- #
def main():
   
    menyVal = ""

    while menyVal != "q":
        print("""
                                         --- MENY ---
                    Välkommen till buss-simulatorn. Välj ett av alternativen nedan:
            1. Plocka upp ny passagerare                        2. Låt passagerare gå av
            3. Skriv ut alla passagerare                        4. Beräkna sammanlagd ålder
            5. Beräkna medelåldern                              6. Hitta äldst person
            7. Sortera bussen                                   8. Hitta personer inom ett specifikt åldersspann
            9. Peta på passagerare                              q. Avsluta
        ---------------------------------------------------------------------------------------
        """)

        menyVal = input("-> ")

        if menyVal == "1":
            plockaUpp()
        elif menyVal == "2":
            gåAv()
        elif menyVal == "3":
            skrivUt()
        elif menyVal == "4":
            sammanlagdÅlder()
        elif menyVal == "5":
            medelÅlder()
        elif menyVal == "6":
            äldst()
        elif menyVal == "7":
            busSort()
        elif menyVal == "8":
            hittaPassagerare()
        elif menyVal == "9":
            peta()
        elif menyVal == "q":
            print("Bussen körde av vägen pga ishalka")
        else:
            print("Ogiltigt val. Försök igen.")
    
    print("""
                                           _____________
                                         _/_|[][][][][] | - -
                                        ( SL - Lokalbuss| - -
                                        =--OO-------OO--=
    """)

main()