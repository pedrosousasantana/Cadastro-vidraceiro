Glass Management System (CRUD)

Um sistema de gerenciamento de inventário para vidraçarias desenvolvido em **Python**. Este projeto implementa as operações fundamentais de um software de gestão: **C**reate, **R**ead, **U**pdate e **D**elete (CRUD).

Sobre o Projeto
Este script foi desenvolvido para automatizar o controle de estoque de diferentes tipos de vidros (temperado, comum, laminado), permitindo que o usuário tenha um controle preciso sobre preços e especificações técnicas de forma rápida via interface de linha de comando (CLI).

Tecnologias Utilizadas
* **Python 3.x**: Linguagem base para toda a lógica estruturada.
* **Dicionários e Listas**: Para simular um banco de dados em memória.
* **Tratamento de Exceções**: Uso de blocos `try/except` para garantir a estabilidade do software.

Demonstração (Funcionamento)

1. Cadastro e Listagem
Permite o registro dinâmico de novos materiais com atribuição automática de IDs.
![Gif de Cadastro](path/para/seu/gif-cadastro.gif)

2. Atualização e Exclusão
Gerenciamento flexível de dados existentes, com busca por identificador único.
![Gif de Update/Delete](path/para/seu/gif-update-delete.gif)

  Estrutura de Funções
O código está modularizado para facilitar futuras integrações com bancos de dados reais (SQL):
- `criar_vidro()`: Capta entradas do usuário e popula o dicionário.
- `listar_vidros()`: Itera sobre a lista de objetos e formata a saída.
- `atualizar_vidro()`: Localiza o registro por ID e sobrescreve os atributos.
- `deletar_vidro()`: Remove o objeto da lista de dados.


        
