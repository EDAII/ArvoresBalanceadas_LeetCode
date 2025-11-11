# ArvoresBalanceadas_LeetCode

## Alunos  
| Matrícula | Nome |  
|-----------|------|  
| 200035703 | Breno Alexandre Soares Garcia |  
| 211062900 | Caio Lucas Lelis Borges |  

## Descrição do projeto
Para essa entrega nossa dupla optou pela prática de questões envolvendo árvores balanceadas no LeetCode.


## Sobre as questões

### Questão 98(Breno Alexandre) - Validate Binary Search Tree
O que a questão pede:
Dado o nó raiz de uma árvore binária, o objetivo é verificar se ela é uma árvore de busca binária (BST) válida.
Uma árvore de busca binária é válida se, para cada nó:
Todos os valores da subárvore esquerda forem menores que o valor do nó atual.
Todos os valores da subárvore direita forem maiores que o valor do nó atual.
E ambas as subárvores também forem BSTs válidas.

Como resolvi:
A solução utiliza recursão com limites (mínimo e máximo) para validar cada nó.
1. Criamos uma função auxiliar (helper(node, lower, upper)) que recebe:
- O nó atual.
- O limite inferior (lower) — o menor valor permitido.
- O limite superior (upper) — o maior valor permitido.

2. Para cada nó:
- Se o nó for nulo (None), ele é válido (caso base).
- Verificamos se o valor do nó está dentro dos limites (lower < val < upper).
- Chamamos recursivamente a função para:
  - A subárvore esquerda, atualizando o limite superior (upper = val).
  - A subárvore direita, atualizando o limite inferior (lower = val).

3. Se todas as verificações passarem, a árvore é uma BST válida.

Essa abordagem garante que cada nó obedece às regras de uma BST, propagando os limites adequados para cada nível da árvore.

### Questão 124(Breno Alexandre) - Binary Tree Maximum Path Sum
O que a questão pede:
Dado o nó raiz de uma árvore binária, o objetivo é encontrar o maior somatório possível de um caminho na árvore.
Aqui, um “caminho” é uma sequência de nós conectados por arestas — ele pode começar e terminar em qualquer nó, não necessariamente na raiz, e deve percorrer nós adjacentes (pai-filho).

Como resolvi:
A resolução usa uma abordagem por DFS (recursiva), onde em cada nó calculo dois valores importantes:
O valor máximo de um “caminho ascendente” que tenho que retornar ao pai (isto é: melhor caminho descendo da esquerda ou da direita mais o valor do nó)
O valor global máximo de caminho que pode passar pelo nó (isto pode incluir tanto o ramo esquerdo quanto o direito + o valor do nó)

Passos principais:
1. Defino uma variável global ou externa (max_sum) iniciada com valor muito baixo (por exemplo -inf), para acompanhar o maior somatório encontrado até agora.

2. Escrevo uma função dfs(node) que retorna o valor máximo de caminho “para cima” (ao pai):
- Se node for None, retorno 0.
- Chamo recursivamente para left = dfs(node.left) e right = dfs(node.right).
- Para garantir que não “afundamos” com valores negativos desnecessariamente, faço left = max(0, left) e right = max(0, right) (ou alternativamente considerar nodos negativos de forma apropriada).
- Então, calculo current_path_sum = left + right + node.val — este representa o caminho que passa pelo nó, usando ambos ramos.
- Atualizo max_sum = max(max_sum, current_path_sum).
- E retorno para o pai node.val + max(left, right) — isto representa a melhor escolha se o caminho continuar ascendendo do nó pelo melhor ramo.

3. Após a chamada dfs(root), o valor max_sum guarda o resultado da questão.

Essa abordagem garante que todos os possíveis caminhos “começando/terminando em qualquer nó” são considerados (porque em cada nó consideramos o caminho que passa por ele) e também propagamos para cima a melhor forma de continuar caminho.

### Questão 710(Caio Lelis) - Random Pick with Blacklist
O que a questão pede:
Dado um inteiro n e uma lista de números blacklist, o objetivo é criar um algoritmo que escolha aleatoriamente um número no intervalo [0, n-1] que não esteja na blacklist.
Todos os números válidos devem ter a mesma probabilidade de serem escolhidos. Além disso, a solução deve minimizar chamadas à função de randomização da linguagem.

Como resolvi:
A solução cria uma lista de números válidos (todos os números de 0 a n-1 que não estão na blacklist).

Na inicialização, percorremos o intervalo [0, n-1] e armazenamos apenas os números que não estão na blacklist.

Para cada chamada de pick(), escolhemos aleatoriamente um índice dessa lista de números válidos.
Essa abordagem garante que todos os números permitidos tenham probabilidade uniforme e que a função random seja chamada uma vez por pick, de forma eficiente.

### Questão 3542(Caio Lelis) - Minimum Operations to Convert All Elements to Zero
O que a questão pede:
Dado um array de números inteiros não-negativos, precisamos zerar todos os elementos usando o mínimo número de operações possível.
Em cada operação, é permitido escolher um subarray e zerar todas as ocorrências do mínimo valor não-negativo desse subarray.

Como resolvi:
A solução utiliza uma abordagem recursiva baseada em segmentos:

Para cada subarray, encontra-se o mínimo valor e aplica-se a operação para zerá-lo.

O array é então dividido em subsegmentos de valores maiores que o mínimo, que são processados recursivamente.

Em cada etapa, o algoritmo escolhe o mínimo entre:

Zerando cada elemento individualmente (pior caso)

Zerando pelo mínimo e processando os segmentos recursivamente

## Conclusões
A prátiva das questões nos ajudou bastante a fixar os conceitos de árvores balanceadas, além de nos proporcionar o contato com diferentes tipos de problemas que podem ser resolvidos com essas estruturas de dados.

## Referências
Caso tenha utilizado algum agoritmo como base, citar o mesmo devidamente para  evitar quaisquer denuncias de plágio.
