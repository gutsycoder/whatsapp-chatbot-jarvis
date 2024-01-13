n=input("Enter the value of n ")
s="1"
c=1
s2=""
print(s)
for i in range(1,int(n)):
    for j in range(0,len(s)):
        if(j+1<len(s) and s[j]==s[j+1]):
            c=c+1
        else:
            s2=s2+str(c)+s[j]
            c=1
    print(s2)
    s=s2
    s2=""
