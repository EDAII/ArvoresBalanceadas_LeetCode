Arv-questoesLeetCode

## Alunos  
| Matrícula | Nome |  
|-----------|------|  
| 200035703 | Breno Alexandre Soares Garcia |  
| 211062900 | Caio Lucas Lelis Borges |  

## Descrição do projeto
Para essa entrega nossa dupla optou pela prática de questões envolvendo árvores balanceadas no LeetCode.


## Sobre as questões

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


### Questão 710(Caio Lelis) - Random Pick with Blacklist

O que a questão pede:
Dado um inteiro n e uma lista de números blacklist, o objetivo é criar um algoritmo que escolha aleatoriamente um número no intervalo [0, n-1] que não esteja na blacklist.
Todos os números válidos devem ter a mesma probabilidade de serem escolhidos. Além disso, a solução deve minimizar chamadas à função de randomização da linguagem.

Como resolvi:
A solução cria uma lista de números válidos (todos os números de 0 a n-1 que não estão na blacklist).

Na inicialização, percorremos o intervalo [0, n-1] e armazenamos apenas os números que não estão na blacklist.

Para cada chamada de pick(), escolhemos aleatoriamente um índice dessa lista de números válidos.
Essa abordagem garante que todos os números permitidos tenham probabilidade uniforme e que a função random seja chamada uma vez por pick, de forma eficiente.

## Conclusões
A prátiva das questões nos ajudou bastante a fixar os conceitos de árvores balanceadas, além de nos proporcionar o contato com diferentes tipos de problemas que podem ser resolvidos com essas estruturas de dados.

## Referências

Caso tenha utilizado algum agoritmo como base, citar o mesmo devidamente para  evitar quaisquer denuncias de plágio.
