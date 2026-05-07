'''
Problema: beecrowd | 1050
Data: 2026.05.07
Estudante: Matheus Margraf
'''

# Objetivo: Ler um codigo DDD e informar qual cidade ele pertence

# --- ANÁLISE (LIAC) ---
# Entrada: o DDD
# Processamento: comparar o DDD com cada codigo na tabela usando if/elif/else
# Saída: nome da cidade correspondente, ou "DDD nao cadastrado" se não encontrado
DDD = int(input())

if DDD == 61:
    print("Brasília")
elif DDD == 71: 
    print("Salvador")
elif DDD == 11: 
    print("Sao Paulo")
elif DDD == 21: 
    print("Rio de Janeiro")
elif DDD == 32: 
    print("Juiz de Fora")  
elif DDD == 19: 
    print("Campinas")
elif DDD == 27: 
    print("Vitoria")
elif DDD == 31: 
    print("Belo Horizonte")
else:                 
    print("DDD nao cadastrado")