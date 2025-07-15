lista=[]
if len(lista)==0:
    resp=True
    while resp:
        lista.apppend(input("Dame una palabra: ").upper())
        resp=input("Deseas solicitar otra frase (si/no)").lower().strip()
        if resp=="no":
            resp=False
    print(lista)


