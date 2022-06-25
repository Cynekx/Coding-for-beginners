Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print(1235)
1235
print("Cynia")
Cynia
print(true)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
print(True)
True
type(123)
<class 'int'>
type(1.4)
<class 'float'>
type(Cynia)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    type(Cynia)
NameError: name 'Cynia' is not defined
type("Cynia
     
SyntaxError: unterminated string literal (detected at line 1)
type("Cynia")
     
<class 'str'>
type("
     
SyntaxError: unterminated string literal (detected at line 1)
type(True)
     
<class 'bool'>
''' inspired by Udemy course " The perfect course for complete beginners. Friendly - No experience required. Go from scratch to coding a real app!" '''
