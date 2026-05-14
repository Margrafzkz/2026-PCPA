'''
Problema: beecrowd | 1010 
Data: 2026.05.14
Estudante: Matheus Margraf
'''
#objetivo: ler código, quantidade e valor unitário de duas peças e calcular o total a pagar

#--- ANÁLISE (LIAC) ----
# Entrada: duas linhas; cada uma com código (int), quantidade (int) e valor unitário (float)
# Processamento: total = (______*______) * (_______*______)
# Saída: "VALOR A PAGAR: R$ ____" com ____ casas decimais 

cod1, qtd1, val1 = input().split()

qtd1 = int(qtd1)
val1 = float(val1)

cod2, qtd2, val2 = input().split()

qtd2 = int(qtd2)
val2 = float(val2)

total = (qtd1*val1)+(qtd2*val2)

print(f"VALOR A PAGAR: R$ {total:.2f}")