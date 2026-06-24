# if elif else ladder:

a = int(input("enter your age: "))
if (a >= 18):
    print("You are eligible to vote.")
    print("you are eligible to drive.")
elif (a<0 or a > 120):
    print("it is not a valid age.")
    print("tora mayi ke chodo kehu ke age negative me na hokhela samjhlee!!!")
else:
    print("You are not eligible to vote.")
    print("you are not eligible to drive.")
print("Thank you for checking your eligibility.")