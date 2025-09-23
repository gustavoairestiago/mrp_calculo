
# -*- coding: utf-8 -*-
import argparse
from .core import executar

def main():
    p = argparse.ArgumentParser(prog="mrp_calculo", description="Calcula indicadores do MRP e extrai as NOTAS.")
    p.add_argument("--csv", required=True, help="Caminho do CSV extraído do Kobo.")
    p.add_argument("--xlsx", required=True, help="Caminho do XLSX com dicionário (coluna atual -> coluna original).")
    p.add_argument("--col-atual", required=True, dest="col_atual", help="Nome da coluna no XLSX com os nomes ATUAIS (presentes no CSV).")
    p.add_argument("--col-origem", required=True, dest="col_origem", help="Nome da coluna no XLSX com os nomes ORIGINAIS do MRP.")
    p.add_argument("--sep", default=";", help="Separador do CSV. Padrão: ';'")
    p.add_argument("--saida", default=None, help="Caminho para salvar o CSV completo de saída (opcional).")
    p.add_argument("--saida-notas", default=None, help="Caminho para salvar o CSV apenas com NOTAS (opcional).")

    args = p.parse_args()

    df, notas = executar(
        args.csv, args.xlsx, coluna_atual=args.col_atual, coluna_destino=args.col_origem, sep=args.sep
    )

    if args.saida:
        df.to_csv(args.saida, index=False)
    if args.saida_notas:
        notas.to_csv(args.saida_notas, index=False)

    if not args.saida and not args.saida_notas:
        # Mostra um resumo
        print(\"==== Dados (head) ====\") 
        print(df.head().to_string())
        print(\"\\n==== NOTAS (head) ====\") 
        print(notas.head().to_string())

if __name__ == "__main__":
    main()
