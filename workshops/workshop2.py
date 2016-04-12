score = float(input("Enter score: "))
if score < 0:
   print("Invalid score")
else:
   if score > 100:
       print("Invalid score")
   elif score > 50:
       print("Passable")
   if score >= 90:
     print("Excellent")
   elif score < 50:
    print("Bad")

print("************************************************************")

option=input("Enter an option : ")
if option=='a':
 print("HELLO")
 if option=='b':
  print("GOODBYE...")
while option !='c':

   option1=input("Enter an option : ")
   if option1=='a':
    print("HELLO")
   elif option1=='b':
    print("GOODBYE...")
   elif option1=='c':
    print ("you quit the program")

print("*************************************************************")


