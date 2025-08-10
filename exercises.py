from datetime import date
import random

def exercise_01():
    print("Olá, Mundo!")

def exercise_02():
    name = input("Qual é o seu nome? ")
    print(f"Olá {name}, é um prazer te conhecer!")

def exercise_03():
    employee_name = input("Digite o nome do funcionário: ")
    employee_salary = float(input("Digite o salário do funcionário: "))
    print(f"O funcionário {employee_name} tem um salário de R$ {employee_salary:.2f} em junho.")

def exercise_04():
    number_1 = int(input("Digite um número: "))
    number_2 = int(input("Digite outro número: "))
    result = number_1 + number_2
    print(f"A soma entre {number_1} e {number_2} é igual a {result}.")
    
def exercise_05():
    grade_1 = float(input("Digite a primeira nota: "))
    grade_2 = float(input("Digite a segunda nota: "))
    average = (grade_1 + grade_2) / 2
    print(f"A média entre {grade_1} e {grade_2} é igual a {average:.2f}")
    
def exercise_06():
    number = int(input("Digite um número: "))
    predecessor = number - 1
    successor = number + 1
    print(f"O antecessor de {number} é {predecessor}")
    print(f"O sucessor de {number} é {successor}")
    
def exercise_07():
    number = float(input("Digite um número: "))
    double = number * 2
    third_part = number / 3
    print(f"O dobro de {number} é {double:.2f}")
    print(f"A terça parte de {number} é {third_part:.5f}")

def exercise_08():
    distance_meters = float(input("Digite uma distância em metros: "))
    print(f"A distância de {distance_meters}m corresponde a:")
    print(f"{distance_meters / 1000:.5f}Km")
    print(f"{distance_meters / 100:.2f}Hm")
    print(f"{distance_meters / 10:.1f}Dam")
    print(f"{distance_meters * 10:.1f}dm")
    print(f"{distance_meters * 100:.1f}cm")
    print(f"{distance_meters * 1000:.1f}mm")

def exercise_09():
    real_amount = float(input("Digite quanto dinheiro você tem na carteira (em R$): "))
    usd_rate = 3.45
    dollar_amount = real_amount / usd_rate
    print(f"Você pode comprar US${dollar_amount:.2f}")

def exercise_10():
    width_cm = float(input("Digite a largura da parede em centímetros: "))
    height_cm = float(input("Digite a altura da parede em centímetros: "))
    width_m = width_cm / 100
    height_m = height_cm / 100
    area = width_m * height_m
    paint_needed = area / 2
    print(f"A área a ser pintada será {area:.2f}m² precisando de {paint_needed:.2f} litros de tinta.")

def exercise_11():
    value_a = float(input("Digite o valor de A: "))
    value_b = float(input("Digite o valor de B: "))
    value_c = float(input("Digite o valor de C: "))
    delta = (value_b ** 2) - 4 * value_a * value_c
    print(f"{delta} é o valor de Delta.")
    
def exercise_12():
    price = float(input("Digite o preço do produto: "))
    promotional_price = price * 0.95
    print(f"O preço promocional deste produto é: R$ {promotional_price:.2f}")

def exercise_13():
    current_salary = float(input("Digite o seu salário: "))
    new_salary = current_salary * 1.15
    print(f"Seu novo salário é: R$ {new_salary:.2f}")
    
def exercise_14():
    kilometers = float(input("Digite quantos quilômetros foram percorridos: "))
    rental_days = float(input("Digite quantos dias foram alugados: "))
    daily_rate = 90
    km_rate = 0.20
    total_cost = (kilometers * km_rate) + (rental_days * daily_rate)
    print(f"O preço total a pagar é: R$ {total_cost:.2f}")
    
def exercise_15():
    work_days = int(input("Digite quantos dias foram trabalhados: "))
    daily_wage = 25 * 8
    salary = work_days * daily_wage
    print(f"O seu salário é: R$ {salary:.2f}")
    
def exercise_16():
    cigarettes_per_day = int(input("Digite quantos cigarros você fuma por dia: "))
    years_smoking = int(input("Digite quantos anos você fuma: "))
    minutes_lost_per_cigarette = 10
    total_minutes_lost = cigarettes_per_day * 365 * years_smoking * minutes_lost_per_cigarette
    days_lost = total_minutes_lost / 1440
    print(f"Esse é o total de dias de vida que você perdeu: {days_lost:.2f}")
    
def exercise_17():
    car_speed = int(input("Qual a velocidade do carro? "))
    speed_limit = 80
    
    if car_speed > speed_limit:
        excess_speed = car_speed - speed_limit
        fine = excess_speed * 5
        print(f"Você foi multado! Valor da multa: R$ {fine:.2f}")
    else:
        print("Você está dentro do limite de velocidade.")
    
def exercise_18():
    birth_year = int(input("Digite o ano de nascimento: "))
    current_year = date.today().year
    age = current_year - birth_year
    
    if age < 16:
        print("Você NÃO pode votar.")
    elif 16 <= age < 18 or age > 70:
        print("O voto é OPCIONAL.")
    else:
        print("O voto é OBRIGATÓRIO.")
        
