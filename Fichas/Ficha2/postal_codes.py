import re 

def postal_codes(postal_codes_list):  
    pairs_list = []

    for postal_code in postal_codes_list:
        match = re.match(r'(\d{4})-(\d{3})', postal_code) 
        if match:
            pair = match.groups()
            pairs_list.append(pair)

    return pairs_list

def main():
    postal_codes_list = [
        "4700-000", # válido
        "9876543", # inválido
        "1234-567", # válido
        "8x41-5a3", # inválido
        "84234-12", # inválido
        "4583--321", # inválido
        "9481-025" # válido
    ]   

    print(postal_codes(postal_codes_list))

if __name__ == "__main__":
    main()
