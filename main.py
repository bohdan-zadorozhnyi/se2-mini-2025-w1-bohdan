import numbers
import decimal
import re


def check_num(x):
    return isinstance(x, numbers.Number) or isinstance(x, decimal.Decimal)


def extract_delimiters(x):
    delimiters = []
    while True:
        custom_delimiter_match = re.match(r"^//\[(.+?)\](.+)", x)
        if not custom_delimiter_match: break
        delimiter, x = custom_delimiter_match.groups()
        x = "//" + x
        delimiters.append(delimiter)

    return '|'.join(map(re.escape, delimiters)), x[2:]

def calculator(x):
    if x == "":
        return 0
    if check_num(x):
        return x

    delimiter, x1 = extract_delimiters(x)

    if not delimiter:
        custom_delimiter_match = re.match(r"^//(.)(.+)", x)
        if custom_delimiter_match:
            delimiter, x = custom_delimiter_match.groups()
            delimiter = re.escape(delimiter)
        else:
            delimiter = r",|\n"
    else:
        x = x1
    print(delimiter, x)
    try:
        numbers_list = re.split(delimiter, x)
        print(numbers_list)
        numbers_list = [decimal.Decimal(num) for num in numbers_list if num]

        for i, num in enumerate(numbers_list):
            if num > 1000:
                numbers_list.pop(i)

            if num < 0:
                raise Exception

        if len(numbers_list) > 3:
            return ":("

        return sum(numbers_list)

    except (ValueError, decimal.InvalidOperation):
        return ":("
