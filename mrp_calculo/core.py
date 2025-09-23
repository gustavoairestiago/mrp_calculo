
# -*- coding: utf-8 -*-
"""mrp_calculo.core

Funções em português para carregar dados, aplicar o dicionário de mapeamento de variáveis
e calcular os indicadores do MRP, reutilizando exatamente o código fornecido pelo usuário.
"""
from __future__ import annotations
import pandas as pd
import numpy as np
from types import SimpleNamespace
from pathlib import Path

def ler_arquivos(caminho_csv_kobo: str, caminho_xlsx_variaveis: str, sep: str = ';') -> tuple[pd.DataFrame, pd.DataFrame]:
    """Lê os arquivos de base.

    Parâmetros
    ----------
    caminho_csv_kobo : str
        Caminho para o CSV de extração do MRP (resultado do Kobo).
    caminho_xlsx_variaveis : str
        Caminho para o XLSX contendo o dicionário com a variável original e a variável atual.
    sep : str, default=';'
        Separador do CSV.

    Retorna
    -------
    (df, df_map) : tuple
        DataFrame principal e DataFrame do dicionário de mapeamento.
    """
    df = pd.read_csv(caminho_csv_kobo, sep=sep)
    df_map = pd.read_excel(caminho_xlsx_variaveis)
    return df, df_map

def aplicar_mapeamento(df: pd.DataFrame, df_map: pd.DataFrame, coluna_atual: str, coluna_destino: str) -> pd.DataFrame:
    """Aplica o mapeamento de nomes de colunas do CSV (atual) para os nomes originais do MRP.

    É a transposição direta do trecho de código enviado pelo usuário.

    Parâmetros
    ----------
    df : DataFrame
    df_map : DataFrame
    coluna_atual : str
        Nome da coluna no XLSX que contém os nomes atuais (no CSV/extração).
    coluna_destino : str
        Nome da coluna no XLSX que contém os nomes originais (como usado no MRP).

    Retorna
    -------
    DataFrame com colunas renomeadas quando aplicável.
    """
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

def calcular_indicadores(df_renomeado: pd.DataFrame) -> pd.DataFrame:
    """Executa o cálculo dos indicadores exatamente como no código original.

    Implementação: executa o conteúdo do arquivo 'algoritmo_original.py' dentro de um namespace
    onde as variáveis 'df' e 'df_map' já estão definidas adequadamente. Como o arquivo original
    contém a lógica de transformação (e não dependemos de leituras de arquivo), basta injetar
    o DataFrame renomeado em 'df' e usar um df_map vazio (não é mais utilizado nesta fase).
    """
    import runpy, types, importlib.util, sys, os

    # Carrega o texto do algoritmo original
    modulo_path = Path(__file__).with_name("algoritmo_original.py")

    # Monta um namespace com df/df_map
    ns = {}
    ns['pd'] = pd
    ns['np'] = np
    ns['df'] = df_renomeado.copy()
    # df_map não é utilizado após o renomeio; ainda assim mantemos por compatibilidade
    ns['df_map'] = pd.DataFrame()

    # Executa o código original (com leituras desativadas) dentro do namespace
    code = modulo_path.read_text(encoding='utf-8')
    exec(compile(code, str(modulo_path), 'exec'), ns, ns)

    # Ao final do script original, 'df' contém as colunas calculadas
    if 'df' not in ns or not isinstance(ns['df'], pd.DataFrame):
        raise RuntimeError("Execução do algoritmo original não produziu um DataFrame 'df'.")
    return ns['df']

def executar(caminho_csv_kobo: str, caminho_xlsx_variaveis: str, coluna_atual: str, coluna_destino: str, sep: str = ';') -> pd.DataFrame:
    """Pipeline completo: lê, aplica mapeamento e calcula indicadores.

    Parâmetros
    ----------
    caminho_csv_kobo : str
    caminho_xlsx_variaveis : str
    coluna_atual : str
    coluna_destino : str
    sep : str, default=';'

    Retorna
    -------
    DataFrame final com indicadores.
    """
    df, df_map = ler_arquivos(caminho_csv_kobo, caminho_xlsx_variaveis, sep=sep)
    df_renomeado = aplicar_mapeamento(df, df_map, coluna_atual, coluna_destino)
    df_final = calcular_indicadores(df_renomeado)
    return df_final
