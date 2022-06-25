''' program will be marking students' test by  given percentage'''

#ask for the percentage from test

mark = int(input("Please enter yout test mark (0-100... )"))  # int is converting strin into number

#award correct grade
'''
5: 90-100
4: 80-89
3: 70-79
2: 60-69
1: 0-69
'''
if mark >= 90:
    grade = "5"

elif mark >= 80:  #elif is a shortcut of "else if"
    grade = "4"
elif mark >= 70:
     grade = "3"
elif mark >= 60:
     grade = "2"
else:
     grade = "1"
  

#print the grade to UI

if grade == "1":
    print("Ooops, you did not pass the test. Better luck nex time!")
else:
    print("Well done! You got a grade of: " + grade)
''' inspired by Udemy course " The perfect course for complete beginners. Friendly - No experience required. Go from scratch to coding a real app!" '''