def exercise_19():
    student_name = input("Digite o nome do aluno: ")
    grade_1 = float(input("Digite a primeira nota: "))
    grade_2 = float(input("Digite a segunda nota: "))
    average = (grade_1 + grade_2) / 2

    print(f"\nAluno: {student_name}")
    print(f"Notas: {grade_1} e {grade_2}")
    print(f"Média: {average:.2f}")

    if average >= 7.0:
        print("Situação: Bom aproveitamento!")
    else:
        print("Situação: Aproveitamento insuficiente.")
        
def exercise_20():
    number = int(input("Digite um número inteiro: "))

    if number % 2 == 0:
        print(f"O número {number} é PAR.")
    else:
        print(f"O número {number} é ÍMPAR.")
    
def exercise_21():
    year = int(input("Digite um ano: "))

    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    if is_leap:
        print(f"O ano {year} é BISSEXTO.")
    else:
        print(f"O ano {year} NÃO é bissexto.")
    
def exercise_22():
    birth_year = int(input("Digite o ano de nascimento: "))
    current_year = date.today().year
    age = current_year - birth_year
    enlistment_age = 18

    print(f"Você tem {age} anos.")

    if age < enlistment_age:
        years_remaining = enlistment_age - age
        enlistment_year = current_year + years_remaining
        print(f"Ainda faltam {years_remaining} ano(s) para o alistamento.")
        print(f"Seu alistamento será em {enlistment_year}.")
    elif age == enlistment_age:
        print("Você deve se alistar este ano!")
    else:
        years_overdue = age - enlistment_age
        past_enlistment_year = current_year - years_overdue
        print(f"Você já deveria ter se alistado há {years_overdue} ano(s).")
        print(f"Seu alistamento foi em {past_enlistment_year}.")
    
def exercise_23():
    customer_name = input("Digite o nome do cliente: ")
    gender = input("Digite o sexo (M/F): ").strip().upper()
    purchase_amount = float(input("Digite o valor das compras: R$ "))

    if gender == "M":
        discount_rate = 0.05
    elif gender == "F":
        discount_rate = 0.13
    else:
        discount_rate = 0
        
    discounted_price = purchase_amount * (1 - discount_rate)

    print(f"\nCliente: {customer_name}")
    print(f"Sexo: {gender}")
    print(f"Valor original: R$ {purchase_amount:.2f}")
    print(f"Valor com desconto: R$ {discounted_price:.2f}")
    
def exercise_24():
    distance = float(input("Digite a distância que deseja percorrer (em km): "))

    if distance <= 200:
        price_per_km = 0.50
    else:
        price_per_km = 0.45
        
    total_price = distance * price_per_km

    print(f"Distância: {distance:.1f} km")
    print(f"Preço da passagem: R$ {total_price:.2f}")
    
def exercise_25():
    segment_a = float(input("Digite o comprimento do primeiro segmento: "))
    segment_b = float(input("Digite o comprimento do segundo segmento: "))
    segment_c = float(input("Digite o comprimento do terceiro segmento: "))

    can_form_triangle = (segment_a < segment_b + segment_c and 
                        segment_b < segment_a + segment_c and 
                        segment_c < segment_a + segment_b)

    if can_form_triangle:
        print("Os segmentos podem formar um triângulo!")
    else:
        print("Os segmentos NÃO podem formar um triângulo.")

def exercise_26():
    number_1 = int(input("Digite o primeiro número: "))
    number_2 = int(input("Digite o segundo número: "))
    
    if number_1 > number_2:
        print("O primeiro valor é o maior")
    elif number_2 > number_1:
        print("O segundo valor é o maior")
    else:
        print("Não existe valor maior, os dois são iguais")

def exercise_27():
    grade_1 = float(input("Digite a primeira nota: "))
    grade_2 = float(input("Digite a segunda nota: "))
    average = (grade_1 + grade_2) / 2
    
    print(f"Média: {average:.1f}")
    
    if average <= 4.9:
        print("REPROVADO")
    elif 5.0 <= average <= 6.9:
        print("RECUPERAÇÃO")
    else:
        print("APROVADO")

def exercise_28():
    width = float(input("Digite a largura do terreno (m): "))
    length = float(input("Digite o comprimento do terreno (m): "))
    area = width * length
    
    print(f"Área do terreno: {area:.2f} m²")
    
    if area < 100:
        print("TERRENO POPULAR")
    elif 100 <= area <= 500:
        print("TERRENO MASTER")
    else:
        print("TERRENO VIP")

