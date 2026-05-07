'''
Problema: beecrowd | 1020
Data: 2026.05.07
Estudante: Matheus Margraf
'''
# Objetivo: 

# --- ANÁLISE (LIAC) ---
# Entrada: um número inteiro N representando segundos totais
# Processamento: extrair horas, minutos e segundos restantes por divisão inteira e módulo
# Saída: no formato h:m:s (sem zeros à esquerda - 0:9:16, não 00:09:16)

#int(input()) duração sempre é um número inteiro de segundos
N = int(input())

# // divisão inteira: retorna quantas vezes o divisor cabe no dividendo
# % - modulo: retorna apenas o resto da divisão

a = N // 365
N = N % 365
m = N // 30
d = N % 30

print(f'{a} ano(s)')
print(f"{m} mes(es)")
print(f'{d} dia(s)')