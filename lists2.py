men = ["Adam", "Michał", "Zenek", "Tomek"]
women = ["Zuza", "Ania", "Kasia", "Zosia" "Beata"]
people = []  #tutaj robimy listę list

people.append(men) #funkcja append dodaje elementy (tutaj do listy)
people.append(women)
print(people)
print(people[0] [3]) #wybiera najpierw listę pierwszą - 0 a pozniej element 3(zaczynajac od zera to 4)

''' inny przykład - tutaj robi jedna liste z dwoch ''' 
people = men+women
print(people)

a = [1, 2, 3]
b = [4, 5, 6]
c = a+b
print(c)
