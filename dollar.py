word=input("Enter a word :")
if word:
    first_char=word[0]
    modified=first_char+word[1:].replace(first_char,'$')
    print("Modified string :",modified)
else:
    print("no repitition of word")
