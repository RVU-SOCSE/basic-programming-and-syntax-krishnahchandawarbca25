Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
mylist = [10,20,30,40]
mylist.append(50)
mylist
[10, 20, 30, 40, 50]
mylist.insert(1,20)
mylist
[10, 20, 20, 30, 40, 50]
mylist.index(40)
4
mylist.pop(2)
20
>>> mylist.remove
<built-in method remove of list object at 0x00000218793CB300>
(
>>> mylist.remove(20)
>>> mylist
[10, 30, 40, 50]
>>> mylist.reverse()
>>> mylist
[50, 40, 30, 10]
>>> mylis.sort()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    mylis.sort()
NameError: name 'mylis' is not defined. Did you mean: 'mylist'?
>>> mylist.sort()
>>> mylist
[10, 30, 40, 50]
>>> mylist.extend([60,70])
>>> mylist
[10, 30, 40, 50, 60, 70]
>>> mylist.append(50)
>>> mylist
[10, 30, 40, 50, 60, 70, 50]
>>> mylist.count(50)
2
>>> mylist.count(10)
1
>>> mylist.copy()
[10, 30, 40, 50, 60, 70, 50]
mylist.clear()
mylist
[]
