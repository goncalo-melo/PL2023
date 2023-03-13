import re 

def valid_file_names(file_names):  
    result = ""
    for file_name in file_names:
        if re.fullmatch(r'[\w\-.]+\.(txt|docx|jpg)$', file_name):
            result += f"{file_name} -> válido\n"
        else:
            result += f"{file_name} -> inválido\n"
    return result

def valid_file_names_dict(file_names):
    valid_file_names = {}
    for file_name in file_names:
        match = re.fullmatch(r'[\w\-.]+\.(txt|docx|jpg)$', file_name)
        if match:
            extension = match.group(1)
            if extension not in valid_file_names:
                valid_file_names[extension] = [file_name]
            else:
                valid_file_names[extension].append(file_name)
    return valid_file_names

def main():
    file_names = [
        "document.txt", # válido
        "file name.docx", # inválido
        "image_001.jpg", # válido
        "script.sh.txt", # válido
        "test_file.txt", # válido
        "file_name.", # inválido
        "my_resume.docx", # válido
        ".hidden-file.txt", # válido
        "important-file.text file", # inválido
        "file%name.jpg" # inválido
    ]

    print(valid_file_names(file_names))
    print(valid_file_names_dict(file_names))

if __name__ == "__main__":
    main()
