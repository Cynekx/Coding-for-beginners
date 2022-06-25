#w Pythonie listy zaczynaja sie od 0 a nie od 1!!

fruits = ["oranges", "apples", "grapes", "melons", "dragon fruits", "papayas"]
vegetables = ["cucumber", "tomato", "potato", "carrots"]
print(fruits)
print(fruits[0])
print(fruits[5])
print(fruits[3], vegetables[0])

#mozna zmienic nazwe danej i ona zmieni sie po kolejnym egzekwowaniu kodu:

fruits[0] = "kiwi"
print(fruits)

#dodawanie na koniec listy nowego itemu za pomoca kodu:

fruits.append("watermelon")
print(fruits)

print(len(fruits), len(vegetables))
''' inspired by Udemy course " The perfect course for complete beginners. Friendly - No experience required. Go from scratch to coding a real app!" '''
