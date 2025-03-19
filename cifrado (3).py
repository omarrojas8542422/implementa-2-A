texto=input("Tu texto: ")
if texto== texto.upper():
    abc="ABCDEFGHIJKLMNOPQRSTVXYZ"
else:
    abc="abcdefghijklmnopqrstuvwxyz"
k=int(input("40"))
cifrad=""
for c in texto:
    if c in abc:
        cifrad+= abc[(abc.index(c)+k)%(len(abc))]
    else:
        cifrad+=c
print("hola mundo", cifrad)
                    
