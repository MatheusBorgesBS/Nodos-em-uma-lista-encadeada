# Lista Encadeada em Python 🚀

## 📄 Descrição

Este projeto implementa uma **estrutura de dados de lista encadeada** em Python, utilizando as classes `Lista` e `Nodo`. A classe `Lista` fornece diversas operações comuns para manipulação de listas, como adicionar, remover, inserir e buscar elementos.

A classe `Nodo` representa os nós individuais da lista, armazenando valores e referências ao próximo elemento (nó) da sequência.

---

## 🎯 Objetivo

O objetivo deste projeto é:

- Demonstrar o funcionamento de **listas encadeadas**.
- Aplicar conceitos de programação orientada a objetos em Python.
- Criar uma implementação prática de adição, remoção e busca de elementos em uma lista dinâmica.

---

## 🚧 Funcionalidades

- **Adicionar Elementos**:  
  - `add(item)` → Adiciona um elemento no início da lista.  
  - `append(item)` → Adiciona um elemento no final da lista.  
  - `insert(item, position)` → Insere um elemento em uma posição específica.  

- **Remover Elementos**:  
  - `rem()` → Remove o primeiro elemento da lista.  
  - `pop(position=None)` → Remove o último elemento ou um elemento em uma posição específica.  

- **Buscar e Modificar Elementos**:  
  - `__getitem__(position)` → Retorna o valor do elemento na posição especificada.  
  - `__setitem__(position, valor)` → Altera o valor do elemento na posição especificada.  
  - `busca(valor)` → Busca um valor na lista e retorna sua posição, ou -1 se não encontrado.  

- **Outras Funcionalidades**:  
  - `__str__()` → Representação da lista encadeada como string.  
  - `__len__()` → Retorna o tamanho atual da lista.  

---

## 🛠 Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

```plaintext
.
├── lista_encadeada.py   # Arquivo principal contendo as classes Lista e Nodo
└── README.md            # Documentação do projeto
