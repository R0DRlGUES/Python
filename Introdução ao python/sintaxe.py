#Declaração de Variáveis

nome = "Alice"  # String
idade = 25  # Inteiro
altura = 1.75  # Float
ativo = True  # Booleano

#Estruturas Condicionais
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

#Laços de Repetição
    # for
    for i in range(5):  # Loop de 0 a 4
        print(i)

    #while
    contador = 0
    while contador < 5:
        print(contador)
        contador += 1

#Declaração de Funções
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Alice"))

#Métodos em Classes
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        return f"Meu nome é {self.nome} e tenho {self.idade} anos."

pessoa1 = Pessoa("Alice", 25)
print(pessoa1.apresentar())


#Entrada e Saída de Dados
nome = input("Digite seu nome: ")  # Entrada de usuário (sempre retorna string)
print(f"Olá, {nome}!")  # Saída formatada

#Estruturas de Dados

    #Listas (Mutáveis)
    numeros = [1, 2, 3, 4, 5]
    numeros.append(6)  # Adiciona um elemento
    print(numeros[0])  # Acessa o primeiro elemento

    #Tuplas (Imutáveis)
    coordenadas = (10, 20)
print(coordenadas[0])  # Acessa o primeiro valor

#Tratamento de Erros (Try/Except)
try:
    num = int(input("Digite um número: "))
    print(10 / num)
except ValueError:
    print("Por favor, digite um número válido!")
except ZeroDivisionError:
    print("Não é possível dividir por zero!")
