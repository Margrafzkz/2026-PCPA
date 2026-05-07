'''
Problema: beecrowd | 1006
Data: 2026.04.09
Estudante: Matheus Margraf
'''
# Obejtivo: Ler duas notas com pesos diferentes e calcular a média ponderada

# --- ANÁLISE (LIAC) ---
# Entrada: duas notas de ponto flutuante A e B (cada uma em uma linha)
# Processamento: média ponderada = (A * 3.5 + B * 7.5) / 11
# Saída: exibir no formato exato "MEDIA = valor" com 5 casas decimais

# float(input()) - notas podem ter casas decimais (ex: 5.0, 7.1)
A = float(input())
B = float(input())
C = float(input())

# Nota A tem pesos 3.5 e nota B tem peso 7.5
# A soma dos pesos é 11 - divide-se por 11 para obter a média ponderada 
media = (A * 2.0 + B * 3.0 + C * 5.0 ) / 10

# :.5f dentro da f-string - formata o número com exatamente 5 casas decimais 
# O enunciado exige espaço antes e depois do = - seguir à risca
print(f"MEDIA = {media:.1f}")