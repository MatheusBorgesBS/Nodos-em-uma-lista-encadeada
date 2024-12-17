Lista Encadeada em Python 🚀
📄 Descrição
Este projeto implementa uma estrutura de dados de lista encadeada em Python, utilizando as classes Lista e Nodo. A classe Lista fornece diversas operações comuns para manipulação de listas, como adicionar, remover, inserir e buscar elementos.

A classe Nodo representa os nós individuais da lista, armazenando valores e referências ao próximo elemento (nó) da sequência.

🚧 Funcionalidades
Adicionar Elementos:

add(item) → Adiciona um elemento no início da lista.
append(item) → Adiciona um elemento no final da lista.
insert(item, position) → Insere um elemento em uma posição específica.
Remover Elementos:

rem() → Remove o primeiro elemento da lista.
pop(position=None) → Remove o último elemento ou um elemento em uma posição específica.
Buscar e Modificar Elementos:

__getitem__(position) → Retorna o valor do elemento na posição especificada.
__setitem__(position, valor) → Altera o valor do elemento na posição especificada.
busca(valor) → Busca um valor na lista e retorna sua posição, ou -1 se não encontrado.
Outras Funcionalidades:

__str__() → Representação da lista encadeada como string.
__len__() → Retorna o tamanho atual da lista.
🛠 Estrutura do Projeto
Lista: Classe responsável pelas operações gerais da lista.
Nodo: Classe que representa os nós da lista, contendo o valor e o ponteiro para o próximo nó.
Exemplo de Uso:
python
Copiar código
# Importação e uso da classe
lista = Lista()

# Adicionando elementos
lista.add(10)
lista.append(20)
lista.insert(15, 1)

# Visualizando a lista
print(lista)  # Output: [ 10 , 15 , 20 ]

# Removendo elementos
lista.rem()
lista.pop()

# Modificando valores
lista[0] = 50
print(lista[0])  # Output: 50

# Buscando elementos
pos = lista.busca(15)
print(pos)  # Output: -1 (caso não encontrado)
🎯 Objetivo
Este código foi desenvolvido com o objetivo de praticar e demonstrar o funcionamento de listas encadeadas em Python, explorando conceitos como classes, construtores, e manipulação de ponteiros.

📂 Estrutura de Arquivos
bash
Copiar código
.
├── lista_encadeada.py   # Arquivo principal contendo as classes Lista e Nodo
└── README.md            # Documentação do projeto
🧩 Melhorias Futuras
Implementação de busca binária em listas ordenadas.
Conversão da lista encadeada em outras estruturas, como arrays ou filas.
🧑‍💻 Autor
Matheus Borges Borba dos Santos
Estudante de Matemática Industrial - UFPR

