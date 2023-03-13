import re
import json
from statistics import mean

def main():
    csv_filepath = input("Insira o nome do dataset csv: ")
    with open(csv_filepath) as csv_file:
        lines = csv_file.readlines()

    header_regex = re.compile(r'([^,{]+)(?:\{(\d+)(?:,(\d+))?\}(?:::(\w+))?)?[,]?')
    header_fields = header_regex.findall(lines[0].strip())

    header = []

    sizes = {}
    aggregation_functions = {}

    for i in range(0, len(header_fields)):
        field_name = header_fields[i][0]
        min_size = header_fields[i][1]
        max_size = header_fields[i][2]
        aggregation_function = header_fields[i][3]

        header.append(field_name)

        if aggregation_function != "":
            sizes[field_name] = (min_size, max_size)
            aggregation_functions[field_name] = aggregation_function
        elif min_size != '':
            sizes[field_name] = (min_size, max_size)

    data_regex = ""
    for field_name in header:
        if field_name in sizes:
            if sizes[field_name][1] != "":
                size = f"{{{int(sizes[field_name][0])},{int(sizes[field_name][1])}}}"
            else:
                size = f"{{{int(sizes[field_name][0])}}}"

            data_regex += rf"(?P<{field_name}>([^,]+[,]?){size})[,]?"
        else:
            data_regex += rf"(?P<{field_name}>[^,]+)[,]?"

    data_regex = re.compile(data_regex)

    data = []

    for line in lines[1:]:
        matches = data_regex.finditer(line.strip())
        data += [match.groupdict() for match in matches]

    for elem in data:
        for field_name in header:
            if field_name in sizes:
                elem[field_name] = [int(num) for num in re.findall(r'\d+', elem[field_name])]
            if field_name in aggregation_functions:
                if aggregation_functions[field_name] == "sum":
                    elem[field_name] = sum(elem[field_name])
                elif aggregation_functions[field_name] == "media":
                    elem[field_name] = mean(elem[field_name])

    print(csv_filepath.replace('.csv', '.json'))
    with open(csv_filepath.replace(".csv", ".json"), "w") as json_file:
        json.dump(data, json_file, indent=len(header), ensure_ascii=False)

if __name__ == '__main__':
    main()

