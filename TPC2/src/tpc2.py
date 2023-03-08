def main():

    def sum_string_digits(str):
        sum = 0
        for c in str:
            if c.isdigit():
                n = int(c)
                sum = sum + n

        return sum   

    string = input("Insira o texto:\n> ")

    sum_flag = True
    digits = ""

    for i, c in enumerate(string):
        if sum_flag == True:
            if c.isdigit():
                digits += c
            elif c in ['o', 'O'] and string[i : i+3].lower() == 'off':
                sum_flag = False   
            elif c == '=':
                print("A soma das sequências de dígitos é: " + str(sum_string_digits(digits)))
        if sum_flag == False:
            if c in ['o', 'O'] and string[i : i+2].lower() == 'on':
                sum_flag = True
            elif c == '=':
                print("A soma das sequências de dígitos é: " + str(sum_string_digits(digits)))

if __name__ == "__main__":
    main()


