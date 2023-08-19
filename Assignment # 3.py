#Assignment No. 1-B

# Write a python program to print the following string in a spexcific format.
# print ("Twinkle, Twinkle, Little star\n\tHow I wonder what you are!\n\t\t Up above the world so high,\n\t\t Like a diamond in the sky.\n Twinkle, Twinkle, Little star\n\tHow I wonder what you are ")


#Write a python program to get the python version you are using.

# import sys
# print("System Version")
# print (sys.version)
# print ("version info")
# print (sys.version_info)

#Write a python program to display the current date and time.

# import datetime
# current_datetime = datetime.datetime.now()
# print (current_datetime)

#Write a python program which accept the radius of a circle from the user and compute the area.

# rad = int(input("Enter radius of a circle: "))
# print (rad)
# Area = 3.14*rad*rad
# print (Area)

# rad = float(input("Enter radius of a circle: "))
# print (rad)
# Area = 3.14*rad*rad
# print (Area)

#write a python program which accept the user's forst and last name and print them in reverse order with a space between them.

# First_Name = input("Enter First_Name: ")
# Last_Name = input("Enter Last_Name: ")
# print (Last_Name +" "+ First_Name)

#Write a python program which tskes two inputs from user and print them addition

# num_1 = int(input("Enter num_1: "))
# num_2 = int(input("ENter num_2: "))
# sum = num_1 + num_2
# print ("the sum of two numbers is:" ,sum)


#Write a program ehich takes five input from user for different subject's makrs, total it and genrate marksheet using grades.

# Student_name = input("Enter Student Name: ")
# Roll_number =  int (input ("Enter Roll number: "))
# Standard = int (input ("Enter Standard: "))   
# English = int (input ("Enter English Marks: ")) 
# Math = int (input ("Enter Math Marks: ")) 
# Islamiat = int (input ("Enter Islamiat Mark: ")) 
# Biology = int(input("Enter Biology Marks: "))
# Chemistry = int(input("Enter Chemistry Marks: "))
# Marks_Obtained = English + Math + Islamiat + Biology + Chemistry
# print (Marks_Obtained)
# Total_Marks = 500
# perc = (Marks_Obtained / Total_Marks)*100
# print (perc)
# if perc <=100 and perc >= 90:
#     print("Grade: A+")
# elif perc <=90 and perc >=80:
#     print("Grade: A")
# elif perc <=80 and perc >=70:
#     print("Grade: B+")
# elif perc <=70 and perc >=60:
#     print("Grade: B")
# elif perc <= 60 and perc >=50:
#     print("Grade: C+")
# elif perc <=50 and perc >=40:
#     print("Grade:D (Fail)")
# elif perc <100 or perc > 50:
#     print ("Put the correct grade")
# else:
#     print ("Result: Fail")

#Write a program which take input from user and identify that the given number is even or odd?
# A = int(input("Enter the number: "))
# if (A %1 ==1):
#     print (A, "is even number")
# else: print(A, "is odd number")

# Write a program which print the length of the list?
# country = ["Pakistan", "India", "China", "Russia", "Afghanistan"]
# print(len(country)

# #Write a Python program to sum all the numeric items in a list?
# def sum_list(lst):
#     sum_numbers = 0
#     for item in lst:
#         if isinstance(item,(int,float)):
#             sum_numbers += item
#     return sum_numbers
# my_list = ["hammna","hira","Fatima",34,25,2.0,True]
# total_sum = sum_list(my_list)
# print(total_sum)

# Write a Python program to get the largest number from a numeric list.
# l = [65, 609, 45, 768, 43, 467,]
# print(max(l))

# Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Write a program that prints out all the elements of the list that are less than 5.
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for items in a:
#     if items <5:
#       print(items,end=",")

# 1. Make a calculator using Python with addition , subtraction ,multiplication ,division and power.
# v1 = int(input("Enter Value: "))
# v2 = int(input("Enter value: "))
# v3 = input("Enter math operation:")
# sum = v1 +v2
# sub = v1- v2
# mul = v1 * v2
# div = v1 / v2
# if(v3 == "+"):
#     print("Your Answer is:"+ str(sum))
# elif(v3 == "-"):
#     print("Your Answer is:"+ str(sub))
# elif(v3 == "*"):
#     print("Your Answer is:"+ str(mul))
# elif(v3 == "/"):
#     print("Your Answer is:"+ str(div))
# else:
#     print("You put wrong operator")

#Write a program to check if there is any numeric value in list using for loop.
# def has_num_value(lst):
#     for item in lst:
#         if isinstance(item,(int,float)):
#             return True
#     return False
# my_list = [10,20,30,40,50]
# result = has_num_value(my_list)
# if result:
#     print("In list there is numeric value exist")
# else:
#     print("No numberic value exist")

# Write a Python script to add a key to a dictionary.
# d1={
#     "primary_colour" : "red",
#     "secondary_colour" : "green"
# }
# print(d1)
# d1.update({"tertiary_colour" : "blue-green"})
# print(d1)


# Write a Python program to sum all the numeric items in a dictionary.
# d1 = {
#     "value_1" : 50,
#     "value_2" : 40,
#     "value_3" : 50,

# }
# print(sum(d1.values()))

# def num_my_dict(dictionary):
#     sum = 0
#     for val in dictionary.values():
#         if isinstance(val,(int,float)):
#             sum += val
#     return sum
# my_dict = {"a":10, "b":"3.14","c":7, "d":89, "e":"not-numeric"}
# sum_my_dict = num_my_dict(my_dict)
# print(f'Sum of Numeric value is',sum_my_dict)

# # Write a program to identify duplicate values from list.
# provinces = ["sindh", "Punjab","Balochistan", "KPK","sindh"]
# dup_provinces = []
# for items in provinces:
#     if items not in dup_provinces:
#       dup_provinces.append(items)
        
#     else:
#        print(items,end="")

# Write a Python script to check if a given key already exists in a dictionary

# d1= {
#  "primary_colour" : "red",
#  "secondary_colour" : "green"
# }
# def is_key_present(x):
#     if x in d1:
#         print('Key is present in the dictionary')
#     else:
#         print('Key is not present in the dictionary')
# key = "primary_colour"
# is_key_present(key)


