import os
import matplotlib.pyplot as plt
from quick_find import QuickFind

def carregar_dados(caminho_arqfivo):
    """Lê o arqfivo de teste e retorna o N e a lista de conexões."""
    try:
        with open(caminho_arqfivo, "r") as arqfivo:
            linhas = arqfivo.readlines()
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
        print(f"Erro ao ler o arqfivo: {e}")
        return None, []

def gerar_grafico_amortizado():
    # 1. Navega para a pasta Testes na RAIZ do projeto
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arqfivo = os.path.join(diretorio_atual, "..", "Testes", "adversarial_10000.txt")
    
    tamanho, conexoes = carregar_dados(caminho_arqfivo)
    if tamanho is None:
        return

    qf = QuickFind(tamanho)
    
    # Listas para armazenar as coordenadas (X, Y) do gráfico
    eixo_x_conexoes = []
    eixo_y_custo_i = []
    eixo_y_custo_medio = []

    print(f"Processando uniões para N={tamanho} e coletando acessos...")
    for i, (p, q) in enumerate(conexoes):
        qf.union(p, q)
        
        # O eixo X é o número da conexão processada (começando de 1)
        eixo_x_conexoes.append(i + 1)
        eixo_y_custo_i.append(qf.custo_i)
        eixo_y_custo_medio.append(qf.get_custo_medio())

    print("Desenhando o gráfico...")
    plt.figure(figsize=(10, 6))
    
    # Custo pontual (Cinza). Usamos scatter (pontos) com transparência (alpha) 
    # para não virar um bloco sólido de cor e esconder a linha vermelha.
    plt.scatter(eixo_x_conexoes, eixo_y_custo_i, color='gray', label='Custo por operação (custo_i)', alpha=0.5, s=2)
    
    # Custo médio (Vermelho). Usamos plot (linha contínua).
    plt.plot(eixo_x_conexoes, eixo_y_custo_medio, color='red', label='Custo médio até i', linewidth=2)

    # Formatação exigida pelo trabalho
    plt.title(f'Custo Amortizado - Quick Find (N={tamanho})')
    plt.xlabel('Número de Conexões Processadas')
    plt.ylabel('Acessos ao vetor id[]')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    
    # Salva a imagem em alta resolução (300 dpi) na pasta atual
    nome_imagem = f"grafico_amortizado_N{tamanho}.png"
    plt.savefig(nome_imagem, dpi=300, bbox_inches='tight')
    print(f"✓ Sucesso! Gráfico salvo como: {nome_imagem}")

if __name__ == "__main__":
    gerar_grafico_amortizado()