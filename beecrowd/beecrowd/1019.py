'''
Problema: beecrowd | 1019
Data: 2026.05.07
Estudante: Matheus Margraf
'''
# Objetivo: Ler nome, salário fixo e total de vendas; calcular e exibir o total a receber

# --- ANÁLISE (LIAC) ---
# Entrada: um número inteiro N representando segundos totais
# Processamento: extrair horas, minutos e segundos restantes por divisão inteira e módulo
# Saída: no formato h:m:s (sem zeros à esquerda - 0:9:16, não 00:09:16)

#int(input()) duração sempre é um número inteiro de segundos
N = int(input())

# // divisão inteira: retorna quantas vezes o divisor cabe no dividendo
# % - modulo: retorna apenas o resto da divisão

h = N // 3600
N = N % 3600
m = N // 60
s = N % 60 

print(f'{h}:{m}:{s}')