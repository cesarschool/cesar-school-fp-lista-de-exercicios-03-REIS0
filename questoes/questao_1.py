## QUESTÃO 1 ##
#
# Um site exige que os usuários insiram nome de usuário e senha para se registrarem. 
# Escreva um programa para verificar se a senha digitada pelos usuários é forte o suficiente.
# A seguir estão os critérios para verificar a senha:
#
# 1. Pelo menos uma letra entre [a-z]
# 2. Pelo menos 1 número entre [0-9]
# 3. Pelo menos uma letra entre [A-Z]
# 4. Pelo menos 1 caractere de [$ # @]
# 5. Comprimento mínimo da senha: 6
# 6. Comprimento máximo da senha: 12
#
# Seu programa deve aceitar uma sequência de senhas separadas por vírgula e as verificará 
# de acordo com os critérios acima. As senhas que correspondem aos critérios devem ser 
# impressas, separadas por uma vírgula.
# Exemplo
# Se as seguintes senhas forem fornecidas como entrada para o programa:
# ABd1234 @ 1, um F1 #, 2w3E *, 2We3345
# Então, a saída do programa deve ser:
# ABd1234 @ 1
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    usuario = str(input("Digite um nome de usuário: "))
    logado = 0
    isalpha = 0
    isnumeric = 0
    isupper = 0
    desisto = 0
    while logado == 0:
        senha = str(input("1. Pelo menos uma letra entre [a-z]\n2. Pelo menos 1 número entre [0-9]\n3. Pelo menos uma letra entre [A-Z]\n4. Pelo menos 1 caractere de [$ # @]\n5. Comprimento mínimo da senha: 6\n6. Comprimento máximo da senha: 12\nDigite uma senha: "))
        if senha.isalnum() == True:
            for char in senha:
                if char.isalpha() == True:
                    isalpha = 1
                    pass
                if char.isnumeric() == True:
                    isnumeric = 1
                    pass
                if char.isupper() == True:
                    isupper = 1
                    pass
            if isalpha == 1 and isnumeric == 1 and isupper == 1:
                logado = 1
                desisto = 1
                print('senha válida\nsua senha é:',senha)
                break
            elif desisto == 0:
                print('senha inválida')
    


if __name__ == '__main__':
    main()
