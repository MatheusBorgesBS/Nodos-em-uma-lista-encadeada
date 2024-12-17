# Classe onde ocorre as operações da Lista
class Lista():
    # Construtor de argumentos self que serão utilizados na lista.
    def __init__(self):
        # Primeiro Nodo é None até que um nodo seja adicionado a ele pela classe Nodo().
        self.firstnode = None
        # Tam que se altera de tal forma que +1 para items adicionados na lista, -1 para items removidos dela.
        self.tam = 0

    # Função para retornar o tamanho da lista, unico argumento é o self.tam que se atualiza de forma ja apresentada antes.     
    def __len__(self):      
        return self.tam

    # Função Str que sera o output de todo comando print
    def __str__(self):
        # Começa com uma str vazia, que vai concatenando com as informações adicionadas
        s = ""
        ''' Uma variavel recebe o valor atual do firstnode, se o firstnode estiver como None, momento sem nenhum item adicionado a lista ele vai passar o while e returnar algo direto
            Se ele recebe um valor ele vai concatenar até que seu proximo seja none, ou seja acabou os nodos e entao retorna a string''' 
        nodo = self.firstnode
        while nodo != None:
            s += str(nodo)
            if nodo.next != None:
                s += (' , ')
            nodo = nodo.next

        return (f'[ {s} ]')

    #Função para adicionar valores aos nodos
    
    def add(self, item):
        # se o primeiro nodo for vazio, ou seja o começo da lista, ele só vai adicionar o valor chamando a classe nodo com só o parametro do item
        if self.firstnode == None:
            self.firstnode = Nodo(item)
        #Se o firstnode ja tem algum valor, o variavel nodo vai receber ele e ser passada como parametro de next para classe nodo, entao o novo nodo recebe o valor do item,
        # dessa forma cria uma lista encadeada que o novo valor aponta para o next
        else:
            nodo = self.firstnode
            self.firstnode = Nodo(item, nodo)
        self.tam += 1           

    # Função para remover o primeiro nodo
    def rem(self,):
        ''' a variavel nodo recebe o nodo da posiçao inicial atual só para poder retornar oque foi removido, o if verifica se o nodo atual é diferente de None,
            caso atenta essa condição agora o firstnode vai virar o nodo para quem ele estava apontando dessa forma oque estava em primeiro passar ser o proximo removendo ele
            da lista de nodos'''
        nodo = self.firstnode
        if self.firstnode != None:
            self.firstnode = self.firstnode.next 
            self.tam -= 1
        return nodo

    #Função para adicionar o nodo na ultima posição, um append dele.
    def append(self, item):
        #Quando o primeiro nodo for none nao tem oque fazer, apenas adicionar um novo nodo pelo append.
        if self.firstnode == None:
            self.firstnode = Nodo(item)
        #Caso seja != None,  entao meu nodo recebe o primeiro nodo, e percorre todos eles até que o proximo seja None, até isso ela percorre a lista todo com o .next
        # Quando chega no ultimo, ela termina o loop e o nodo.next vai ser chamado com a classe nodo() e o valor do append, entao ele se torna o ultimo nodo e o .next
        # continua sendo None    
        else:
            nodo = self.firstnode
            while nodo.next != None:
                nodo = nodo.next
            nodo.next = Nodo(item)
        self.tam += 1
    
    #Função para inserir algum valor em um indice do nodo especifico 
    def insert(self, item, position):
        #Primeiro criamos um novo nodo e adicionamos o valor dele
        novo_nodo = Nodo(item)
        # Se a posiçao for 0 ou seja o primeiro indice da lista, o nosso next do nosso novo_nodo recebe o atual primeiro nodo, e depois o primeiro nodo recebe o novo nodo
        if position == 0:
            novo_nodo.next = self.firstnode
            self.firstnode = novo_nodo
        # Se ela for diferente de 0, entao fazemos basicamente a mesma coisa, porém percoremos a lista até a posiçao-1 (porque começa em 0) e adicionamos o nodo daquela posiçao 
        # como o proximo, e o nodo que estava naquela posiçao agora é nosso novo nodo, dessa forma a lista se mantem encadeada, e atualizamos a lista percorrendo ela para posicoes
        # diferentes de 0
        else:
            nodo = self.firstnode
            for _ in range(position - 1):
                nodo = nodo.next
            novo_nodo.next = nodo.next
            nodo.next = novo_nodo
        self.tam += 1
    
    # Funçao pop, vai remover ou o ultimo nodo se nao tiver posiçao, ou uma posiçao especifica.
    def pop(self,position = None):
        # A ideia utilizada aqui é usar uma variavel que vai ficar sendo chamada pro next, e uma que recebe a anterior.
        nodo = self.firstnode
        nodo_anterior = None
        # Se a posiçao nao for indicada, vamos percorrer a o tam_lista-1 (porque começa em 0)
        if position == None:
            position = self.tam - 1
        # Percorremos ate a posiçao especifica,  
        for i in range(position + 1): 
            # se i for a posiçao que queremos, removemos o primeiro nodo, se não transformamos o nodo_anterior no proximo nodo
            if i == position:
                if nodo_anterior == None: 
                    self.firstnode = nodo.next
                else:
                    nodo_anterior.next = nodo.next
                self.tam -= 1
                # retorna o valor do nodo desejado
                return nodo.value  
            # aqui o nodo anterior recebe o proximo e o nodo atual pula pro proximo
            nodo_anterior, nodo = nodo , nodo.next
                        
    # Funçao para verificar o nodo pela posiçao.
    def __getitem__ (self,position):
        # setamos o primeiro nodo para o firstnode e percorremos uma lista até a posiçao que queremos, enquanto percorre até ela, atualizamos nosso nodo para o proximo,
        # Depois só retornamos o valor do nodo que estara na posiçao que pedimos.
        nodo = self.firstnode
        for _ in range (position):
            nodo = nodo.next
        return nodo.value     
    
    # Funçao para mudarmos o valor de uma posiçao, recebemos a posiçao e o valor, setamos o nodo para o firstnode, e percorremos um vetor até a posiçao que queremos e vamos 
    # Atualizando o nodo para o next até ela, e quando chegamos la, alteramos a propriedade de nodo.value para o valor desejado.
    def __setitem__(self, position, valor):
        nodo = self.firstnode
        for _ in range(position):
            nodo = nodo.next
        nodo.value = valor
    
    # Funçao busca, serve para buscar verificar um item se ele esta no nodo, aqui ele estara usando uma busca sequencial, entao percorremos um vetor do tamanho da lista,
    # enquanto percorre, comparamos o valor com os values dos nodos, se ele achar o valor ele retorna i que sera a posiçao que o nodo esta, se não achar ele retorna -1
    def busca(self, valor):
        nodo = self.firstnode
        for i in range (self.tam):
            if valor ==  nodo.value:
                return i
            else:
                nodo = nodo.next
        return -1      

# Classe nodo, queremos orientar objetos com valores e que estejam apontado para eles mesmos,
class Nodo(Lista):
    # Construtor, recebe o valor que o nodo sera, e por definiçao, o next começa apontando para none, e sempre que adicionado um novo sera none, ele só deixa de ser vazio
    # Em casos que queremos adicionar um nodo no meio da lista
    def __init__(self, valor, next = None):
        # Value é o valor do nodo, e next para apontar para o proximo.
        self.value = valor
        self.next = next
    
    # Str, quando queremos printar um nodo, normalmente só queremos saber qual é o valor indicado no nodo.
    def __str__(self):
        return str(self.value)
    

