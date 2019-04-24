http://help.autodesk.com/cloudhelp/2017/ENU/Maya-Tech-Docs/CommandsPython/cat_Animation.html

import maya.cmds as mc

s = [i for i in range(0,10)]

#print(s)

for rad in s:
    myString = "avikSphere" + str(rad)
    mc.polySphere(name=myString, radius = 0.2 + rad/7.0)
    mc.move(0, 0, rad, myString )


# programming_fr_artists
sem4_2019


* ###### Print *

- Intro
- Basic Prints
- Comments

###### Variables

- Variable Naming
- Data Types


###### Integer and strings
- Int
- Float
- Basic Strings



###### Strings and Text

- f-string
- end1, end2, .....
- format function
- \t, \n, etc
- Slicing


###### Prompting People
----------------
i) age = input("How old are you? ")



###### Module
------
i)   sys - argv
ii)  datetime
iii) os
iv)  re



###### Loops
-----
i) For
ii)While



###### Conditionals
------------
i)   if
ii)  if-else
iii) try, except
iv)  break, continue



###### Combining loops and conditions
------------------------------
i)   even-odd numbers
ii)  fizz-buzz
iii) shopping cart



###### Function
--------
i)   Small Functions
ii)  Passing Arguements
iii) Temperature Converter
iv)  Passing Function in function
v)   lambda functions
vi)  Generator Functions
vii) Decorators
viii)Scope
ix)  Shopping List


###### Reading and writing files
-------------------------
i)   Reading Files
ii)  Writing Files
iii) Mores Files


###### Tuples and Dictionaries
------------------------
i)   Tuple
ii)  Dictionary
iii) JSON


###### Class and Objects
-----------------


###### Nuke
----
i)    Reading Documentation
ii)   __init__.py
iii)  menu.py
iv)   Writing a Nuke utility
