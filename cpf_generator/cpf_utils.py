import re
import random


def get_digit(cpf: str) -> int:

    len_cpf = len(cpf) + 1

    multiplication = []
    for cpf_index, multiplier in enumerate(range(len_cpf, 1, -1)):

        multiplication.append(int(cpf[cpf_index]) * multiplier)

    total_sum = sum(multiplication)
    digit = 11 - (total_sum % 11)

    return digit if digit < 10 else 0

def get_first_digit(cpf: str) -> int:

    return get_digit(cpf[:9])


def get_second_digit(cpf: str) -> int:

    return get_digit(cpf[:10])


def remove_not_numbers(cpf: str) -> str:

    return re.sub(r'\D', '', cpf)


def has_eleven_chars(value: str) -> bool:

    return len(value) == 11


def is_sequence(value: str) -> bool:

    return (value[0] * len(value)) == value


def is_valid(cpf: str) -> bool:

    clean_cpf = remove_not_numbers(cpf)

    if not has_eleven_chars(clean_cpf):

        return False

    if is_sequence(clean_cpf):

        return False

    first_digit = get_first_digit(clean_cpf)
    second_digit = get_second_digit(clean_cpf)

    new_cpf = f'{clean_cpf[:9]}{first_digit}{second_digit}'

    if new_cpf == clean_cpf:
        
        return True
    
    return False


def generate_cpf() -> str:

    nine_digits = ''.join([str(random.randint(0, 9)) for x in range(9)])
    first_digit = get_first_digit(nine_digits)
    second_digit = get_second_digit(f'{nine_digits}{first_digit}')
    new_cpf = f'{nine_digits}{first_digit}{second_digit}'
    
    return new_cpf


def format_cpf(cpf: str) -> str:

    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'


if __name__ == "__main__":

    print(is_valid('488.611.340-09'))
    print(is_valid('111.111.111-11'))

    cpf = generate_cpf()
    formatted_cpf = format_cpf(cpf)

    print(cpf, formatted_cpf)