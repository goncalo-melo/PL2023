import re 

def abbreviations_expansion(string, abbreviations):  
    return re.sub(
        r'/abrev\{(?P<abrev>[A-Z]+)\}', 
        lambda m: abbreviations.get(m.group('abrev'), m.group()),
        string
        )

def main():
    abreviaturas = {
        "UM": "Universidade do Minho",
        "LEI": "Licenciatura em Engenharia Informática",
        "UC": "Unidade Curricular",
        "PL": "Processamento de Linguagens"
    }

    texto = "A /abrev{UC} de /abrev{PL} é muito fixe! É uma /abrev{UC} que acrescenta muito ao curso de /abrev{LEI} da /abrev{UM}."

    print(abbreviations_expansion(texto, abreviaturas))

if __name__ == "__main__":
    main()
