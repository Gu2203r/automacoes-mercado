import pyautogui as pg
from time import sleep
import csv

cod_produto = [396, 170]
checkbox = [63, 257]
excluir = [150, 105]

# Caminho do arquivo CSV com os códigos de produto
caminho_csv = "excluir_itens/produtos.csv"

# Lê os códigos do CSV (assume uma coluna, sem cabeçalho)
def ler_codigos(caminho):
    codigos = []
    with open(caminho, newline='', encoding='utf-8') as f:
        leitor = csv.reader(f)
        for linha in leitor:
            if linha and linha[0].strip():
                codigos.append(linha[0].strip())
    return codigos

codigos = ler_codigos(caminho_csv)
print(f"Total de produtos a processar: {len(codigos)}")

for i, produto in enumerate(codigos, start=1):
    print(f"[{i}/{len(codigos)}] Processando produto {produto}")

    pg.click(x=cod_produto[0], y=cod_produto[1])
    sleep(0.5)
    pg.write(produto)
    sleep(0.5)
    pg.press('f1')
    sleep(1)
    pg.click(x=checkbox[0], y=checkbox[1])
    sleep(0.5)
    pg.click(x=excluir[0], y=excluir[1])
    sleep(0.5)
    pg.press('tab')
    sleep(0.5)
    pg.press('enter')
    sleep(0.5)
    pg.press('enter')

    sleep(1)  # pequena pausa entre um produto e outro

print("Processamento concluído.")
