import pyautogui as pg
from time import sleep
import csv

cod_adicionar = [740, 457]

# Caminho do arquivo CSV com os códigos de produto
caminho_csv = "adicionar_balanco/produtos.csv"

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
print(f"Total de produtos a adicionar ao balanço: {len(codigos)}")

for i, produto in enumerate(codigos, start=1):
    print(f"[{i}/{len(codigos)}] Adicionando produto {produto}")

    sleep(1)
    pg.click(x=cod_adicionar[0], y=cod_adicionar[1])
    sleep(0.5)
    pg.write(produto)
    sleep(0.5)
    pg.press('tab')
    sleep(0.5)
    pg.press('tab')
    sleep(0.5)
    pg.write('0')
    sleep(0.5)
    pg.press('tab')
    sleep(0.5)
    pg.press('enter')



    sleep(1)  # pequena pausa entre um produto e outro

print("Processamento concluído.")
