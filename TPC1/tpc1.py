import csv

from person import Person

def tpc1():

    people = list()

    with open('myheart.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            age = int(row[0])
            gender = row[1]
            pressure = int(row[2])
            cholesterol = int(row[3])
            beat = int(row[4])
            disease = bool(int(row[5]))

            people.append(Person(age, gender, pressure, cholesterol, beat, disease))

    # <--- Distribuição da doença por sexo ---

    disease_by_gender = {}

    def by_gender():
        for p in people:
            if p.gender not in disease_by_gender:
                disease_by_gender[p.gender] = {True: 0, False: 0}
            disease_by_gender[p.gender][p.disease] += 1

    def print_by_gender():
        for gender in disease_by_gender:
            total = sum(disease_by_gender[gender].values())
            true = disease_by_gender[gender][True]
            true_percent = (true / total) * 100
            false = disease_by_gender[gender][False]
            false_percent = (false / total) * 100
            if gender == 'M': 
                gender = 'Masculino'
            else: 
                gender = 'Feminino'
            print(f'{gender}: Com doença: {true}({true_percent:.2f}%), Sem doença: {false}({false_percent:.2f}%)')

    # --- Distribuição da doença por sexo ---/>



    # <--- Distribuição da doença por escalões etários ---
                
    disease_by_age = {}

    def by_age():
        age_min = 30
        age_max = max(int(p.age) for p in people)
        age_range = age_max - age_min
        age_group_size = 5
        num_age_groups = (age_range // age_group_size) + 1
       
        for i in range(num_age_groups):
            age_lower = age_min + i * age_group_size
            age_upper = age_min + (i + 1) * age_group_size 
            age_bound = (age_lower, age_upper)
            disease_by_age[age_bound] = {True: 0, False: 0}

            for p in people:
                age = p.age
                if age_lower <= age < age_upper:
                    disease = p.disease
                    disease_by_age[age_bound][disease] += 1

    def print_by_age():
        for age_bound in disease_by_age:
            age_group = f'{age_bound[0]}-{age_bound[1]}'
            total = sum(disease_by_age[age_bound].values())
            true = disease_by_age[age_bound][True]
            true_percent = (true / total) * 100
            false = disease_by_age[age_bound][False]
            false_percent = (false /total) * 100
            print(f'Escalão etário: {age_group} -> Com doença: {true}({true_percent:.2f}%), Sem doença: {false}({false_percent:.2f}%)')
            
    # --- Distribuição da doença por escalões etários ---/>



    # <--- Distribuição da doença por níveis de colestrol ---
    disease_by_cholesterol = {}

    def by_cholesterol():

        cholesterol_min = 9999 # cuidado extra porque o ficheiro .csv apresenta linhas em que o nível de colestrol é 0; essas linhas não vão ser consideradas nas estatísticas
        for p in people:
            if (p.cholesterol <= cholesterol_min) and (p.cholesterol != 0):
                cholesterol_min = p.cholesterol
        cholesterol_max = max(int(p.cholesterol) for p in people)
        cholesterol_range = cholesterol_max - cholesterol_min
        cholesterol_group_size = 10
        num_cholesterol_groups = (cholesterol_range // cholesterol_group_size) + 1

        print(cholesterol_min)
        print(cholesterol_max)
        print(num_cholesterol_groups)

        for i in range(num_cholesterol_groups):
            cholesterol_lower = cholesterol_min + i * cholesterol_group_size
            cholesterol_upper = cholesterol_min + (i + 1) * cholesterol_group_size 
            cholesterol_bound = (cholesterol_lower, cholesterol_upper)
            disease_by_cholesterol[cholesterol_bound] = {True: 0, False: 0}

            for p in people:
                if p.cholesterol!=0:
                    cholesterol = p.cholesterol
                    if cholesterol_lower <= cholesterol < cholesterol_upper:
                        disease = p.disease
                        disease_by_cholesterol[cholesterol_bound][disease] += 1

    def print_by_cholesterol():
        for cholesterol_bound in disease_by_cholesterol:
            cholesterol_group = f'{cholesterol_bound[0]}-{cholesterol_bound[1]}'
            total = sum(disease_by_cholesterol[cholesterol_bound].values())
            true = disease_by_cholesterol[cholesterol_bound][True]
            true_percent = (true / total) * 100
            false = disease_by_cholesterol[cholesterol_bound][False]
            false_percent = (false /total) * 100
            print(f'Escalão etário: {cholesterol_group} -> Com doença: {true}({true_percent:.2f}%), Sem doença: {false}({false_percent:.2f}%)')


    # --- Distribuição da doença por níveis de colestrol ---/>


    by_gender()
    print_by_gender()

    by_age()
    print_by_age()
   
    by_cholesterol()
    print_by_cholesterol()

tpc1()

