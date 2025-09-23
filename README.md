
# mrp_calculo

Pacote que organiza o código do MRP em funções com nomes em português e um CLI simples.

## Instalação (local)
```bash
pip install .
```

## Instalação (GitHub)
```bash
!pip install -q "git+https://github.com/gustavoairestiago/mrp_calculo.git"
```

## Uso como biblioteca
```python
from mrp_calculo import executar

df = executar(
    caminho_csv="dados.csv",
    caminho_xlsx="dicionario.xlsx",
    coluna_atual="cod_mare",
    coluna_destino="cod_orig",
    sep=";",
)
df.to_csv("resultado.csv", index=False)
notas.to_csv("notas.csv",index=False)
```

## Uso via CLI
```bash
python -m mrp_calculo --csv dados.csv --xlsx dicionario.xlsx --col-atual cod_mare --col-origem cod_orig --sep ';' --saida resultado.csv
```

> Observação: o cálculo em si é executado a partir do **código original** (mantido em `algoritmo_original.py`)
com as leituras de arquivo desativadas, de forma que os DataFrames já carregados são usados diretamente.
