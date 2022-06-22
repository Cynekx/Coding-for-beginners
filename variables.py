mojeCukierki = 16

print ("***eating sweets ***")

ileCukierkowZjadlam = 5

mojeCukierki = mojeCukierki - ileCukierkowZjadlam # mozna tez napisac: mojeCukierki -=ileCukierkowZjadlam

print(mojeCukierki)


''' Przyklad drugi - obliczanie reszty z zakupow '''



moneyInWallet = 50
print(moneyInWallet)
bananasPrice = 4 #net price
salesTax1 = 0.5 * bananasPrice
bananasPrice += salesTax1 # gross price
orangesPrice = 6
salesTax2 = 0.4 * orangesPrice
orangesPrice += salesTax2
moneyInWallet = moneyInWallet - bananasPrice - orangesPrice
print(moneyInWallet)
