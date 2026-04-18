import os
import matplotlib.pyplot as plt
from quick_union import QuickUnion

def carregar_dados(caminho_arquivo):
    """Lê o arquivo de teste e retorna o N e a lista de conexões."""
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
        print(f"Erro ao ler o arquivo: {e}")
        return None, []

def gerar_grafico_amortizado():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(diretorio_atual, "..", "Testes", "adversarial_100000.txt")
    
    tamanho, conexoes = carregar_dados(caminho_arquivo)
    if tamanho is None:
        return

    qu = QuickUnion(tamanho)
    
    eixo_x_conexoes = []
    eixo_y_custo_i = []
    eixo_y_custo_medio = []

    print(f"Processando uniões para N={tamanho} e coletando acessos...")
    for i, (p, q) in enumerate(conexoes):
        qu.union(p, q)
        
        eixo_x_conexoes.append(i + 1)
        eixo_y_custo_i.append(qu.custo_i)
        eixo_y_custo_medio.append(qu.get_custo_medio())

    print("Desenhando o gráfico...")
    plt.figure(figsize=(10, 6))
    
    plt.scatter(eixo_x_conexoes, eixo_y_custo_i, color='gray', label='Custo por operação (custo_i)', alpha=0.5, s=2)
    
    plt.plot(eixo_x_conexoes, eixo_y_custo_medio, color='red', label='Custo médio até i', linewidth=2)

    plt.title(f'Custo Amortizado - Quick-Union (N={tamanho})')
    plt.xlabel('Número de Conexões Processadas')
    plt.ylabel('Acessos ao vetor id[]')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    
    nome_imagem = f"grafico_amortizado_N{tamanho}.png"
    plt.savefig(nome_imagem, dpi=300, bbox_inches='tight')
    print(f"✓ Sucesso! Gráfico salvo como: {nome_imagem}")

if __name__ == "__main__":
    gerar_grafico_amortizado()