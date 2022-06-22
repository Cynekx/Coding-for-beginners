men = ["Adam", "Michał", "Zenek", "Tomek"]
women = ["Zuza", "Ania", "Kasia", "Zosia" "Beata"]
people = []

people.append(men) #funkja append dodaje elementy (tutaj do listy)
people.append(women)
print(people)
print(people[0] [3]) #wybiera najpierw listę pierwszą - 0 a pozniej element 3(zaczynajac od zera to 4)

people = men+women
print(people)
''' inny przykład '''
a = [1, 2, 3]
b = [4, 5, 6]
c = a+b
print(c)
