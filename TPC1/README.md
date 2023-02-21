# PL2023
21/02/2023 - João Gonçalo de Faria Melo (a95085)

Considerações relativas à realização do TPC1:

- O modelo utilizado para guardar a informação presente nas linhas do ficheiro 'myheart.csv' fornecido é uma lista do Objeto 'Person'. Este objeto visa representar a pessoa no contexto em questão, apresentando uma variável de instância para cada um dos campos presentes no cabeçalho do ficheiro .csv.

- Na leitura do ficheiro para o modelo de dados referido em cima são alterados os tipos das variáveis (str) para tipos mais convenientes à manipulação

- Para registar os cálculos das distribuições da doença usei diferentes dicionários.

- Visto que não tenho muita experiência em programação em python, recorri ao ChatGPT para aprender como podia usar corretamente os dicionários para manipular mais facilmente a informação.

- Tomei a decisão de não implementar quase nenhuma validação dos limites dos argumentos devido à fiabilidade do ficheiro após análise. Além disso, a implementação desta funcionalidade será mais fácil e fará mais sentido com recurso a regular expressions.

- Para além da distribuição numérica, calculei também a distribuição percentual.

- Para a representação dos resultados em forma de tabela decidi usar o módulo 'tabulate' apenas com o intuito de melhorar a estética.

- O fluxo do programa criado está bastante simplificado.

- Bibliografia/Ferramentas para famarialização com o módulo 'matplotlib': https://www.youtube.com/watch?v=D4VlmL3G4_o
