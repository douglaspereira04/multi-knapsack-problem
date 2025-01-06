import sys

T = list()  # Conjunto de caminhoes
C = list()  # Estrutura para relacionar os caminhoes com sua capacidade

G = list()  # Conjunto de itens
W = list()  # Estrutura para relacionar o peso com os items
V = list()  # Estrutura para relacionar o valor com os items


def w(i):
    return W[i]


def v(i):
    return V[i]


__M: dict = {}


"""
    M representa uma matriz de 2+|T| dimensões
    M[item][caminhao][capacidades possiveis de t1][capacidades possiveis de t2]...[capacidades possiveis de t|T|]
    mas é modelada como uma estrutura de três dimensões do tipo
    M[item][caminhao][possiveis configuração capacidades de todos os caminões em T]
    sendo que cada "possível configuração de capacidade" é expressada por uma
    tupla de |T| elementos
"""

"""
    Função auxiliar para acessar M
    Se "value" está definido então o valor é escrito
"""


def M(i: int, j: int, C_: tuple, value: int = None):
    d1 = __M.get(i, None)
    if d1 is None:
        d1 = {}
        __M[i] = d1
    d2 = d1.get(j, None)
    if d2 is None:
        d2 = {}
        d1[j] = d2

    old_value = d2.get(C_, None)
    if old_value is None:
        d2[C_] = value

    return old_value


def OPT(i: int, j: int, C: tuple, D: tuple):

    result: tuple = None

    if i == -1:
        result = (0, D)
    else:
        memory = M(i, j, C)
        if memory is not None:
            result = memory

        elif j == -1:
            result = OPT(i - 1, len(C) - 1, C, D)

        elif C[j] < w(i):
            result = OPT(i, j - 1, C, D)

        else:
            v1, D1 = OPT(i - 1, len(C) - 1, C[:j] + (C[j] - w(i),) + C[j + 1 :], D)
            v1 += v(i)
            v2, D2 = OPT(i, j - 1, C, D)
            if v1 > v2:
                result = (v1, D1 + (i,))
            else:
                result = (v2, D2)

    M(i, j, C, result)
    return result


with open(sys.argv[1], "r") as file:
    for i, line in enumerate(file):
        if i == 0:
            T = line.strip().split()
        if i == 1:
            c_strs = line.strip().split()
            C = [int(c_str) for c_str in c_strs]
        if i == 2:
            G = line.strip().split()
        if i == 3:
            w_strs = line.strip().split()
            W = [int(w_str) for w_str in w_strs]
        if i == 4:
            v_strs = line.strip().split()
            V = [int(v_str) for v_str in v_strs]


i0 = len(G) - 1
j0 = len(C) - 1
max_value, D = OPT(i0, j0, tuple(C), ())
not_D = [G[item] for item in range(len(G)) if item not in D]

print(f"Maior Valor: {max_value}")
print(f"Não entregues: {', '.join(not_D)}")
