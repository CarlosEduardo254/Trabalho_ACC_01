import os
import time
import statistics
from quick_union_ponderado import QuickUnionPonderado

def carregar_dados(caminho_arquivo):
    """Lê o arquivo uma única vez e retorna o N e a lista de conexões."""
    try:
        with open(caminho_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
        
        if not linhas:
            print("Erro: O arquivo está vazio!")
            return None, []

        tamanho = int(linhas[0].strip())
        conexoes = []
        for linha in linhas[1:]:
            linha = linha.strip()
            if linha:
                p, q = map(int, linha.split())
                conexoes.append((p, q))
                
        return tamanho, conexoes
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None, []

def executar_benchmark():
    caminho_arquivo = os.path.join("Testes", "mediumUF.txt")
    print(f"Carregando dados de {caminho_arquivo}...")
    
    tamanho, conexoes = carregar_dados(caminho_arquivo)
    if tamanho is None:
        return

    numero_execucoes = 10
    tempos_execucao = []

    print("-" * 55)
    print(f"Iniciando Benchmark: Quick-Union Ponderado (N = {tamanho})")
    print(f"Executando {numero_execucoes} vezes...")
    print("-" * 55)

    for i in range(numero_execucoes):
        # 1. Instancia uma árvore zerada para cada rodada
        qup = QuickUnionPonderado(tamanho)
        
        # 2. Inicia o cronômetro de alta precisão
        inicio = time.perf_counter()
        
        # 3. Roda o algoritmo puro (SEM PRINTS!)
        for p, q in conexoes:
            qup.union(p, q)
            
        # 4. Para o cronômetro
        fim = time.perf_counter()
        
        tempo_decorrido = fim - inicio
        tempos_execucao.append(tempo_decorrido)
        print(f"Rodada {i+1:02d}: {tempo_decorrido:.5f} segundos")

    # 5. Calcula Média e Desvio Padrão automaticamente
    tempo_medio = statistics.mean(tempos_execucao)
    desvio_padrao = statistics.stdev(tempos_execucao)

    print("-" * 55)
    print("Resultados Finais:")
    print(f"Tempo Médio:    {tempo_medio:.5f} segundos")
    print(f"Desvio Padrão:  {desvio_padrao:.5f} segundos")

if __name__ == "__main__":
    executar_benchmark()