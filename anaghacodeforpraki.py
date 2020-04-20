#write a program to print a list of strings in the predefined order , with the following modification
le=eval(input())
t=[]#number
s=[]#strings
for x in range(0,i):
    y=eval(input ("no "+str(x+1)+":")) 
    t.append(y)#input no 
for x in range(0,i):
    z=input("string "+str(x+1)+":")
    s.append(z)#input strings
for x in range(0,i):
    if ((t[x]==len(s[x])) and (t[x]!=x+1)):#string length equalto position 
        s[x]=s[x].upper()#string to uppercase
    else:
        s[x]=s[x].lower()#string to lowercase
        
s=sorted(s,reverse=true)
for x in s:
    print(x)#printing output in required location with required changes