def exercise_29():
    employee_name = input("Digite o nome do funcionário: ")
    current_salary = float(input("Digite o salário (R$): "))
    years_of_service = int(input("Quantos anos na empresa: "))
    
    if years_of_service <= 3:
        increase_rate = 0.03
    elif 3 < years_of_service < 10:
        increase_rate = 0.125
    else:
        increase_rate = 0.20
        
    new_salary = current_salary * (1 + increase_rate)
    
    print(f"Funcionário: {employee_name}")
    print(f"Salário antigo: R$ {current_salary:.2f}")
    print(f"Novo salário: R$ {new_salary:.2f} (aumento de {increase_rate*100:.1f}%)")

def exercise_30():
    side_a = float(input("Digite o comprimento do 1º segmento: "))
    side_b = float(input("Digite o comprimento do 2º segmento: "))
    side_c = float(input("Digite o comprimento do 3º segmento: "))
    
    can_form_triangle = (side_a < side_b + side_c and 
                        side_b < side_a + side_c and 
                        side_c < side_a + side_b)
    
    if can_form_triangle:
        print("Os segmentos podem formar um triângulo!")
        
        if side_a == side_b == side_c:
            print("Tipo: EQUILÁTERO")
        elif side_a == side_b or side_b == side_c or side_a == side_c:
            print("Tipo: ISÓSCELES")
        else:
            print("Tipo: ESCALENO")
    else:
        print("Os segmentos NÃO podem formar um triângulo.")

def exercise_31():
    choices = {'1': 'Pedra', '2': 'Papel', '3': 'Tesoura'}
    computer_choice = random.choice(['1', '2', '3'])
    player_choice = input("Escolha: 1-Pedra 2-Papel 3-Tesoura: ").strip()
    
    if player_choice not in choices:
        print("Opção inválida.")
        return
        
    print(f"Você: {choices[player_choice]} x Computador: {choices[computer_choice]}")
    
    if player_choice == computer_choice:
        print("Empate!")
    elif (player_choice, computer_choice) in [('1', '3'), ('2', '1'), ('3', '2')]:
        print("Você venceu!")
    else:
        print("Você perdeu.")

def exercise_32():
    target_number = random.randint(1, 5)
    guess = int(input("Tente adivinhar o número (1-5): "))
    
    if guess == target_number:
        print("Acertou!")
    else:
        print(f"Errou! Eu escolhi {target_number}")

def exercise_33():
    house_value = float(input("Valor da casa (R$): "))
    buyer_salary = float(input("Salário do comprador (R$): "))
    payment_years = int(input("Quantos anos para pagar: "))
    
    total_payments = payment_years * 12
    monthly_payment = house_value / total_payments
    max_payment = 0.3 * buyer_salary
    
    if monthly_payment <= max_payment:
        print(f"Empréstimo aprovado! Prestação = R$ {monthly_payment:.2f} em {total_payments}x")
    else:
        print(f"Empréstimo NEGADO. Prestação R$ {monthly_payment:.2f} excede 30% do salário.")

def exercise_34():
    weight = float(input("Digite o peso (kg): "))
    height = float(input("Digite a altura (m): "))
    bmi = weight / (height ** 2)
    
    print(f"IMC = {bmi:.2f}")
    
    if bmi < 18.5:
        print("Abaixo do peso")
    elif 18.5 <= bmi < 25:
        print("Peso ideal")
    elif 25 <= bmi < 30:
        print("Sobrepeso")
    elif 30 <= bmi <= 40:
        print("Obesidade")
    else:
        print("Obesidade mórbida")

def exercise_35():
    car_type = input("Tipo do carro (P-popular / L-luxo): ").strip().upper()
    rental_days = int(input("Quantos dias alugado: "))
    kilometers = float(input("Quantos km percorridos: "))
    
    if car_type == 'P':
        daily_rate = 90
        km_rate = 0.20 if kilometers <= 100 else 0.10
    elif car_type == 'L':
        daily_rate = 150
        km_rate = 0.30 if kilometers <= 200 else 0.25
    else:
        print("Tipo inválido.")
        return
        
    total_cost = daily_rate * rental_days + km_rate * kilometers
    print(f"Total a pagar: R$ {total_cost:.2f}")

def exercise_36():
    activity_hours = float(input("Quantas horas de atividade no mês: "))
    
    if activity_hours <= 10:
        points = activity_hours * 2
    elif activity_hours <= 20:
        points = activity_hours * 5
    else:
        points = activity_hours * 10
        
    earnings = points * 0.05
    print(f"Pontos: {points:.1f} -> Valor ganho: R$ {earnings:.2f}")

def exercise_37():
    current_salary = float(input("Salário atual (R$): "))
    gender = input("Gênero (M/F): ").strip().upper()
    years_of_service = int(input("Anos de empresa: "))
    
    if gender == 'F':
        if years_of_service < 15:
            increase_rate = 0.05
        elif 15 <= years_of_service <= 20:
            increase_rate = 0.12
        else:
            increase_rate = 0.23
    elif gender == 'M':
        if years_of_service < 20:
            increase_rate = 0.03
        elif 20 <= years_of_service <= 30:
            increase_rate = 0.13
        else:
            increase_rate = 0.25
    else:
        print("Gênero inválido. Use M ou F.")
        return
        
    new_salary = current_salary * (1 + increase_rate)
    print(f"Novo salário: R$ {new_salary:.2f} (aumento de {increase_rate*100:.1f}%)")

