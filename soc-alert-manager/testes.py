# 1. Funções

def par(n):
    if n % 2 == 0:
        return True
    else:
        return False


# print(par(57))

def estatisticas(valores):
    minimo = min(valores)
    maximo = max(valores)
    media = sum(valores)/2
    return [minimo, maximo, media]

# print(estatisticas([7,4,9]))

def adiciona(item, destino=[]):
    destino.append(item)
    return destino

# print(adiciona(1))
# print(adiciona(2))
# print(adiciona(3))

# 2. Condicionais

def tipo_triangulo(a, b, c):
    if (a <= 0 or b <= 0 or c <= 0) or (a+b < c) or (a+c < b) or (b+c < a):
        return "inválido"
    elif a != b and a != c and b != c:
        return "escaleno"
    elif a == b and a != c or a == c and a != b or b == c and b != a:
        return "isósceles"
    return "equi"

# print(tipo_triangulo(10,10,10))

def bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 4 == 0 and ano % 100 != 0 and ano % 400 == 0): 
        return "É"
    else:
        return "Não é"

# print(bissexto(2012))

# print(0 or "a", [] and 1, not "")

# 3. Laços

def mult_tres_cinco():
    soma_tres = 0
    soma_cinco = 0

    for i in range (3, 1001):
        if i % 3 == 0:
            soma_tres = soma_tres + i

        if i % 5 == 0:
            soma_cinco = soma_cinco + i

    return soma_cinco, soma_tres

# print (mult_tres_cinco())

def passos_collatz(n):
    contador = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1

        contador += 1

    return contador

# print(passos_collatz(4))

# Um numero primo é quando ele so é divisivel por 1 e ele mesmo

def primos_ate(n):

    contador = 2
    lista_primos = []

    if n < 2:
        return []

    while contador <= n: 

        for i in range (1,n+1):
            if contador == i:
                pass
            elif contador % i == 0:
                lista_primos.append(contador) 

        contador += 1

        lista = [n for n in lista_primos if lista_primos.count(n) == 1] # remover os itens que repetem
                
    return lista


# print(primos_ate(100))

# 4. Listas

def sem_duplicatas(lista):
    return set(lista)

# print(sem_duplicatas([2,2,2,3,5,6,6,7]))

def rotaciona(lista, k):

    final = lista[-k:]
    inicio = lista[:-k]

    resultado = final + inicio

    return resultado

# print(rotaciona([1,2,3,4,5], 2))

# 5. Dicionários

# estoque = {"parafuso": 100, "porca": 50}
# estoque["arruela"] = 30
# estoque["porca"] += 10

# for item, qtd in estoque.items():
#     print(f"{item}: {qtd}")

# contagem = {}
# for letra in "banana":
#     contagem[letra] = contagem.get(letra, 0) + 1
# {'b': 1, 'a': 3, 'n': 2}

def frequencia_palavras(texto):

    contagem = {}

    for letra in texto:
        contagem[letra] = contagem.get(letra, 0) + 1

    return contagem

print(frequencia_palavras("teste"))