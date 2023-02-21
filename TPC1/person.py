class Person:
    def __init__(self, age:int, gender:str, pressure:int, cholesterol:int, beat:int, disease:bool):
        self.age = age
        self.gender = gender
        self.pressure = pressure
        self.cholesterol = cholesterol
        self.beat = beat
        self.disease = disease

    def __str__(self):
        return f'Pessoa:\nIdade: {self.age}\ngender: {self.gender}\nTensão: {self.pressure}\ncholesterol: {self.cholesterol}\nbeat: {self.beat}\nTem Doença: {self.disease}\n'