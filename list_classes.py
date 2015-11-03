#
# This file is used for students to enter their schedules. This will allow our homework program to grab homework. 
#

classes = ['math','science','advanced math', 'ss', 'la', 'spanish']
my_schedule = []

for i,p in enumerate(classes):
       print str(i) + ". " + p  
       
my_classes = input("What class do you have A block? ")

if my_classes in range(len(classes)):
    print("this is a valid choice")
    my_schedule.append(classes.pop(my_classes))
else: 
    print("this is not a valid choice")    
