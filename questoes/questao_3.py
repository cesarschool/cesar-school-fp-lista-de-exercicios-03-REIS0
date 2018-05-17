## QUESTÃO 3 ##
#
# Um robô se move em um plano a partir do ponto original (0,0). O robô pode se 
# mover nas direções CIMA, BAIXO, ESQUERDA e DIREITA de acordo com um 
# passo fornecido. O traço do movimento do robô é mostrado da seguinte forma:
#
# CIMA 5
# BAIXO 3
# ESQUERDA 3
# DIREITA 2
#
# Os números após a direção são passos. 
# Escreva um programa para calcular a distância entre a posição atual e o 
# ponto original após uma seqüência de movimentos. Se a distância for um 
# float, basta imprimir o inteiro mais próximo.
# Exemplo:
# Se as seguintes tuplas são dadas como entrada para o programa:
# 
# CIMA 5
# BAIXO 3
# ESQUERDA 3
# DIREITA 2
#
# Então, a saída do programa deve ser:
# 2
# 
# Dicas:
# As entradas devem ser lidas do console até que um valor vazio seja digitado. 
# A saída deve ser um inteiro que representa a distancia para o ponto original. 
# Entradas inválidas devem ser descartadas da contagem.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    x = 0
    y = 0
    while True:
        print('CIMA 5\nBAIXO 4\nESQUERDA 3\nDIREITA 2\nNão digite e aperte enter para ver a posição final\nPosição inicial(x,y): (0,0)')
        direcao = str(input('Digite a direção: '))
        if direcao == "":
            print('a posição final é: (',x,',',y,')')
            break
        direcaoo = float(direcao)
        direcaoo = int(round(direcaoo))
        if direcaoo == 5:
            y = y + 1
            print('(',x,',',y,')')
        if direcaoo == 4:
            y = y - 1
            print('(',x,',',y,')')
        if direcaoo == 3:
            x = x - 1
            print('(',x,',',y,')')
        if direcaoo == 2:
            x = x + 1
            print('(',x,',',y,')')



    
if __name__ == '__main__':
    main()
