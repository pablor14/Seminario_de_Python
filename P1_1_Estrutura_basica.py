
#########################################################################################################################
################################################## Estruturas de Dados ##################################################
#########################################################################################################################
'''

    Listas, Tuplas, Dicionários, Sets

    # Metodos que podem ser usados em listas, tuplas, dicionarios e sets (Considera o primeiro item do iterable):
    
    Sintaxe: metodo(iterable)
        - len() : Retorna o tamanho do iterable , se for uma string, retorna o número de caracteres
        - max() : Retorna o maior valor do iterable, se forem números
        - min() : Retorna o menor valor do iterable, se forem números
        - sum() : Retorna a soma dos valores do iterable, se forem números
        - sorted() : Retorna uma lista ordenada do iterable, baseado no primeiro item
        - reversed() : Retorna uma lista invertida do iterable, baseado no primeiro item
        - enumerate() : Retorna um objeto enumerado do iterable (lista de tupulas), baseado no primeiro item

'''

############# Listas #############
"""
    # Sintaxe: lista = [item1, item2, item3, ...]
    # Descrição: São coleções ordenadas de itens, que podem ser de diferentes tipos.
        - list() : Cria uma lista/Converte um objeto em lista
    # Métodos:
        # Sintaxe : lista.metodo()
        - append() : Adiciona um item no final da lista
        - extend() : Concatena a lista com outra lista
        - clear() : Remove todos os itens da lista
        - copy() : Retorna uma cópia da lista
        - count() : Retorna o número de vezes que um valor aparece na lista
        - index() : Retorna o índice do primeiro item com o valor especificado
        
"""
print('\n')

# Exemplo

lista = [1, 'dois', 3.0, True]   # [1, 'dois', 3.0, True]
print(lista)

lista[0] = 3
print(lista[0])



############# Tuplas #############
"""
    # Sintaxe: tupla = (item1, item2, item3, ...)
    # Descrição: São coleções ordenadas de itens, que podem ser de diferentes tipos. São imutáveis. 
        - unpacking é o desempacotamento de tuplas em variáveis (item1, item2, item3, ... = tupla)
        - tuple() : Cria uma tupla/Converte um objeto em tupla
    # Métodos:
        - count() : Retorna o número de vezes que um valor aparece na tupla
        - index() : Retorna o índice do primeiro item com o valor especificado
        
"""
print('\n')


# Exemplo
tupula = (1, 'dois', 3.0, True)   # (1, 'dois', 3.0, True)
print(tupula)

print(tupula[0])
#tupula[0] = 1;  # ERRO: Imutavel



############# Dicionários #############
"""
    # Sintaxe: dicionario = {chave1: valor1, chave2: valor2, chave3: valor3, ...}
    # Descrição: São coleções não ordenadas de itens, que são acessados por chaves.
        - dict() : Cria um dicionário/Converte um objeto em dicionário (ex: lista de tupulas)
    # Métodos:
        - fromkeys() : Retorna um dicionário com as chaves e valores especificados
        - get() : Valor da chave especificada
        - items() : Lista contendo uma tupla para cada par de chave-valor
        - values() : Lista contendo os valores do dicionário
        - keys() : Lista contendo as chaves do dicionário
        - pop() : Remove o item com a chave especificada

"""
print('\n')
    # Exemplo
dicionario = {'nome': 'Ana', 'idade': 25, 'cidade': 'São Paulo'}   # {'nome': 'Ana', 'idade': 25, 'cidade': 'São Paulo'}
print(dicionario)

dicionario = {1:'a' ,'b':0.3, True: 1}
dicionario['b'] = 0.4
print(dicionario['b'])

dicionario = {'nome': 'Ana', 'idade': 25, 'cidade': 'São Paulo'}   # {'nome': 'Ana', 'idade': 25, 'cidade': 'São Paulo'}

############# Sets #############
"""
    # Sintaxe: conjunto = {item1, item2, item3, ...}
    # Descrição: São coleções não ordenadas de itens, que não possuem itens duplicados.
        - set() : Cria um conjunto/Converte um objeto em conjunto
    
"""
print('\n')
    # Exemplo
conjunto = {1, 2, '3', 4, 5}   # {1, 2, 3, 4, 5}
conjunto = {1, 2, '3', 4, 1}   # {1, 2, 3, 4}     # Não aceita elemento repetidos
conjunto.add('a')
# print(conjunto[0])         # ERRO: Não é acessivel por indices
# conjunto[0] = 2            # ERRO: Não é acessivel por indices
print(conjunto)


#######################################################################################################################
####################################################### Sintaxe #######################################################
#######################################################################################################################

# FOR EACH
for n in conjunto:
    print(n)


# IF, ELSE, ELIF
if(dicionario['idade']> 18):
    print('maior de idade')

elif(dicionario['idade'] < 18):
    print('menor de diade')

else:
    print('18 anos')


# WHILE
while (False):
    print('Hello')
