# Problema da Mochila Estendido

Os programas implementados resolvem o problema da mochila extendido para
mais de uma mochila, encontrando o valor máximo. As "mochilas" são
denominadas "caminhões".

O arquivo da implementação se encontra em `trucks.py` a partir do
diretório raiz (Obs: deixei um arquivo `trucks_clean.py` que resolve
somente o valor máximo, sendo de mais fácil leitura e comparação com a
função *OPT* discutida na seção **Desenvolvimento**). A versão
`trucks_detailed.py` apresenta detalhadamente a distribuição de itens
nos caminhões.

Os aquivos de entrada seguem os seguinte formato:

1.  Conjunto *T*. Nomes dos caminhões separados por espaço;

2.  Conjunto *C*. Capacidades dos caminhões separadas por espaço;

3.  Conjunto *G*. Nomes dos items separados por espaço;

4.  Conjunto *W*. Pesos dos items separados por espaço, sendo
    equivalente a função *w*;

5.  Conjunto *V*. Valores dos items separados por espaço, sendo
    equivalente a função *v*.

Existem dois arquivos de instância do problema, *teste1.txt* e
*teste2.txt*. Para testar o programa, execute no terminal
`python3 trucks.py teste2.txt` no diretório raiz.
