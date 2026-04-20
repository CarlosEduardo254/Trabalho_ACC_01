# Trabalho Prático 01 - Instruções

*OBS*: O arquivo largeUF.txt foi retirados das pastas <algoritmo>/TestesProntos, pois o SIGAA só aceita arquivos de até 10MB e apenas o largeUF ocupava quase 30MB, se quiser testá por favor baixe o arquivo acessando esse link abaixo e copie para a pasta TestesProntos no respectivo algoritmo que gostaria de testar
*Link:* https://algs4.cs.princeton.edu/15uf/largeUF.txt

Este diretório contém a implementação, análise de tempo e de custo amortizado dos algoritmos de conectividade dinâmica: **Quick-Find**, **Quick-Union** e **Quick-Union Ponderado**.

## Pré-requisitos e Ambiente

Os algoritmos foram desenvolvidos em **Python**. O código não necessita de compilação, sendo interpretado diretamente. Para executar os testes e gerar os gráficos presentes no relatório, você precisará ter em sua máquina:

- **Python 3.x** (Recomendado 3.10 ou superior)
- **Matplotlib** (Biblioteca necessária para plotagem dos gráficos de análise)

Caso não tenha o Matplotlib instalado, você pode instalá-lo executando o seguinte comando no terminal:

`pip install matplotlib`

## Estrutura do Projeto

O projeto está dividido em pastas para cada abordagem do algoritmo, além de pastas para os arquivos de testes:

- `Quick Find/`: Contém os scripts `quick_find.py`, `main.py` e os scripts de geração de gráficos (`plotar_tempo.py`, `plotar_custos.py`).
- `Quick Union/`: Contém a implementação base e análises do Quick-Union.
- `Quick-Union Ponderado/`: Contém a implementação otimizada e suas análises.
- `Testes/` e `TestesProntos/`: Pastas que armazenam os arquivos `.txt` com os casos de teste em diferentes tamanhos (N = 10.000, 50.000, 100.000, etc.), incluindo instâncias adversariais.
- `gerar_testes.py`: Script raiz utilizado para criar dinamicamente os casos de teste utilizados no trabalho.
- `Trabalho_de_ACC.pdf`: O relatório final em PDF detalhando a metodologia e os resultados.

## Instruções de Execução

### 1. Executando os Algoritmos

Para rodar a implementação principal de um algoritmo e verificar seu processamento nos arquivos de teste padrão, abra seu terminal, navegue até a pasta correspondente e execute o script `main.py`.

**Exemplo executando o Quick-Find:**
`cd "Quick Find"`
`python main.py`

*(Nota: Dependendo da configuração do seu sistema (Linux/Windows), pode ser necessário utilizar `python3 main.py`)*

Caso queira mudar a instância de teste, vá para a linha 30 que possui a sintaxe abaixo e mude apenas o nome do arquivo que deseja testar:

`caminho_arquivo = os.path.join("TestesProntos", "mediumUF.txt")`

Para testar o tinyUF.txt, por exemplo, mude para:

`caminho_arquivo = os.path.join("TestesProntos", "tinyUF.txt")`

### 2. Gerando os Gráficos de Análise

Dentro do diretório de cada um dos três algoritmos, existem scripts dedicados à plotagem visual dos resultados discutidos no relatório.

Para rodar a análise de **tempo de execução** empírico, execute:
`python plotar_tempo.py`

Para rodar a análise de **custo amortizado** das operações:
`python plotar_custos.py`

Os gráficos gerados serão ou salvos como `.png` no respectivo diretório.

O plot do tempo irá plotar todas as instâncias de teste possíveis para o algoritmo, por sua vez o plot do custo irá plotar apenas 1 instância por vez, para mudar a instância da plotagem vá para a linha 27 do arquivo `plotar_custo.py` e modifique apenas o nome do arquivo para o caso adversarial que você deseja, por exemplo:

`caminho_arquivo = os.path.join(diretorio_atual, "..", "Testes", "adversarial_500000.txt")`

Para rodar o com 100 000 elementos:

`caminho_arquivo = os.path.join(diretorio_atual, "..", "Testes", "adversarial_100000.txt")`

### 3. Gerando Novos Casos de Teste (Opcional)

Caso deseje recriar os arquivos `.txt` adversariais, basta executar o script de geração na raiz do projeto:

`python gerar_testes.py`

Isso irá popular a pasta `Testes/` com os testes adversariais para serem lidos pelos algoritmos.