def exercise_38():
    for i in range(6, 12):
        print(i, end=' ')
    print("Acabou!")

def exercise_39():
    for i in range(10, 2, -1):
        print(i, end=' ')
    print("Acabou!")

def exercise_40():
    for i in range(0, 19, 3):
        print(i, end=' ')
    print("Acabou!")

def exercise_41():
    for i in range(100, -1, -5):
        print(i, end=' ')
    print("Acabou!")

def exercise_42():
    value = int(input("Digite um número inteiro e positivo: "))
    print("Contagem:", end=' ')
    for i in range(1, value + 1):
        print(i, end=' ')
    print("Acabou!")

def exercise_43():
    for i in range(30, 0, -1):
        if i % 4 == 0:
            print(f"[{i}]", end=' ')
        else:
            print(i, end=' ')
    print("Acabou!")

def exercise_44():
    start = int(input("Digite o primeiro valor: "))
    end = int(input("Digite o último valor: "))
    increment = int(input("Digite o incremento: "))
    
    if increment == 0:
        print("Incremento não pode ser zero.")
        return
        
    print("Contagem:", end=' ')
    current = start
    
    if start <= end:
        while current <= end:
            print(current, end=' ')
            current += increment
    else:
        while current >= end:
            print(current, end=' ')
            current -= abs(increment)
    print("Acabou!")

def exercise_45():
    start = int(input("Digite o primeiro valor: "))
    end = int(input("Digite o último valor: "))
    increment = int(input("Digite o incremento: "))
    
    if increment == 0:
        print("Incremento não pode ser zero.")
        return
        
    print("Contagem:", end=' ')
    
    if start <= end:
        current = start
        while current <= end:
            print(current, end=' ')
            current += abs(increment)
    else:
        current = start
        while current >= end:
            print(current, end=' ')
            current -= abs(increment)
    print("Acabou!")

def exercise_46():
    total = sum(range(6, 101, 2))
    print(f"Resultado da soma: {total}")

def exercise_47():
    total = sum(range(500, -1, -50))
    print(f"Resultado da expressão: {total}")

def exercise_48():
    total = 0
    for i in range(7):
        number = int(input(f"Digite o {i+1}º número inteiro: "))
        total += number
    print(f"Somatório: {total}")

def exercise_49():
    even_count = 0
    odd_count = 0
    
    for i in range(6):
        number = int(input(f"Digite o {i+1}º número inteiro: "))
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
            
    print(f"Pares: {even_count} | Ímpares: {odd_count}")

def exercise_50():
    random_numbers = [random.randint(0, 10) for _ in range(20)]
    above_5 = sum(1 for x in random_numbers if x > 5)
    divisible_by_3 = sum(1 for x in random_numbers if x % 3 == 0)
    
    print("Números sorteados:", random_numbers)
    print(f"Quantidade acima de 5: {above_5}")
    print(f"Quantidade divisíveis por 3: {divisible_by_3}")

def exercise_51():
    prices = []
    for i in range(8):
        price = float(input(f"Preço do {i+1}º produto (R$): "))
        prices.append(price)
    print(f"Maior preço: R$ {max(prices):.2f}")
    print(f"Menor preço: R$ {min(prices):.2f}")

def exercise_52():
    ages = []
    for i in range(10):
        age = int(input(f"Idade da {i+1}ª pessoa: "))
        ages.append(age)
    
    average = sum(ages) / len(ages)
    above_18 = sum(1 for age in ages if age > 18)
    below_5 = sum(1 for age in ages if age < 5)
    max_age = max(ages)
    
    print(f"Média: {average:.1f}")
    print(f"Pessoas com mais de 18 anos: {above_18}")
    print(f"Pessoas com menos de 5 anos: {below_5}")
    print(f"Maior idade lida: {max_age}")

def exercise_53():
    ages = []
    men_count = 0
    women_count = 0
    total_age = 0
    men_age_sum = 0
    men_registered = 0
    women_above_20 = 0
    
    for i in range(5):
        age = int(input(f"Idade da {i+1}ª pessoa: "))
        gender = input("Sexo (M/F): ").strip().upper()
        
        ages.append(age)
        total_age += age
        
        if gender == 'M':
            men_count += 1
            men_age_sum += age
            men_registered += 1
        elif gender == 'F':
            women_count += 1
            if age > 20:
                women_above_20 += 1
    
    average = total_age / 5
    men_average = (men_age_sum / men_registered) if men_registered > 0 else 0
    
    print(f"Homens cadastrados: {men_count}")
    print(f"Mulheres cadastradas: {women_count}")
    print(f"Média de idade do grupo: {average:.1f}")
    if men_registered > 0:
        print(f"Média de idade dos homens: {men_average:.1f}")
    else:
        print("Nenhum homem cadastrado para média")
    print(f"Mulheres com mais de 20 anos: {women_above_20}")

