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
   while True :
    direcao = str(input('Digite a direção do robo para CIMA,BAIXO,ESQUERDA E DIREITA, e junto o número de passos(aperte enter para ver o resultado final)\nExemplo:\nDIREITA 5\nDigite as direções: '))
    for palavra in direcao:
        ako = direcao.split()
        cb = []
        ed = []
        if "CIMA" in ako or "BAIXO" in ako:
            cb.append(ako)
            for pato in cb:
                if "CIMA" in cb:
                    j = float(cb[0][1])
                    x = round(j)
                if "BAIXO" in cb:
                    t = float(cb[0][1])
                    y = round(t)
        if "ESQUERDA" in direcao or "DIRETA" in direcao:
            ed.append(ako)
            for peixe in ed:
                if "ESQUERDA" in ed:
                    b = float(ed[0][1])
                    d = round(b)
                if "DIRETA" in ed:
                    p = float(ed[0][1])
                    f = round(p)
    if direcao == "":
        n = x - y
        m = y - x
        h = d - f
        k = f - d
        if n > h or n > k or m > h or m > k:
            if m > n:
                print(m)
            if n > m:
                print(n)
        if h > n or h > m or k > n or k > m:
            if h > k:
                print(h)
            if k > h:
                print(k)
        break

    
if __name__ == '__main__':
    main()
