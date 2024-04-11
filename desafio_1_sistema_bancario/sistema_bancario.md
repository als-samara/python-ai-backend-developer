# Desafio

Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque, extrato.

Depósito: deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trbalha apenas com 1 usuário, dessa forma, não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armezenados em uma variável e exibidos na operação de extrato.

Saque: o sistema deve permitir realizar 3 saques diários com limite máximo de 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

Extrato: essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx


## Implementação

Além das funcionalidades pedidas no desafio, utilizei a biblioteca time para salvar a data de cada operação no extrato e checar o limite diário de saques a cada nova tentativa.

## Tratamento de exceção

Utilizei a exceção ValueError para tratar o cenário de um input incorreto no Menu Principal.