def exercise_54():
    heights = []
    above_90kg = 0
    below_50kg_160cm = 0
    above_190cm_100kg = 0
    
    for i in range(7):
        weight = float(input(f"Peso da {i+1}ª pessoa (kg): "))
        height = float(input(f"Altura da {i+1}ª pessoa (m): "))
        heights.append(height)
        
        if weight > 90:
            above_90kg += 1
        if weight < 50 and height < 1.60:
            below_50kg_160cm += 1
        if height > 1.90 and weight > 100:
            above_190cm_100kg += 1
    
    height_average = sum(heights) / len(heights)
    
    print(f"Média de altura: {height_average:.2f} m")
    print(f"Pessoas com mais de 90kg: {above_90kg}")
    print(f"Pessoas com menos de 50kg e menos de 1.60m: {below_50kg_160cm}")
    print(f"Pessoas com mais de 1.90m e mais de 100kg: {above_190cm_100kg}")

def exercise_55():
    target = random.randint(1, 10)
    attempts = 4
    won = False
    
    for attempt in range(attempts):
        guess = int(input(f"Tentativa {attempt+1}/{attempts} - Escolha (1-10): "))
        if guess == target:
            print("Acertou!")
            won = True
            break
        else:
            print("Errado.")
    
    if not won:
        print(f"Suas tentativas acabaram. Eu escolhi {target}")

def exercise_56():
    total = 0
    while True:
        number = int(input("Digite um número (1111 para parar): "))
        if number == 1111:
            break
        total += number
    print(f"Somatório dos valores: {total}")

def exercise_57():
    men_total = 0.0
    women_total = 0.0
    
    while True:
        salary = float(input("Salário (R$): "))
        gender = input("Sexo (M/F): ").strip().upper()
        
        if gender == 'M':
            men_total += salary
        elif gender == 'F':
            women_total += salary
        else:
            print("Sexo inválido, registro não somado.")
        
        continue_input = input("Deseja continuar? (S/N): ").strip().upper()
        if continue_input == 'N':
            break
    
    print(f"Total pago a homens: R$ {men_total:.2f}")
    print(f"Total pago a mulheres: R$ {women_total:.2f}")

def exercise_58():
    ages = []
    while True:
        age = int(input("Digite a idade (999 para parar): "))
        if age == 999:
            break
        ages.append(age)
    
    total_students = len(ages)
    average = sum(ages) / total_students if total_students > 0 else 0
    
    print(f"Quantidade de alunos: {total_students}")
    print(f"Média de idade: {average:.1f}")

def exercise_59():
    max_age = 0
    men_count = 0
    youngest_woman_age = None
    men_age_sum = 0
    men_registered = 0
    
    while True:
        gender = input("Sexo (M/F) [ou ENTER para parar]: ").strip().upper()
        if gender == '':
            break
        
        age = int(input("Idade: "))
        
        if age > max_age:
            max_age = age
        
        if gender == 'M':
            men_count += 1
            men_age_sum += age
            men_registered += 1
        elif gender == 'F':
            if youngest_woman_age is None or age < youngest_woman_age:
                youngest_woman_age = age
        
        continue_input = input("Continuar? (S/N): ").strip().upper()
        if continue_input == 'N':
            break
    
    men_average = (men_age_sum / men_registered) if men_registered > 0 else 0
    
    print(f"Maior idade lida: {max_age}")
    print(f"Homens cadastrados: {men_count}")
    print(f"Idade da mulher mais jovem: {youngest_woman_age if youngest_woman_age is not None else 'Nenhuma mulher cadastrada'}")
    if men_registered > 0:
        print(f"Média de idade entre os homens: {men_average:.1f}")
    else:
        print("Nenhum homem cadastrado")

def exercise_60():
    names = []
    ages = []
    genders = []
    
    while True:
        name = input("Nome (ENTER para parar): ").strip()
        if name == '':
            break
        
        age = int(input("Idade: "))
        gender = input("Sexo (M/F): ").strip().upper()
        
        names.append(name)
        ages.append(age)
        genders.append(gender)
        
        continue_input = input("Continuar? (S/N): ").strip().upper()
        if continue_input == 'N':
            break
    
    if len(ages) == 0:
        print("Nenhum dado cadastrado.")
        return
    
    oldest_index = ages.index(max(ages))
    oldest_name = names[oldest_index]
    
    youngest_woman_age = None
    youngest_woman_name = None
    for name, age, gender in zip(names, ages, genders):
        if gender == 'F':
            if youngest_woman_age is None or age < youngest_woman_age:
                youngest_woman_age = age
                youngest_woman_name = name
    
    average = sum(ages) / len(ages)
    men_above_30 = sum(1 for age, gender in zip(ages, genders) if gender == 'M' and age > 30)
    women_below_18 = sum(1 for age, gender in zip(ages, genders) if gender == 'F' and age < 18)
    
    print(f"Nome da pessoa mais velha: {oldest_name}")
    print(f"Nome da mulher mais jovem: {youngest_woman_name if youngest_woman_name else 'Nenhuma mulher cadastrada'}")
    print(f"Média de idade do grupo: {average:.1f}")
    print(f"Homens com mais de 30 anos: {men_above_30}")
    print(f"Mulheres com menos de 18 anos: {women_below_18}")

