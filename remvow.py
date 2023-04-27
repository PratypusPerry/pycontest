x='abcdeABCDE'
vowels=('a','e','i','o','u','A','E','I','O','U')
for i in x:
    if i in vowels:
        x=x.replace(i,'')
# print(x.lower())
print(x)
