'''
Problema: beecrowd | 1052
Data: 2026.05.07
Estudante: Matheus Margraf
'''

# Objetivo: Ler um numero de 1 a 12 e informar qual mes ele pertence

# --- ANÁLISE (LIAC) ---
# Entrada: o numero
# Processamento: comparar o numero com cada mes na tabela usando if/elif/else
# Saída: nome do mes correspondente, ou "mes nao cadastrado" se não encontrado
N = int(input())

if N == 1:
    print("January")
elif N == 2: 
    print("February")
elif N == 3: 
    print("March")
elif N == 4: 
    print("April")
elif N == 5: 
    print("May")  
elif N == 6: 
    print("June")
elif N == 7: 
    print("July")
elif N == 8: 
    print("August")
elif N == 9:
    print("September")
elif N == 10:
    print("October")
elif N == 11:    
    print("November")
elif N == 12:
    print("December")
