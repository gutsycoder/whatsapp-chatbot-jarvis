import enchant
d = enchant.Dict("en_US")
s=input("Enter the string ")
if(d.check(s)):
    print(s)
store=s
s1=""
def permute(s1,s):
    if(s==""):
        if(d.check(s1)):
            print(s1)
        return
    for i in range(0,len(s)):
        if(s.index(s[i])==i):
            permute(s1+s[i],s[0:i]+s[i+1:])
permute(s1,s)
