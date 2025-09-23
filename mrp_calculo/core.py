
# -*- coding: utf-8 -*-
"""mrp_calculo.core

Funções em português para carregar dados, aplicar o dicionário de mapeamento de variáveis
e calcular os indicadores do MRP, reutilizando exatamente o código fornecido pelo usuário.
"""
from __future__ import annotations
import pandas as pd
import numpy as np
from pathlib import Path

def ler_arquivos(caminho_csv_kobo: str, caminho_xlsx_variaveis: str, sep: str = ';') -> tuple[pd.DataFrame, pd.DataFrame]:
    """Lê os arquivos de base."""
    df = pd.read_csv(caminho_csv_kobo, sep=sep)
    df_map = pd.read_excel(caminho_xlsx_variaveis)
    return df, df_map

def aplicar_mapeamento(df: pd.DataFrame, df_map: pd.DataFrame, coluna_atual: str, coluna_destino: str) -> pd.DataFrame:
    """Aplica o mapeamento de nomes de colunas (atual -> original)."""
    for c in (coluna_atual, coluna_destino):
        if c not in df_map.columns:
            raise ValueError(f"Coluna '{c}' não encontrada no XLSX. Colunas disponíveis: {list(df_map.columns)}")

    m = (
        df_map[[coluna_atual, coluna_destino]]
        .dropna()
        .astype(str)
        .apply(lambda s: s.str.strip())
        .drop_duplicates(subset=[coluna_atual])
    )
    m = m[m[coluna_destino] != ""]
    dicionario = dict(zip(m[coluna_atual], m[coluna_destino]))

    efetivo = {k: v for k, v in dicionario.items() if k in df.columns}
    df_renomeado = df.rename(columns=efetivo)
    return df_renomeado

def extrair_notas(df: pd.DataFrame) -> pd.DataFrame:
    """Extrai apenas as colunas de notas do DataFrame final.

    Critério: qualquer coluna cujo nome contenha 'NOTA' (case-insensitive).
    """
    cols_nota = [c for c in df.columns if "NOTA" in c.upper()]
    return df.loc[:, cols_nota].copy()

def calcular_indicadores(df_renomeado: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Executa o cálculo dos indicadores e também extrai as 'NOTAS'."""
    # Carrega o texto do algoritmo original
    modulo_path = Path(__file__).with_name("algoritmo_original.py")

    # Monta um namespace com df/df_map
    ns = {}
    ns['pd'] = pd
    ns['np'] = np
    ns['df'] = df_renomeado.copy()
    ns['df_map'] = pd.DataFrame()  # compatibilidade

    code = modulo_path.read_text(encoding='utf-8')
    exec(compile(code, str(modulo_path), 'exec'), ns, ns)

    if 'df' not in ns or not isinstance(ns['df'], pd.DataFrame):
        raise RuntimeError("Execução do algoritmo original não produziu um DataFrame 'df'.")

    df_final = ns['df']
    df_notas = extrair_notas(df_final)
    return df_final, df_notas

def executar(caminho_csv_kobo: str, caminho_xlsx_variaveis: str, coluna_atual: str, coluna_destino: str, sep: str = ';') -> tuple[pd.DataFrame, pd.DataFrame]:
    """Pipeline completo: lê, aplica mapeamento e calcula indicadores + notas."""
    df, df_map = ler_arquivos(caminho_csv_kobo, caminho_xlsx_variaveis, sep=sep)
    df_renomeado = aplicar_mapeamento(df, df_map, coluna_atual, coluna_destino)
    df_final, df_notas = calcular_indicadores(df_renomeado)
    return df_final, df_notas
