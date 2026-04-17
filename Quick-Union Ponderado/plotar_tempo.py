import os
import time
import statistics
import matplotlib.pyplot as plt
from quick_union_ponderado import QuickUnionPonderado

def carregar_dados(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
        if not linhas:
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
        print(f"Erro: {e}")
        return None, []

def gerar_grafico_tempo():
    # Tamanhos razoáveis para não travar a máquina (excluindo 500.000 se demorar demais)
    tamanhos = [10000, 50000, 100000]
    medias = []
    desvios = []
    
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    numero_execucoes = 10
    
    print("Iniciando benchmark unificado...")
    for n in tamanhos:
        caminho_arquivo = os.path.join(diretorio_atual, "..", "Testes", f"adversarial_{n}.txt")
        tamanho, conexoes = carregar_dados(caminho_arquivo)
        
        if tamanho is None:
            continue
            
        tempos_execucao = []
        print(f"Testando N={n} ({numero_execucoes} execuções)...")
        
        for _ in range(numero_execucoes):
            qup = QuickUnionPonderado(tamanho)
            inicio = time.perf_counter()
            for p, q in conexoes:
                qup.union(p, q)
            fim = time.perf_counter()
            tempos_execucao.append(fim - inicio)
            
        media = statistics.mean(tempos_execucao)
        desvio = statistics.stdev(tempos_execucao)
        medias.append(media)
        desvios.append(desvio)
        
    print("\nDesenhando o gráfico de tempo...")
    plt.figure(figsize=(10, 6))
    
    # A mágica acontece aqui: errorbar plota a linha e os "pauzinhos" do desvio padrão
    plt.errorbar(tamanhos, medias, yerr=desvios, fmt='-o', color='blue', 
                 ecolor='red', capsize=5, label='Tempo Médio ± Desvio Padrão')
    
    # Formatação exigida
    plt.title('Tempo de Execução vs N - Quick-Union Ponderado')
    plt.xlabel('Quantidade de elementos das instâncias testadas (N)')
    plt.ylabel('Tempo de execução (segundos)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    
    nome_imagem = "grafico_tempo_execucao_QUP.png"
    plt.savefig(nome_imagem, dpi=300, bbox_inches="tight")
if __name__ == "__main__":
    gerar_grafico_tempo()