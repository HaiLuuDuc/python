thuongCount = 0
hoaCount = 0
str = input()
for i in str:
    if(i.isupper()):
        hoaCount += 1
    else:
        thuongCount += 1
if(thuongCount >= hoaCount):
    print(str.lower())
else:
    print(str.upper())