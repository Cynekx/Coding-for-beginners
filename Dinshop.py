'''
Aplikacja ma za zadanie stworzyc liste zakupow do wybranych posilkow.
lista zakupow bedzie obejmowala wybrana przez uzytkownika liczbe dni (user input)
uzytkownik moze modyfikowac listy posilkow w zaleznosci od preferencji
kazdy posilek bedzie mial liste  potrzebnych skladnikow

I > jesli podoba nam sie jadlospis
1. zapytaj na ile dni stworzyc plan posilkow i liste zakupow
2. wylosuj potrawy
3. zapytaj uzytkownika czy chce cos zmienic? NIE
4. stworz liste potraw
5. zapytaj czy stworzyc liste zakupow? 
5a TAK stworz liste zakupow
5b NIE pozegnaj sie
II > jesli nie podoba nam sie jadlospis
1. zapytaj na ile dni stworzyc plan posilkow i liste zakupow
2. wylosuj potrawy
3. zapytaj uzytkownika czy chce cos zmienic? TAK
4. wylosuj kolejne potrawy
5. zapytaj ponownie czy cos zmienic? NIE
6. stworz liste potraw
7. zapytaj czy stworzyc liste zakupow
7a TAK stworz liste zakupow
7b NIE pozegnaj sie

'''

from random import choice

# ***** A funkcje *****
# 1 Wybieranie dania
#len -> lenght

# wybor posilkow

def chooseMeal(days):
    while len(myMenu) < int(days): #int zmienia string w intgeger(numer)
        chosenMeal = choice(meals)
        if chosenMeal not in myMenu:
            myMenu.append(chosenMeal)
    print("Here you have! Your menu for " + answer + "days:")
    print()
    print(myMenu)
    print()
    print("My favourite one from above is... " + choice(myMenu))

# 2 tworzenie listy zakupow

def createShoppingList():
    if "salad" in myMenu:
        myShoppingList.append(salad)
    if "spaghetti" in myMenu:
        myShoppingList.append(spaghetti)
    if "tortillas" in myMenu:
        myShoppingList.append(tortillas)
    if "fruits salad" in myMenu:
        myShoppingList.append(fruitsSalad)
    if "oatmeals" in myMenu:
        myShoppingList.append(oatmeals)
    if "sandwitch" in myMenu:
        myShoppingList.append(sandwitch)
    if "chicken with rice" in myMenu:
        myShoppingList.append(chickenWithRice)
    if "carbonara" in myMenu:
        myShoppingList.append(carbonara)
    if "waffles" in myMenu:
        myShoppingList.append(waffles)
    if "pancakes" in myMenu:
        myShoppingList.append(pancakes)
    print(myShoppingList)
    
# ***** B listy *****


meals = ["salad" , "spaghetti" , "tortillas" , "fruits salad" , "oatmeals" , "sandwitch" , "chicken with rice" , "carbonara" , "waffles" , "pancakes"]


salad = ["salad", "tomatoe", "cucmber", "peppers", "spinach", "olive oil", "knorr dressing"]
spaghetti = ["pasta", "canned tomatoes", "tofu", "olive oil", "oregano", "basil", "salt", "pepper"]
tortillas = ["tortilla wraps", "salad", "tomatoes", "canned corn", "chicken breast", "peppers" , " redbeans", "olive oil", "salt", "pepper", "fajita dressing powrder"]
fruitsSalad = ["watermelon", "orange", "strawberries" "apple", "grapes", "melon", "banana", "kiwi", "honey"]
oatmeals = ["oat flakes" , "vegan milk", "banana", "white chocolate powder"]
sandwitch = ["bread", "ham", "cheese", "butter", "cucumber", "potato", "salt", "pepper"]
chickenWithRice = ["chicken breast", "rice", "Łowicz sauce", "salt", "pepper", "olive oil"]
carbonara = ["bacon", "pasta", "carbonara powder", "cream", "oil"]
waffles = ["milk", "eggs", "flour", "whipped cream", "strawberries", "blueberries"]
pancakes = ["milk", "eggs", "flour", "nutella", "bananas", "oil"]

myMenu = []
myShoppingList = []

# ***** C Flow *****

# Ile dni zaplanować?

print("Hello, my name is Dinshop and I will prepare a menu for you and a shopping list if you wish for one too!")

answer = input("For how many days do you need a menu? " )

print("Okay, I'm on it! Planning " + answer + " meal(s) for you!")

chooseMeal(answer)
# tworzenie menu


# tworzenie listy zakupow

answer = input("Would you like me to create a shopping list for chosen meals? Write y for yes ")
if answer == 'y':
    createShoppingList()
else:
    print("Okay, that's all for now. Thank you and see you soon!")

    

''' inspired by Udemy course " The perfect course for complete beginners. Friendly - No experience required. Go from scratch to coding a real app!" '''
