

nome = input("Insira seu nome: ").strip

nome = nome.upper()

if nome.find("SILVA") != -1:
    print("Olá Silva")
else:
    print("Olá Usuário")
