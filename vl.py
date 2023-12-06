li=["hello","there"]
vowels='aeiou'
li2=[x for x in li for x in x if x in vowels]
a=print("no of vowels :",len(li2))
for i in li:
    b=len(i)
    print('Length of ',i,'is',b)
    if(b>=10):
        print(i,'word is',b)
