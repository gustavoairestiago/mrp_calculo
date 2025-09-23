
# -*- coding: utf-8 -*-
import argparse
from .core import executar

def main():
    p = argparse.ArgumentParser(prog="mrp_calculo", description="Calcula indicadores do MRP a partir de um CSV e um XLSX de mapeamento.")
    p.add_argument("--csv", required=True, help="Caminho do CSV extraído do Kobo.")
    p.add_argument("--xlsx", required=True, help="Caminho do XLSX com dicionário de variáveis (coluna atual -> coluna original).")
    p.add_argument("--col-atual", required=True, help="Nome da coluna no XLSX com os nomes ATUAIS (presentes no CSV).")
    p.add_argument("--col-origem", required=True, help="Nome da coluna no XLSX com os nomes ORIGINAIS do MRP.")
    p.add_argument("--sep", default=";", help="Separador do CSV. Padrão: ';'")
    p.add_argument("--saida", default=None, help="Caminho para salvar o CSV de saída (opcional).")

    args = p.parse_args()

    df = executar(args.csv, args.xlsx, coluna_atual=args["col-atual"] if hasattr(args, "col-atual") else args.col_atual,
                  coluna_destino=args["col-origem"] if hasattr(args, "col-origem") else args.col_origem,
                  sep=args.sep)

    if args.saida:
        df.to_csv(args.saida, index=False)
    else:
        # Mostra um resumo no stdout
        print(df.head().to_string())

if __name__ == "__main__":
    main()
