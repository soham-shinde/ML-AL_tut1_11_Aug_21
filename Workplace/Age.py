print("Enter the 3 ages Of People ")
a=[]
for i in range(3):
    a.append(int(input()))
if a[0]>=a[1]:
    if a[0]>=a[2]:
        print(" the largest age is "+str(a[0]))
    else:
        print(" the largest age is "+str(a[2]))
else:
    if a[1]>=a[2]:
        print(" the largest age is "+str(a[1]))
    else:
        print(" the largest age is "+str(a[2]))
