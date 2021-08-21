a = input("enter a character ")
vo= ["a","e","i","o","u"]
f=False
for i in vo:
    if a == i :
        print("vowel")
        f=True
        break
if not f :
    print("Consonant")