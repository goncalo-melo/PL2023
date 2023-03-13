import re 

def names_converter(string):  
    return re.sub(
        r'(?P<first_name>\b[A-Z]\w+\b)\ (((\b[A-Z]\w+\b)|(\b(?i:(de|dos?|das?))\b))\ )+(?P<last_name>\b[A-Z]\w+\b)',
        r'\g<last_name>, \g<first_name>',
        string
    )

def main():
    texto = """Este texto foi feito por Sofia Guilherme Rodrigues dos Santos, com 
base no texto original de Pedro Rafael Paiva Moura, com a ajuda
dos professores Pedro Rangel Henriques e José João Antunes Guimarães Dias De Almeida.
Apesar de partilharem o mesmo apelido, a Sofia não é da mesma família do famoso
autor José Rodrigues dos Santos."""


    print(names_converter(texto))

if __name__ == "__main__":
    main()
