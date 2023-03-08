import re
import json
from tabulate import tabulate

# <--- Frequência de processos por ano ---
def processes_frequency_per_year(processes):
    processes_per_year = {}

    for process in processes:
        year = process["year"]
        if year not in processes_per_year:
            processes_per_year[year] = 1
        else:
            processes_per_year[year] += 1

    headers = ['Ano', 'Nº de processos']
    data = []
    for year, count in processes_per_year.items():
        row = [year, count]
        data.append(row)
    data.sort(key=lambda x:x[0])

    print('================================') 
    print('Frequência de processos por ano:')
    print('================================') 
    print(tabulate(data, headers=headers), '\n')

    return processes_per_year
# --- Frequência de processos por ano ---/>


# <--- Frequência de nomes própios e apelidos por século (top 5) ---
def names_frequency_per_century(processes):
    first_names = {}
    last_names = {}

    for process in processes:
        first_name = re.match(r"\b[a-zA-Z]+\b", process["name"]).group()
        last_name = re.search(r"\b[a-zA-Z]+$", process["name"]).group()
        year = process["year"]
        century = (int(year) // 100) + 1

        if century not in first_names:
            first_names[century] = {}

        if century not in last_names:
            last_names[century] = {}

        if first_name not in first_names[century]:
            first_names[century][first_name] = 0

        if last_name not in last_names[century]:
            last_names[century][last_name] = 0

        first_names[century][first_name] += 1
        last_names[century][last_name] += 1

    header_first_names = ['Século', 'Top 5 nomes própios']
    data_first_names = []
    for century, names in first_names.items():
        items = list(names.items())
        items.sort(key=lambda x:x[1], reverse=True)
        row = [century, items[:5]]
        data_first_names.append(row)

    print('======================================') 
    print('Nomes próprios mais usados por século:')
    print('======================================') 
    print(tabulate(data_first_names, headers=header_first_names), '\n')

    header_last_names = ['Século', 'Top 5 apelidos']
    data_last_names = []
    for century, names in last_names.items():
        items = list(names.items())
        items.sort(key=lambda x:x[1], reverse=True)
        row = [century, items[:5]]
        data_last_names.append(row)

    print('================================') 
    print('Apelidos mais usados por século:')
    print('================================') 
    print(tabulate(data_last_names, headers=header_last_names), '\n')

    return first_names, last_names
# --- Frequência de nomes própios e apelidos por século (top 5) ---/>


# <--- Frequência dos vários tipos de relação ---
def relationships_frequency(processes):
    relationships = {}

    relationship_regex = re.compile(r"[a-zA-Z ]*,([a-zA-Z\s]*)\.[ ]*Proc\.\d+\.")

    for process in processes:
        observations = process["observations"]
        matches = relationship_regex.finditer(observations)

        for match in matches:
            if match.group(1) not in relationships:
                relationships[match.group(1)] = 0
            relationships[match.group(1)] += 1
    
    headers = ['Tipo de relação', 'Nº de relações']
    data = []
    for relationship, count in relationships.items():
        row = [relationship, count]
        data.append(row)
    data.sort(key=lambda x:x[1], reverse=True)

    print('========================================') 
    print('Frequência dos vários tipos de relações:')
    print('========================================') 
    print(tabulate(data, headers=headers), '\n')

    return relationships
# --- Frequência dos vários tipos de relação ---/>


# <--- Conversão para ficheiro Json ---
def processes_to_json(processes):
    file = open("../processes_20.json", "w")
    json.dump(processes[:20], file)
    file.close()
# --- Conversão para ficheiro Json ---/>


def main():
    file = open("../processos.txt", 'r')  # Pasta | Data | Nome | Pai | Mãe | Observações
    line_regex = re.compile(r"(?P<folder>\d+)::(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})::(?P<name>[a-zA-Z ]+)::(?P<father>[a-zA-Z ]+)::(?P<mother>[a-zA-Z ]+)::(?P<observations>.*)::")
    damaged_regex = re.compile(r"Doc.danificado.")
    matches = line_regex.finditer(file.read())
    processes = list()

    for match in matches:
        if not damaged_regex.search(match.group("observations")):
            processes.append(match.groupdict())

    opt = 0
    while opt != 5:
        print("===================================================================")
        print("Indique a ação pretendida:")
        print("1 - Frequência de processos por ano")
        print("2 - Frequência de nomes própios e apelidos por século (top 5)")
        print("3 - Frequência dos vários tipos de relação")
        print("4 - Converter os 20 primeiros registos num ficheiro em formato Json")
        print("5 - Sair")
        print("===================================================================")

        opt = int(input())

        if opt==1:
            processes_frequency_per_year(processes)
        elif opt==2:
            names_frequency_per_century(processes)
        elif opt==3:
            relationships_frequency(processes)
        elif opt==4:
            processes_to_json(processes)
        elif opt==5:
            print('Até à próxima!')
            exit()




if __name__ == '__main__':
    main()