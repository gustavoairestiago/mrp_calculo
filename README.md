
# mrp_calculo

Pacote que organiza e calcula notas do MRP.

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

df,notas = executar(
    caminho_csv_kobo="dados.csv",
    caminho_xlsx_variaveis="dicionario.xlsx",
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
