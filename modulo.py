#Tipos de dados
variavel = 'casa' #string
numeroString = '2' #string
# Todas string é caracterizada pelas aspas
n1 = 5 #int
f1 = 1.5 #float
b1 = True #bool

# declara a função (define)
def NomeFuncao():
    print("Oi, eu sou uma função!")

#NomeFuncao() #chamada da função

def OutraFuncao():
    print("oi sou outra função!")

def ImprimeNome(nome):
    # nome é o parâmetro da função
    #um parâmetro marca as posições de um determinado valor!
    print("Meu nome é " + nome) #concatenação

# ImprimeNome("Renata") # "Renata" é um argumento da função
# O argumento da função é posicionado nos parâmetros da definição da função

"""def ImprimeIdade(idade):
    print(idade)  """  

def ImprimeIdade(idade):
    print("Minha idade é " + str(idade) ) 

def ImprimeDocumento(documento):
    print(" Meu documento é " + str(documento))

def ImprimeLetra(letra):
    print("Minha letra preferida é " + letra)

def ImprimeDataNiver(data):
    print(" Meu aniversário é " + (data))



