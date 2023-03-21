import re 

state = {
    "interacting" : False,
    "balance" : 0
}

# LEVANTAR 
def pick_up():
    if state['interacting']:
        print("maq: 'O telefone já se encontra em uso.'")
    else:
        state['interacting'] = True
        print("maq: 'Introduza moedas.'")

# POUSAR
def put_down():
    if state['interacting']:
        print(f"maq: 'troco={balance_to_string(state['balance'])} ; Volte sempre!'")
        state['interacting'] = False
    else:
        print("maq: 'O telefone não se encontra em uso.'")

# Auxiliares da MOEDA
def balance_to_string(balance):
    euros = int(balance)
    cents = round((balance - int(balance))*100)
    if euros != 0 and cents != 0:
        return f"{euros}e{cents}c"
    elif euros != 0:
        return f"{euros}e"
    else:
        return f"{cents}c"

def balance_to_double(balance): 
    euros_match = re.search(r"(\d+)e", balance)
    cents_match = re.search(r"(\d+)c", balance)
    if euros_match and cents_match:
        return int(euros_match.group(1)) + (int(cents_match.group(1))/100)
    elif euros_match:
        return int(euros_match.group(1))
    elif cents_match:
        return int(cents_match.group(1))/100
    
def validate_coin(coin):
    return re.match(r"(((1|2)e)|((1|2|5|10|20|50)c))", coin)

# MOEDA
def insert_coins(coins):
    invalid_coins = ""
    if state['interacting']:
        for coin in coins:
            if validate_coin(coin):
                state['balance'] += balance_to_double(coin)
            else:
                invalid_coins += f"{coin} - moeda inválida; "
        print(f"maq: '{invalid_coins}saldo = {balance_to_string(state['balance'])}'")
    else:
        print("maq: 'Não pode inserir moedas, visto que não se encontra numa interação.'")

#T=numero
def call(number):
    if state['interacting']:
        if re.fullmatch(r"\d{9}", number):
            if (number[0:3] == "601" or number[0:2] == "641"): # chamadas bloqueadas
                print("maq: 'A sua chamada foi _bloqueada_.'")
            if (number[0] == "2"): # chamadas nacionais
                if state['balance'] > 0.25:
                    state['balance'] -= 0.25
                    print(f"maq: 'saldo = {balance_to_string(state['balance'])}'")
                else:
                    print("maq: 'Não tem saldo suficiente para efetuar a chamada nacional.'")
            if number[0:3] == "800": # chamadas verdes
                print(f"maq: 'saldo = {balance_to_string(state['balance'])}'")
            if number[0:3] == "808": # chamadas azuis
                if state['balance'] > 0.10:
                    state['balance'] -= 0.10
                    print(f"maq: 'saldo = {balance_to_string(state['balance'])}'")
                else:
                    print("maq: 'Não tem saldo suficiente para efetuar a chamada azul.'")
            else: 
                print("maq: 'O número introduzido não é válido.")
        elif re.fullmatch(r"00\d{9}", number):
            if (number[0:2] == "00"): # chamadas internacionais
                if state['balance'] > 1.50:
                    state['balance'] -= 1.50
                    print(f"maq: 'saldo = {balance_to_string(state['balance'])}'")
                else:
                    print("maq: 'Não tem saldo suficiente para efetuar a chamada internacional.'")
            else:
                print("maq: 'O número introduzido não é válido.'")
        else:
            print("maq: 'O número introduzido não é válido.'")
    else:
        print("maq: 'Não pode efetuar chamadas, visto que não se encontra numa interação.'")

# ABORTAR
def abort(coins_string):
    if state['interacting']:
        print(f"maq: 'A interação foi abortada. Foram devolvidas as seguintes moedas: {coins_string}.'")
        state['balance'] = 0
        state['interacting'] = False
    else:
        print("maq: 'Não pode abortar, visto que não se encontra numa interação.'")


def main():
    coins_string = ""
    while True:
        line = input()
        if re.match(r"LEVANTAR", line):
            pick_up()
        elif re.match(r"POUSAR", line):
            put_down()
        elif re.match(r"MOEDA", line):
            coins_string = line[6:-1]
            coins = re.split(r"\s*,\s*", coins_string) # 10c, 20c, 1e, 2e.
            insert_coins(coins)
        elif re.match(r"T=", line):
            number = re.match(r"\d+", line[2:]) # 601181818
            call(number.group())   
        elif re.match(r"ABORTAR", line):
            abort(coins_string)
        else:
            print("Comando não reconhecido.")

if __name__ == '__main__':
    main()