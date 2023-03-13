import re 

def valid_plates(plates):  
    result = ""
    for plate in plates:
        if re.fullmatch(r'', plate):
            result += f"{plate} -> válido\n"
        else:
            result += f"{plate} -> inválido\n"
    return result

def main():
    plates = [
        "AA-AA-AA", # inválida
        "LR-RB-32", # válida
        "1234LX", # inválida
        "PL 22 23", # válida
        "ZZ-99-ZZ", # válida
        "54-tb-34", # inválida
        "12 34 56", # inválida
        "42-HA BQ" # válida, mas inválida com o requisito extra
    ]

    print(valid_plates(plates))

if __name__ == "__main__":
    main()
