class QuickFind:
    def __init__(self, n):
        # Inicializa o vetor onde cada elemento é a raiz de seu próprio componente
        self.id = list(range(n))

        # Variáveis para as métricas de desempenho
        self.custo_i = 0
        self.total_i = 0  # Total acumulado de acessos
        self.conexoes_processadas = 0

    def reset_custo(self):
        # Zera os contadores para uma nova operação de conexão.
        self.custo_i = 0
        self.conexoes_processadas += 1

    def find(self, p):
        self.custo_i += 1  # acesso de leitura
        return self.id[p]

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        self.reset_custo()

        pid = self.find(p)
        qid = self.find(q)

        # Se já estão no mesmo componente, finaliza o processamento desta conexão
        if pid == qid:
            self.total_i += self.custo_i
            return

        # Para o Quick-Find, precisamos varrer o vetor inteiro
        for i in range(len(self.id)):
            self.custo_i += 1  # 1 acesso de leitura na verificação (self.id[i] == pid)

            if self.id[i] == pid:
                self.id[i] = qid
                self.custo_i += 1  # 1 acesso de escrita na atribuição

        # Acumula o custo da i-ésima conexão no total geral
        self.total_i += self.custo_i

    def get_custo_medio(self):
        # Calcula o custo amortizado: total_i / i
        if self.conexoes_processadas == 0:
            return 0
        return self.total_i / self.conexoes_processadas
