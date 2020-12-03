#!/usr/bin/env python3

# Hardcoded

possible_codes = 0

for i in range(130254,678275):
    a=int((i%1000000)/100000)
    b=int((i%100000)/10000)
    c=int((i%10000)/1000)
    d=int((i%1000)/100)
    e=int((i%100)/10)
    f=int((i%10)/1)

    if (
        ( a<=b and b<=c and c<=d and d<=e and e<=f ) and 
        (a==b or b==c or c==d or d==e or e==f)
    ):
        possible_codes+=1
    

print(possible_codes)