def exercise_61():
    i = 0
    while True:
        print(i, end=' ')
        if i >= 30:
            break
        i += 3
    print("Acabou!")

def exercise_62():
    count = 0
    total = 0
    above_21 = 0
    
    while True:
        age = int(input("Digite uma idade: "))
        count += 1
        total += age
        if age >= 21:
            above_21 += 1
        
        continue_input = input("Continuar? (S/N): ").strip().upper()
        if continue_input == 'N':
            break
    
    average = total / count if count > 0 else 0
    
    print(f"Quantidade de idades digitadas: {count}")
    print(f"Média das idades: {average:.1f}")
    print(f"Pessoas com 21 anos ou mais: {above_21}")

def exercise_63():
    total = 0
    count = 0
    minimum = None
    even_count = 0
    
    while True:
        number = int(input("Digite um número: "))
        total += number
        count += 1
        
        if minimum is None or number < minimum:
            minimum = number
        
        if number % 2 == 0:
            even_count += 1
        
        continue_input = input("Continuar? (S/N): ").strip().upper()
        if continue_input == 'N':
            break
    
    average = total / count if count > 0 else 0
    
    print(f"Somatório: {total}")
    print(f"Menor valor: {minimum}")
    print(f"Média: {average:.1f}")
    print(f"Quantidade de valores pares: {even_count}")

def exercise_64():
    for i in range(0, 41, 5):
        print(i, end=' ')
    print("Acabou!")

def exercise_65():
    for i in range(100, -1, -10):
        print(i, end=' ')
    print("Acabou!")

def exercise_66():
    number = int(input("Digite um valor para ver a tabuada: "))
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

def exercise_67():
    number = int(input("Digite um número inteiro positivo: "))
    print("Contagem:", end=' ')
    for i in range(0, number + 1):
        print(i, end=', ' if i < number else '')
    print(" FIM!")

def exercise_68():
    women_count = 0
    men_above_100kg = 0
    women_weight_sum = 0.0
    women_registered = 0
    max_men_weight = None
    
    for i in range(8):
        gender = input(f"Sexo da {i+1}ª pessoa (M/F): ").strip().upper()
        weight = float(input("Peso (kg): "))
        
        if gender == 'F':
            women_count += 1
            women_weight_sum += weight
            women_registered += 1
        elif gender == 'M':
            if weight > 100:
                men_above_100kg += 1
            if max_men_weight is None or weight > max_men_weight:
                max_men_weight = weight
    
    women_average = (women_weight_sum / women_registered) if women_registered > 0 else 0
    
    print(f"Mulheres cadastradas: {women_count}")
    print(f"Homens com mais de 100kg: {men_above_100kg}")
    print(f"Média de peso entre as mulheres: {women_average:.2f} kg")
    print(f"Maior peso entre os homens: {max_men_weight if max_men_weight is not None else 'Nenhum homem cadastrado'}")

def exercise_69():
    first_term = int(input("Primeiro termo da PA: "))
    ratio = int(input("Razão da PA: "))
    
    terms = [first_term + i * ratio for i in range(10)]
    total = sum(terms)
    
    print("10 primeiros termos:", terms)
    print(f"Soma dos termos: {total}")

def exercise_70():
    a, b = 1, 1
    fibonacci = [a, b]
    
    for _ in range(8):
        a, b = b, a + b
        fibonacci.append(b)
    
    print("Sequência Fibonacci (10 primeiros):", fibonacci[:10])

def exercise_71():
    vector = [999] * 8
    print(vector)
    print(list(range(8)))

def exercise_72():
    vector = [(i + 1) * 5 for i in range(10)]
    print(vector)
    print(list(range(10)))

def exercise_73():
    vector = [9 - i for i in range(10)]
    print(vector)
    print(list(range(10)))

def exercise_74():
    vector = [5 if i % 2 == 0 else 3 for i in range(10)]
    print(vector)
    print(list(range(10)))

def exercise_75():
    fibonacci = [1, 1]
    for i in range(2, 15):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    
    print(fibonacci[:15])
    print(list(range(15)))

def exercise_76():
    vector = [random.randint(0, 100) for _ in range(7)]
    print("Valores gerados:", vector)

def exercise_77():
    names = []
    for i in range(7):
        name = input(f"Digite o nome {i+1}: ")
        names.append(name)
    
    print("Ordem inversa:")
    for name in reversed(names):
        print(name)

