def validarSenha(s):
    if len(s) < 8:
        return 'Senha inválida, Muito curta'

    temNumero = False
    temMaiuscula = False
    
    for c in s:
        if c == ' ':
            return 'Senha Inválida, não pode ter espaços'
        if c >= '0' and c<= "9":
            temNumero = True
        if c>= 'A' and c <= "Z":
            temMaiuscula = True
    if temNumero == False:
        return "Senha Inválida, precisa de um num. Pelo menos"
    if not temMaiuscula:
        return 'Senha inválida, precisa de uma letra maiuscula'
    
    return 'Senha Válida'
       
#main
senha = input('Digite a Senha: ')
r = validarSenha(senha)
print(r)
