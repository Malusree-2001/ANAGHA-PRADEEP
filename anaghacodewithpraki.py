#write a program to print a list of strings in the predefined order , with the following modification
i=eval(input())
t=[]#number
s=[]#strings
for x in range(0,i):
    t.append(input())#input no 
for x in range(0,i):
    s.append(input())#input strings
for x in range(0,i):
    if ((t[x]==len(s[x]))and(t[x]!=x+1)):#string length equalto position and printedposition not to position
        s[x]=s[x].upper()#string to uppercase
    else:
        s[x]=s[x].lower()#string to lowercase
    s=sorted(s,reverse=true)
for x in s:
    print(x)#printing output in required location with required changes
