dct1={}
x=int(input('Enter the number of students :'))
for i in range(0,x):
    it1=[]
    key=input("Enter the rollno :")
    val1=input("Enter student name :")
    val2=input("Enter age :")
    it1.append(val1)
    it1.append(val2)
    dct1[key]=it1
print(dct1)
