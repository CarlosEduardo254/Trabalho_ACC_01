class QuickUnion:
    def __init__(self, n):
        self.id = list(range(n))
        
        # Variáveis para as métricas de desempenho
        self.custo_i = 0
        self.total_i = 0  # Total acumulado de acessos
        self.conexoes_processadas = 0
        
    def reset_custo(self):
        self.custo_i = 0
        self.conexoes_processadas += 1

    def find(self, p):
        # 1 acesso de leitura para a primeira avaliação da condição do while
        self.custo_i += 1 
        
            # Diferente do Quick Find, aqui buscamos a raiz navegando entre os nós "pais" até encontrar que seja igual, pq se for igual ele é a raiz
        while p != self.id[p]:
            p = self.id[p]
            # 1 acesso para a atribuição (p = self.id[p]) 
            # + 1 acesso para a próxima avaliação da condição do while
            self.custo_i += 2   
        return p
        
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    
    def union(self, p, q):
        self.reset_custo()
        
        # Achar os "pais" de p e q
        pRoot = self.find(p)
        qRoot = self.find(q)
        
        # Caso possuam a mesma raiz
        if pRoot == qRoot:
            self.total_i += self.custo_i # Acumula para o custo total
            return
            
        self.id[pRoot] = qRoot
        self.custo_i += 1 # Acesso da escrita na atribuição
        self.total_i += self.custo_i # Acumula para o custo total
        
        
    def get_custo_medio(self):
        # Calcula o custo amortizado: total_i / i
        if self.conexoes_processadas == 0:
            return 0
        return self.total_i / self.conexoes_processadas
