import random
from datetime import date

def get_positive_integer(prompt="Digite um número inteiro positivo: "):
    """Obtém um inteiro positivo com validação"""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Por favor, digite um número positivo.")
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

def get_positive_float(prompt="Digite um número positivo: "):
    """Obtém um float positivo com validação"""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Por favor, digite um número positivo.")
        except ValueError:
            print("Por favor, digite um número válido.")

def get_gender(prompt="Digite o sexo (M/F): "):
    """Obtém entrada de gênero com validação"""
    while True:
        gender = input(prompt).strip().upper()
        if gender in ['M', 'F']:
            return gender
        else:
            print("Por favor, digite M para Masculino ou F para Feminino.")

def calculate_bmi(weight, height):
    """Calcula IMC e retorna classificação"""
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        classification = "Abaixo do peso"
    elif 18.5 <= bmi < 25:
        classification = "Peso ideal"
    elif 25 <= bmi < 30:
        classification = "Sobrepeso"
    elif 30 <= bmi <= 40:
        classification = "Obesidade"
    else:
        classification = "Obesidade mórbida"
    
    return bmi, classification

def is_leap_year(year):
    """Verifica se um ano é bissexto"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def can_form_triangle(side_a, side_b, side_c):
    """Verifica se três lados podem formar um triângulo"""
    return (side_a < side_b + side_c and 
            side_b < side_a + side_c and 
            side_c < side_a + side_b)

def get_triangle_type(side_a, side_b, side_c):
    """Determina o tipo de triângulo"""
    if side_a == side_b == side_c:
        return "EQUILÁTERO"
    elif side_a == side_b or side_b == side_c or side_a == side_c:
        return "ISÓSCELES"
    else:
        return "ESCALENO"

def calculate_age(birth_year):
    """Calcula idade baseada no ano de nascimento"""
    current_year = date.today().year
    return current_year - birth_year

def format_currency(amount, currency_symbol="R$"):
    """Formata valor como moeda"""
    return f"{currency_symbol} {amount:.2f}"

class Counter:
    """Classe contador flexível"""
    
    def __init__(self, start, end, increment=1):
        self.start = start
        self.end = end
        self.increment = increment
        
    def count(self):
        """Gera sequência de contagem"""
        if self.increment == 0:
            raise ValueError("Incremento não pode ser zero")
            
        current = self.start
        sequence = []
        
        if self.start <= self.end:
            while current <= self.end:
                sequence.append(current)
                current += abs(self.increment)
        else:
            while current >= self.end:
                sequence.append(current)
                current -= abs(self.increment)
                
        return sequence
    
    def display_count(self):
        """Exibe a sequência de contagem"""
        sequence = self.count()
        print("Contagem:", ' '.join(map(str, sequence)), "Acabou!")

class GradeCalculator:
    """Calculadora para notas de estudantes"""
    
    @staticmethod
    def calculate_average(*grades):
        """Calcula média das notas"""
        return sum(grades) / len(grades)
    
    @staticmethod
    def get_status(average):
        """Obtém situação do aluno baseada na média"""
        if average <= 4.9:
            return "REPROVADO"
        elif 5.0 <= average <= 6.9:
            return "RECUPERAÇÃO"
        else:
            return "APROVADO"
    
    @staticmethod
    def evaluate_student(student_name, *grades):
        """Avaliação completa do estudante"""
        average = GradeCalculator.calculate_average(*grades)
        status = GradeCalculator.get_status(average)
        
        print(f"\nAluno: {student_name}")
        print(f"Notas: {', '.join(map(str, grades))}")
        print(f"Média: {average:.2f}")
        print(f"Situação: {status}")
        
        return average, status
