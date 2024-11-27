# Para que serve isso ?

Esse software serve separar dados a partir de uam tabela em PDF e pesquisa na ECONODATA o CNPJ a partir da razao social.


# Como Usar ?
```bash
python extract.py tabela.pdf 5
```

# Como o software funciona por baixo dos panos ?

No primeiro argumento você precisa dizer o caminho do arquivo que está a tabela em PDF.

No segundo arquivo você dirá a quantidade de threads que serão executadas em paralelo. (Quanto mais threads, mais rápido será feito e mais memoria vai consumir paralelamente)