def exercise_78():
    numbers = []
    for i in range(15):
        number = int(input(f"Digite o {i+1}º número: "))
        numbers.append(number)
    
    print("Vetor:", numbers)
    
    mult10_positions = [i for i, value in enumerate(numbers) if value % 10 == 0]
    print("Posições com múltiplos de 10:", mult10_positions)

def exercise_79():
    numbers = []
    for i in range(10):
        number = int(input(f"Digite o {i+1}º número: "))
        numbers.append(number)
    
    even_numbers = [(i, number) for i, number in enumerate(numbers) if number % 2 == 0]
    print("Números pares e suas posições:", even_numbers)

def exercise_80():
    vector = [random.randint(1, 15) for _ in range(30)]
    key = int(input("Digite a chave (1-15): "))
    
    positions = [i for i, value in enumerate(vector) if value == key]
    occurrences = len(positions)
    
    print("Vetor:", vector)
    print(f"Posições da chave: {positions}")
    print(f"Total de ocorrências: {occurrences}")

def exercise_81():
    ages = [int(input(f"Idade da {i+1}ª pessoa: ")) for i in range(8)]
    
    average = sum(ages) / len(ages)
    above_25_positions = [i for i, age in enumerate(ages) if age > 25]
    max_age = max(ages)
    max_positions = [i for i, age in enumerate(ages) if age == max_age]
    
    print(f"Média: {average:.1f}")
    print(f"Posições com mais de 25 anos: {above_25_positions}")
    print(f"Maior idade: {max_age}")
    print(f"Posições da maior idade: {max_positions}")

def exercise_82():
    grades = [float(input(f"Nota do aluno {i+1}: ")) for i in range(10)]
    
    average = sum(grades) / 10
    above_average = sum(1 for grade in grades if grade > average)
    max_grade = max(grades)
    max_positions = [i for i, grade in enumerate(grades) if grade == max_grade]
    
    print(f"Média da turma: {average:.1f}")
    print(f"Alunos acima da média: {above_average}")
    print(f"Maior nota: {max_grade}")
    print(f"Posições da maior nota: {max_positions}")

def exercise_83():
    vector = [random.randint(0, 99) for _ in range(20)]
    print("Gerados:", vector)
    
    vector.sort()
    print("Ordenados:", vector)

def exercise_84():
    names = []
    ages = []
    
    for i in range(9):
        name = input(f"Nome {i+1}: ")
        age = int(input("Idade: "))
        names.append(name)
        ages.append(age)
    
    print("Menores de idade:")
    for name, age in zip(names, ages):
        if age < 18:
            print(f"{name} - {age} anos")

def exercise_85():
    names = []
    genders = []
    salaries = []
    
    for i in range(5):
        name = input(f"Nome {i+1}: ")
        gender = input("Sexo (M/F): ").strip().upper()
        salary = float(input("Salário (R$): "))
        
        names.append(name)
        genders.append(gender)
        salaries.append(salary)
    
    print("Funcionárias mulheres com salário > R$5000:")
    for name, gender, salary in zip(names, genders, salaries):
        if gender == 'F' and salary > 5000:
            print(f"{name} - R$ {salary:.2f}")

def generator(message="Olá, Mundo!", times=1, border=1):
    borders = {
        1: "+-------=======------+",
        2: "~~~~~~~:::::::~~~~~~~",
        3: "<<<<<<<<------->>>>>>"
    }
    top = borders.get(border, borders[1])
    print(top)
    for _ in range(times):
        print(f" {message}")
    print(top)

def exercise_86():
    generator()

def exercise_87():
    message = input("Mensagem para o gerador: ")
    generator(message=message, times=1)

def exercise_88():
    message = input("Mensagem: ")
    times = int(input("Quantidade de vezes: "))
    generator(message=message, times=times)

def exercise_89():
    message = input("Mensagem: ")
    times = int(input("Quantidade de vezes: "))
    print("Escolha a borda: 1, 2 ou 3")
    border = int(input("Borda: "))
    generator(message=message, times=times, border=border)

def sum_numbers(a, b):
    return a + b

def exercise_90():
    a = float(input("Digite o 1º valor: "))
    b = float(input("Digite o 2º valor: "))
    print(f"Soma: {sum_numbers(a, b)}")

def compare_numbers(a, b):
    if a > b:
        print(f"{a} é maior que {b}")
    elif b > a:
        print(f"{b} é maior que {a}")
    else:
        print("Ambos são iguais")

def exercise_91():
    a = float(input("Digite o 1º valor: "))
    b = float(input("Digite o 2º valor: "))
    compare_numbers(a, b)

def check_even_odd(number):
    print("PAR" if number % 2 == 0 else "ÍMPAR")

def exercise_92():
    number = int(input("Digite um número inteiro: "))
    check_even_odd(number)

def counter(start, end, increment):
    if increment == 0:
        print("Incremento não pode ser zero.")
        return
    
    if start <= end:
        current = start
        while current <= end:
            print(current, end=' >> ')
            current += abs(increment)
    else:
        current = start
        while current >= end:
            print(current, end=' >> ')
            current -= abs(increment)
    print("FIM")

