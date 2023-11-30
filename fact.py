def fact(x)
if x==1:return 1
else:return(x*fact(x-1))
num=int(input("Enter a number :")
if num>=1:
        print("Fcatorial of",num,fact(num))
