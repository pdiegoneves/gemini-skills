import pandas as pd
import argparse
import sys
import os

def extrair_relatorios_xlsx(caminho_arquivo):
    print(f"Lendo o arquivo Excel: {caminho_arquivo}...")
    
    try:
        df = pd.read_excel(caminho_arquivo, header=None, engine='openpyxl')
    except Exception as e:
        print(f"Erro fatal ao ler o arquivo XLSX: {e}")
        sys.exit(1)

    secoes = {
        'Posições': [],
        'Ordens': [],
        'Transações': [],
        'Resultados': []
    }
    
    marcadores = ['Posições', 'Ordens', 'Transações', 'Resultados', 'Posições Abertas']
    secao_atual = None

    for index, row in df.iterrows():
        primeira_coluna = str(row[0]).strip() if pd.notna(row[0]) else ""

        if primeira_coluna in marcadores:
            if primeira_coluna == 'Posições Abertas':
                secao_atual = None 
            else:
                secao_atual = primeira_coluna
            continue

        if secao_atual:
            if not row.dropna().empty:
                secoes[secao_atual].append(row.tolist())

    # 1. Salvar as tabelas normais em CSV
    for nome_secao in ['Posições', 'Ordens', 'Transações']:
        linhas = secoes[nome_secao]
        if not linhas:
            continue
        
        df_secao = pd.DataFrame(linhas)
        df_secao.columns = df_secao.iloc[0]
        df_secao = df_secao[1:].reset_index(drop=True)
        
        # Remove acentos do nome do arquivo
        nome_arquivo = f"{nome_secao.lower().replace('ç', 'c').replace('õ', 'o')}.csv"
        df_secao.to_csv(nome_arquivo, index=False, encoding='utf-8')
        print(f"-> Sucesso: '{nome_arquivo}' gerado com {len(df_secao)} registros.")

    # 2. Salvar os Resultados em um TXT limpo
    linhas_resultados = secoes['Resultados']
    if linhas_resultados:
        txt_linhas = []
        for row in linhas_resultados:
            # Pega apenas as células que realmente têm texto (ignora os NaNs)
            celulas_validas = [str(x).strip() for x in row if pd.notna(x) and str(x).strip() != '']
            
            i = 0
            while i < len(celulas_validas):
                item = celulas_validas[i]
                
                # Se o texto terminar com ':', assumimos que é uma Chave (Ex: "Fator de Lucro:")
                if item.rstrip().endswith(':'):
                    chave = item
                    valor = ""
                    
                    # Verifica se a próxima célula válida é o valor da chave
                    if i + 1 < len(celulas_validas) and not celulas_validas[i+1].rstrip().endswith(':'):
                        valor = celulas_validas[i+1]
                        i += 2 # Pula a chave e o valor que já lemos
                    else:
                        i += 1 # Pula só a chave (às vezes o valor é vazio ou é título de bloco)
                        
                    txt_linhas.append(f"{chave} {valor}".strip())
                else:
                    i += 1

        with open('resultados.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(txt_linhas))
        print(f"-> Sucesso: 'resultados.txt' gerado em formato chave-valor estruturado.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("arquivo")
    args = parser.parse_args()
    
    if not os.path.exists(args.arquivo):
        print(f"Erro: Arquivo '{args.arquivo}' não encontrado.")
        sys.exit(1)
        
    extrair_relatorios_xlsx(args.arquivo)