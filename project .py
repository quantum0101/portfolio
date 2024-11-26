# FOR GREETING TO YOU



# import time

# current_hour = int(time.strftime("%H"))
# print("Enter your name:")
# a = input()

# if current_hour >= 6 and current_hour < 12:
#     print(f"Good Morning, {a} sir!")
# elif current_hour >= 12 and current_hour < 18:
#     print(f"Good Afternoon, {a} sir!")
# elif current_hour >= 18 and current_hour < 24:
#     print(f"Good Evening, {a} sir!")
# else:
#     print(f"Good Night, {a} sir!")
























     # asking a question to see if you can drive# 
# print("Enter your age to see if you can drive:")
# b = int(input())

# if b > 100:
#     print("No one can live that long!")
# elif b >= 18:
#    print("You are perfectly able to drive or vote.")
# elif b == 17:
#    print("It's okay, but drive safely.")
# elif b <= 10:
#    print("Go and study, boy.")
# else:
#    print("You are not able to drive or vote.")
#    if b==15:
#       print("wait for 3 years.")
#    if b==16:
#       print("wait for 2 years.")
#    if b==14:
#       print("wait for 4 years.")
#    if b==13:
#       print("wait for 5 years.")
#    if b==12:
#       print("wait for 6 years.")




















# CALCULATER



# print ("* chose the given number for what you want to do")

# print("-multiplication; no 1")
# print("-addation; no 2")
# print("-subtration; no 3")
# print("-divide; no 4")
# c=int(input("enter the number "))
# a=int(input("enter your 1 numebr which you want to do:"))
# b=int(input("enter your 2 numebr which you want to do:"))
# if c==2:
#   print("the value of ",a,"+",b,"is","=",a+b)
# if c==3:
#   print("the value of ",a,"-",b,"is","=",a-b)
# if c==1:
#   print("the value of ",a,"multipl",b,"is","=",a*b)
# if c==4:
#  print("the value of ",a,"divide",b,"is","=",a/b)



























# rock paper scissor
# print("Lets play a game of rock paper and scissor.")
# import random as r
# lis = ["rock","paper","scissor"]
# ai = (r.choice(lis))
# user = input("call your chance:")
# if user != "rock" and "scissor" and "paper":
#     raise SyntaxError
# print(f"ai choosed {ai} and you choosed {user} so,")
# if ai == user:
#     print("draw")
# if ai == "rock" and user == "paper":
#     print("you win") 
# if ai == "rock" and user == "scissor":
#     print("you lose") 
# if ai == "scissor" and user == "paper":
#     print("you lose") 
# if ai == "scissor" and user == "rock":
#     print("you win") 
# if ai == "paper" and user == "rock":
#     print("you lose") 
# if ai == "paper" and user == "scissor":
#     print("you win") 

















# liberary



# class liberary:
#     def __init__(self):
#         self.n = 0
#         self.book = []

#     def check_book_no(self):
#         if self.n == len(self.book):
#             print("The no of books are equal to books present in liberary.")
#         else:
#             print("The no of books are not equal to books present in liberary.")
   

#     def total_books(self):
#         print(f"Total no of books are: {self.n}")
    
#     def display_books(self):
#         print("Books in this liberary are:")
#         for i in self.book:
#           print(f"- {i}")


#     def add_book(self,books):
#         self.book.append(books)
#         self.n += 1
        


# liberary1 = liberary()
# liberary1.add_book("crime and punishment")
# liberary1.add_book("48 laws of power")
# liberary1.add_book("rich dad poor dad")
# liberary1.display_books()
# liberary1.check_book_no()
# liberary1.total_books()