import re 

def repetitions_removal(string):  
    repeated_words = re.findall(r'\b(\w+)\b(?=.*\b\1\b)', string)

    for word in repeated_words:
        string = re.sub(word, '', string)

    return string
        
def main():
    texto = """This is a sample text text with repeated words, sample words, and more words."""

    print(repetitions_removal(texto))

if __name__ == "__main__":
    main()