def exercise_93():
    start = int(input("Início: "))
    end = int(input("Fim: "))
    increment = int(input("Incremento: "))
    counter(start, end, increment)

def fibonacci_sequence(n):
    a, b = 1, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    print(" >> ".join(str(x) for x in sequence), ">> FIM")

def exercise_94():
    n = int(input("Quantos termos da Fibonacci exibir: "))
    fibonacci_sequence(n)

def sum_function(a, b):
    return a + b

def exercise_95():
    a = float(input("1º valor: "))
    b = float(input("2º valor: "))
    print(f"Soma (função): {sum_function(a, b)}")

def average(n1, n2):
    return (n1 + n2) / 2

def exercise_96():
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    print(f"Média: {average(n1, n2):.1f}")

def find_maximum(a, b, c):
    return max(a, b, c)

def exercise_97():
    a = float(input("1º número: "))
    b = float(input("2º número: "))
    c = float(input("3º número: "))
    print(f"Maior: {find_maximum(a, b, c)}")

def super_sum(a, b):
    if a > b:
        a, b = b, a
    return sum(range(int(a), int(b) + 1))

def exercise_98():
    a = int(input("Início: "))
    b = int(input("Fim: "))
    print(f"Soma entre {a} e {b}: {super_sum(a, b)}")

def power(base, exponent):
    return base ** exponent

def exercise_99():
    base = float(input("Base: "))
    exponent = float(input("Expoente: "))
    print(f"Resultado: {power(base, exponent)}")

def get_situation(avg):
    if avg <= 4.9:
        return "REPROVADO"
    elif 5.0 <= avg <= 6.9:
        return "RECUPERAÇÃO"
    else:
        return "APROVADO"

def exercise_100():
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    avg = average(n1, n2)
    situation = get_situation(avg)
    print(f"Média: {avg:.1f} - Situação: {situation}")

def run_exercise(exercise_number):
    exercise_functions = {
        1: exercise_01, 2: exercise_02, 3: exercise_03, 4: exercise_04, 5: exercise_05,
        6: exercise_06, 7: exercise_07, 8: exercise_08, 9: exercise_09, 10: exercise_10,
        11: exercise_11, 12: exercise_12, 13: exercise_13, 14: exercise_14, 15: exercise_15,
        16: exercise_16, 17: exercise_17, 18: exercise_18, 19: exercise_19, 20: exercise_20,
        21: exercise_21, 22: exercise_22, 23: exercise_23, 24: exercise_24, 25: exercise_25,
        26: exercise_26, 27: exercise_27, 28: exercise_28, 29: exercise_29, 30: exercise_30,
        31: exercise_31, 32: exercise_32, 33: exercise_33, 34: exercise_34, 35: exercise_35,
        36: exercise_36, 37: exercise_37, 38: exercise_38, 39: exercise_39, 40: exercise_40,
        41: exercise_41, 42: exercise_42, 43: exercise_43, 44: exercise_44, 45: exercise_45,
        46: exercise_46, 47: exercise_47, 48: exercise_48, 49: exercise_49, 50: exercise_50,
        51: exercise_51, 52: exercise_52, 53: exercise_53, 54: exercise_54, 55: exercise_55,
        56: exercise_56, 57: exercise_57, 58: exercise_58, 59: exercise_59, 60: exercise_60,
        61: exercise_61, 62: exercise_62, 63: exercise_63, 64: exercise_64, 65: exercise_65,
        66: exercise_66, 67: exercise_67, 68: exercise_68, 69: exercise_69, 70: exercise_70,
        71: exercise_71, 72: exercise_72, 73: exercise_73, 74: exercise_74, 75: exercise_75,
        76: exercise_76, 77: exercise_77, 78: exercise_78, 79: exercise_79, 80: exercise_80,
        81: exercise_81, 82: exercise_82, 83: exercise_83, 84: exercise_84, 85: exercise_85,
        86: exercise_86, 87: exercise_87, 88: exercise_88, 89: exercise_89, 90: exercise_90,
        91: exercise_91, 92: exercise_92, 93: exercise_93, 94: exercise_94, 95: exercise_95,
        96: exercise_96, 97: exercise_97, 98: exercise_98, 99: exercise_99, 100: exercise_100,
    }
    
    if exercise_number in exercise_functions:
        print(f"\n--- Exercício {exercise_number} ---")
        exercise_functions[exercise_number]()
    else:
        print(f"Exercício {exercise_number} não encontrado ou ainda não implementado.")

def main():
    print("Exercícios de Programação Python")
    print("Escolha um número de exercício (1-100) ou 0 para sair:")
    
    while True:
        try:
            choice = int(input("\nDigite o número do exercício: "))
            if choice == 0:
                print("Até logo!")
                break
            run_exercise(choice)
        except ValueError:
            print("Por favor, digite um número válido.")
        except KeyboardInterrupt:
            print("\nAté logo!")
            break

if __name__ == "__main__":
    main()
