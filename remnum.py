x='AbcdEf>2,Ghj7,^6'
print(x)
for i in x:
    if i.isdigit():
        x=x.replace(i,'')
print(x)