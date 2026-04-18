class QuickUnionPonderado:
    def __init__(self, n):
        self.id = list(range(n))
        self.size = [1] * n # Todas as raízes devem começar com 1 de tamanho
        
        self.custo_i = 0
        self.total_i = 0  # Total acumulado de acessos
        self.conexoes_processadas = 0
        
    def reset_custo(self):
        self.custo_i = 0
        self.conexoes_processadas += 1

    def find(self, p):
        self.custo_i += 1 # Acesso para o primeiro while
        while self.id[p] != p:
            p = self.id[p]
            self.custo_i += 2 # Tem o acesso no while e na atribuição
        return p
        
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    
    def union(self, p, q):
        self.reset_custo()
        
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot == qRoot:
            self.total_i += self.custo_i
            return
        if self.size[pRoot] < self.size[qRoot]:
            self.id[pRoot] = qRoot # Como p é menor, q deverá ser a raiz
            self.size[qRoot] += self.size[pRoot] # qRoot passa a ser a raiz e seu tamanho é atualizado
            
            self.custo_i += 1 # Estamos contando apenas os acessos a id[]
            self.total_i += self.custo_i
        else:
            self.id[qRoot] = pRoot # Caso contrário, q é menor então p deve ser a raiz
            self.size[pRoot] += self.size[qRoot] # pRoot passa a ser a raiz e seu tamanho é atualizado
            
            self.custo_i += 1 # Estamos contando apenas os acessos a id[]
            self.total_i += self.custo_i
    
    def get_custo_medio(self):
        if self.conexoes_processadas == 0:
            return 0
        return self.total_i / self.conexoes_processadas