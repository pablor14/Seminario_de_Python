
#######################################################################################################################
################################################# Topicos "Avançados" #################################################
#######################################################################################################################

'''
    Lambda Expressions, List Comprehensions, 
'''
############ Lambda Expressions #############
"""
    # Sintaxe: minha_funcao = lambda parametro(s): expressão 
    # Descrição: São funções anônimas, ou seja, não possuem nome.

"""
print('\n')

# Exemplo
soma = lambda x, y: x + y
print(soma(3,2))    # 5

############ List Comprehension #############
"""
    # Sintaxe:  [expressão for item in iterável]
                [expressão for item in iterável if condição]
                [expressão if condição else expressão for item in iterável]
    # Descrição: É uma forma concisa de criar listas em Python.
"""
print('\n')

# Exemplo
quadrados = [x ** 2 for x in range(5)]                              # [0, 1, 4, 9, 16]
quadrados = [x ** 2 for x in range(5) if  (x % 2) == 0]             # [0, 4, 16]
quadrados = [x ** 2 if ((x % 2) == 0) else 0 for x in range(5)]     # [0, 0, 4, 0, 16]
