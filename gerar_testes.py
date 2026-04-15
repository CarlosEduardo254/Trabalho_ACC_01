import os

def gerar_casos_adversariais():
    # Tamanhos exigidos no PDF: 10.000, 50.000, 100.000 e 500.000
    tamanhos = [10000, 50000, 100000, 500000]
    
    diretorio_base = os.path.dirname(os.path.abspath(__file__))
    pasta_saida = os.path.join(diretorio_base, "Testes")
    
    # Garante que a pasta existe
    os.makedirs(pasta_saida, exist_ok=True)

    for n in tamanhos:
        nome_arquivo = os.path.join(pasta_saida, f"adversarial_{n}.txt")
        print(f"Gerando arquivo: adversarial_{n}.txt ...")
        
        with open(nome_arquivo, 'w') as f:
            # 1. A primeira linha é o N
            f.write(f"{n}\n")
            
            # 2. Padrão adversarial: "0 1", "0 2", "0 3" ... até N-1
            for i in range(1, n):
                f.write(f"0 {i}\n")
                
        print(f"✓ Concluído! ({n} elementos)")

if __name__ == "__main__":
    gerar_casos_adversariais()