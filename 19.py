Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
num = [10,20,30,40,50,60,70]
for i in num:
    print(num)

    
[10, 20, 30, 40, 50, 60, 70]
[10, 20, 30, 40, 50, 60, 70]
[10, 20, 30, 40, 50, 60, 70]
[10, 20, 30, 40, 50, 60, 70]
[10, 20, 30, 40, 50, 60, 70]
[10, 20, 30, 40, 50, 60, 70]
[10, 20, 30, 40, 50, 60, 70]
for i in num:
    print(i)

    
10
20
30
40
50
60
70
for i in range(len(num)):
    print("Index",i,"Value",num[i])

    
Index 0 Value 10
Index 1 Value 20
Index 2 Value 30
Index 3 Value 40
Index 4 Value 50
Index 5 Value 60
Index 6 Value 70

myColors=("Red","Black","Blue")
for j in myColors:
    print(j)

    
Red
Black
Blue
for j in range(len(myColors)):
    print(myColors[j])

    
Red
Black
Blue

fruits=("Apple","Grapes","Mango","Banana")
for f in range(len(fruits)):
    print(f)

    
0
1
2
3
for f in fruits:
    print(f)

    
Apple
Grapes
Mango
Banana

students={"Name":"Nig1","Age":24,"course":"Data science"}
for key in student:
    print(key)

    
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    for key in student:
NameError: name 'student' is not defined. Did you mean: 'students'?
>>> 
... students={"Name":"Nig1","Age":24,"course":"Data science"}
... for key in students:
...     print(key)
...     
SyntaxError: multiple statements found while compiling a single statement
>>> student={"Name":"Nig1","Age":24,"course":"Data science"}
... for key in student:
...     print(key)
...     
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> student={"Name":"Nig1", "Age":24,"course":"Data science"}
... for key in student:
...     print(key)
...     
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> student = {"Name": "Nig1", "Age": 24, "course": "Data science"}
... for key in student:
...     print(key)
... 
SyntaxError: multiple statements found while compiling a single statement
>>> student = {"Name": "Nig1", "Age": 24, "course": "Data science"}
... for key in student:
...     print(key)
... 
SyntaxError: multiple statements found while compiling a single statement
