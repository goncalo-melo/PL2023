import re 
import sys

# Ficha 1

def main():
    # - 1 - 
    line1 = "hello world"
    line2 = "goodbye world"
    line3 = "hi, hello there"
    line4 = "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"
    line5 = "bananas, laranjas, maçãs, uvas, melancias, cerejas, kiwis, etc."

    # 1.1.
    def one_dot_one(line):
        if(re.match(r'hello', line)):
            print("A palavra \"hello\" aparece no ínicio da linha.")
            return True
        else:
            print("A palavra \"hello\" não aparece no ínicio da linha.")
            return False
        
    # 1.2.
    def one_dot_two(line):
        if(re.search(r'hello', line)):
            print("A palavra \"hello\" aparece na linha.")
            return True
        else:
            print("A palavra \"hello\" não aparece na linha.")
            return False

    # 1.3.
    def one_dot_three(line):
        print(f"As occorências da palavra \"hello\", quer seja escrita com maiúsculas ou minúsculas, são:\n->", {re.findall(r'(?i:hello)', line)}) # equivalente a re.findall(r'hello', linha, flags=re.I)

    # 1.4.
    def one_dot_four(line):
        print(f"A linha após as substituições das occorências da palavra \"hello\" por \"*YEP*\" é:\n->", {re.sub(r'(?i:hello)', '*YEP*', line)}) 

    # 1.5.
    def one_dot_five(line):
        print(f"A lista dos items separados por vírgula é:\n->", re.split(r'\s*,\s*', line))


    # - 2 - 
    phrase1 = "Posso ir à casa de banho, por favor?"
    phrase2 = "Preciso de um favor."

    def palavra_magica(phrase):
        if(re.search(r'(por favor[.!?])$', phrase)):
            print(f"A frase termina com a expressão \"por favor\".")
            return True
        else: 
            print(f"A frase não termina com a expressão \"por favor\".")
            return False
    
    # - 3 -
    line6 = "Eu não sei se eu quero continuar a ser eu. Por outro lado, eu ser eu é uma parte importante de quem EU sou."

    def narcissismo(line):
        eu_list = re.findall(r'\b(?i:eu)\b', line)
        return len(eu_list)
   
    # - 4 -
    line7 = "LEI é o melhor curso! Adoro LEI! Gostar de LEI devia ser uma lei."

    def troca_de_curso(line, new_course):
        return re.sub(r'LEI', new_course, line)

    # - 5 -
    line8 = "4,-6,2,3,8,-3,0,2,-5,1"
    
    def soma_string(line):
        nums_string_list = re.split(r',', line)
        nums_list = list()
        for num in nums_string_list:
            num = int(num)
            nums_list.append(num)
        return sum(nums_list)

    # - 6 -
    phrase3 = "Eu sou o rei delas e ninguém, nem mesmo tu, me pode impedir de sair com os meus bros. Porque eles before elas!"

    def pronomes(phrase):
        return re.findall(r'\b(eu|tu|eles?|elas?|nós|vós)\b', phrase, flags=re.I)

    # - 7 -
    variable_string = "a_nice_variable"

    def variavel_valida(string):
        if(re.match(r'[a-zA-Z]\w*', string)):
            return True
        else:
            return False

    # - 8 -
    integer_string = "isto é uma string123 para teste -456 engraçada 2 que testa 67 inteiros -89."

    def inteiros(string):
        return re.findall(r'[\+-]?\d+', string)
            
    # - 9 -
    spaces_string = "esta string      tem                   demasiados    espaços para o meu gosto!"        

    def underscores(string):
        return re.sub(r'\s+', '_', string)

    # - 10 -
    postal_codes_list = [
    "4700-000",
    "1234-567",
    "8541-543",
    "4123-974",
    "9481-025"
    ]

    def codigos_postais(list):
        pairs_list = []
        pair_regex = re.compile(r'(\d{4})-(\d{3})')

        for item in list:
            pair = (pair_regex.match(item).groups())
            pairs_list.append(pair)

        return pairs_list
    
    #print(one_dot_one())
    #print(one_dot_two())
    #print(one_dot_three())
    #print(one_dot_four())
    #print(one_dot_five())
    #print(palavra_magica())
    #print(narcissismo())
    #print(troca_de_curso())
    #print(soma_string())
    #print(pronomes())
    #print(variavel_valida())
    #print(inteiros())
    #print(underscores())
    print(codigos_postais(postal_codes_list))

if __name__ == "__main__":
    main()
