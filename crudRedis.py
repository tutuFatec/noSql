import redis

conecao = redis.Redis (
    host='localhost',
    port=6379,
    db=0
)

'''
    nome da Key = carrrinho
    sadd é como se um conjunto 
        ver como usar como inserir o no sadd 
        ver como usar deletar do sadd 
'''


def inserir():
    print('teste')

def ler():
    print('teste')

def alterar():
    print('teste')

def excluir():
    print('teste')

while True:
    print('Escolha uma opção: \n')
    print('1- Inserir um Produto')
    print('2- Listar os Produtos')
    print('3- Alterar um Produto')
    print('4- Deletar um Produto')

    opcao = input()

    if (opcao == 1):
        inserir()
    elif (opcao == 2):
        ler()
    elif (opcao == 3):
        alterar()
    elif (opcao == 4):
        excluir()

conecao.set('foo', 'bar')
value = conecao.get('foo')
print(value)