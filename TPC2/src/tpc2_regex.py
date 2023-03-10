import re

def main():

    def sum_string_digits(str):
        sum = 0
        for c in str:
            if c.isdigit():
                n = int(c)
                sum = sum + n

        return sum

    string = input("Insira o texto:\n> ")

    substrings = re.findall('(?i)(.+?)(off|on|=)', string)

    print(substrings) 
    
    sum = 0
    sum_flag = True

    for s in substrings:
        if sum_flag == True:
            sum += sum_string_digits(s[0])
            if s[1].lower() == 'off':
                sum_flag = False
            elif s[1] == '=':
                print("A soma das sequências de dígitos é: " + str(sum))
        if sum_flag == False:
            if s[1].lower() == 'on':
                sum_flag = True
            elif s[1] == '=':
                print("A soma das sequências de dígitos é: " + str(sum))

    # debug
    
   
if __name__ == "__main__":
    main()


