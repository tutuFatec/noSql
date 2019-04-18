# -*- coding: utf-8 -*-

import redis

global conecao

conecao = redis.Redis (
    host='localhost',
    port=6379,
    db=0
)

'''
    nome da Key = carrrinho
    sadd e como se um conjunto 
        ver como usar como inserir o no sadd 
        ver como usar deletar do sadd 
'''

key = "carrinho"

print(key)

def inserir():
    print('teste')

def ler(key):
    return conecao.smembers(key)

def alterar(key, editar, editado):
    print(conecao.srem(key, editar))
    conecao.sadd(key, editado)

def excluir():
    print('teste')

while True:
    print('Escolha uma opção: \n')
    print('1- Inserir um Produto')
    print('2- Listar os Produtos')
    print('3- Alterar um Produto')
    print('4- Deletar um Produto')

    opcao = input()
    print('\n')

    if (opcao == 1):
        inserir()
    elif (opcao == 2):
        print(ler(key))
        print('\n')
    elif (opcao == 3):
        editar = raw_input('Qual produto voce deseja alterar?')
        editado = raw_input('Qual produto deseja adicionar?')
        print("Deu certo ", alterar(key, editar, editado))
    elif (opcao == 4):
        excluir()

conecao.set('foo', 'bar')
value = conecao.get('foo')
print(value)