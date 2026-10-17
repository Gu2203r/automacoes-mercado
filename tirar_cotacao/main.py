import pyautogui as pg
from time import sleep
import csv

# Coordenadas dos elementos na tela
carrinho = [444, 48]
cord_codigo = [299, 176]
cord_produto = [300, 255]
cord_comprador = [315, 700]
cord_salvar = [300, 470]

# Caminho do arquivo CSV com os códigos de produto
caminho_csv = "tirar_cotacao/produtos.csv"

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

    pg.click(x=carrinho[0], y=carrinho[1])
    sleep(1.5)
    pg.click(x=cord_codigo[0], y=cord_codigo[1])
    sleep(0.5)
    pg.write(produto)
    sleep(0.5)
    pg.press('f1')
    sleep(1)
    pg.doubleClick(x=cord_produto[0], y=cord_produto[1])
    sleep(6)

    tab = 9

    try:
        imagem = pg.locateOnScreen("tirar_cotacao/imagem.png", confidence=0.8)

    except:
        print("tem imagem")
        tab = 10

    for i in range(tab):

        pg.press('tab')
        sleep(0.2)

    pg.write('1')
    sleep(1)
    pg.press('f3')
    sleep(2)
    pg.press('esc')
    sleep(0.2)
    pg.press('esc')
    sleep(0.2)
    pg.press('esc')
    sleep(1)  # pequena pausa entre um produto e outro

print("Processamento concluído.")