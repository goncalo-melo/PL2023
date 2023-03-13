import re 

def iso_8601(string):  
    return re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\3-\2-\1', string)

    # alternativa 1
    # re.sub(r'(\d{2})/l(\d{2})/(\d{4})', lambda x : f"{x[3]}-{x[2]}-{x[1]}", t)

    # alternativa 2
    # re.sub(r'(?P<dia>\d{2})/(?P<mes>\d{2})/(?P<ano>\d{4})', r'\g<ano>-\g<mes>-\g<dia>', t)

    # alternativa 3
    # def converte_data(m:re.match) -> str:
    #     return f"{m.group('ano')}-{m.group('mes')}-{m.group('dia')}"

    # re.sub(r'(?P<dia>\d{2})/(?P<mes>\d{2})/(?P<ano>\d{4})', converte_data, t)

def main():
    texto = """A 03/01/2022, Pedro viajou para a praia com a sua família.
Eles ficaram hospedados num hotel e aproveitaram o sol e o mar durante toda a semana.
Mais tarde, no dia 12/01/2022, Pedro voltou para casa e começou a trabalhar num novo projeto.
Ele passou muitas horas no escritório, mas finalmente terminou o projeto a 15/01/2022."""

    print(iso_8601(texto))

if __name__ == "__main__":
    main()
