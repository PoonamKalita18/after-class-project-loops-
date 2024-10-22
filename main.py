num = 1
num = int(input("enter a number :"))
while (num>0):
    d = num%10
    sum= sum+ d*d*d
    num = num/10
if num==sum:
    print(num , "is a armstrong number")
else:
    print(num,"is not a armstrong number")