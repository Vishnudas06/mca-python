current=2023
final=int(input('Enter the year :'))
if current<final:
    print("List of leap years from " +str(current)+ "and" +str(final)+":")

    while current<final:
        if current%4==0 and current%100!=0:
            print(current)
        if current%100==0 and current%400==0:
            print(current)
            current+=1
if currenr>=final:
    print("Do re-check")
                
