import os

def gerar_casos_adversariais():
    tamanhos = [10000, 50000, 100000, 500000]
    
    diretorio_base = os.path.dirname(os.path.abspath(__file__))
    pasta_saida = os.path.join(diretorio_base, "Testes")
    
    os.makedirs(pasta_saida, exist_ok=True)

    for n in tamanhos:
        nome_arquivo = os.path.join(pasta_saida, f"adversarial_{n}.txt")
        print(f"Gerando arquivo: adversarial_{n}.txt ...")
        
        with open(nome_arquivo, 'w') as f:
            # 1. A primeira linha é o N
            f.write(f"{n}\n")
            
            for i in range(1, n):
                f.write(f"0 {i}\n")
                
        print(f"✓ Concluído! ({n} elementos)")

if __name__ == "__main__":
    gerar_casos_adversariais()