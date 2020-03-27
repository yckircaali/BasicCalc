Def Add (x, y):
     return x + y

Def Subtraction (x, y):
     return x - y

def Carpma (x, y):
     return x * y

def Bolme (x, y):
     return x / y

print ("Please choose what you want to do.")
print ( "0.Topl") from
print ( "1.Çıkar Up")
print ( "2.Çarp Up")
print ( "Chapter 3 on")

islem = input ("Enter your selection:")

s1 = int (input ("Number 1:"))
s2 = int (input ("2nd Issue:"))

if action == '0':
     print (s1, "+", s2, "=", Addition (s1, s2))

if action == '1':
     print (s1, "-", s2, "=", Subtraction (s1, s2))

if action == '2':
     print (s1, "*", s2, "=", Carpma (s1, s2))

if action == '3':
    try:
     print (s1, "/", s2, "=", Bolme (s1, s2))
    except ZeroDivisionError:
       print ("No number can be divided by 0!")
else:
     print ("Invalid Login")
