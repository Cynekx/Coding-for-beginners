''' Python counting script '''
# "while" loop
count = 0
while count < 5:
    print(count)
    count += 1 # this is the same as count plus one
print("done!")

#use sqquare brackets [] to make lists 


# "for" loop:

myList = ["apples", "oranges", "bananas"]
for item in myList:
    print(item)
a = [1, 2, 3]
for element in a:
    print(element)
    
b = [20, 10, 5]
total = 0
for element in b:
    total = total + element  #shortcut > total += element
print(total)


c = list(range(1,5)) # range is creating list of numbers from 1 to 4
print(c)

for number in range(1,6):
    print(number)

x=0
for x in range(5,10):
    if(x==7): break   #if it gets to 7, stops executing the code.
    print(x)

    
