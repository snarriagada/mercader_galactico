def get_deal_price(line, unit_prices, conversion):
    line = line.split(" ")
    if line[-1] == "?" : line.pop()  
    metal = line.pop()
    galactic_amount = line
    roman_number = galactic_to_roman(galactic_amount, conversion)
    integer_amount = roman_to_integer(roman_number)
    deal_price = integer_amount * unit_prices[metal]
    return deal_price

def get_unit_metal_prices(prices, conversion):
    unit_prices = dict()
    for metal in prices.keys():
        roman_number = galactic_to_roman(prices[metal][0], conversion)
        integer = roman_to_integer(roman_number)
        credits = prices[metal][1].split(" ")
        unit_prices[metal] = int(credits[0])/integer
    return unit_prices


def roman_to_integer(roman_number):
    integers = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    i = 0
    while i < len(roman_number):
        if i == len(roman_number)-1:
            result += integers[roman_number[i]]
        elif integers[roman_number[i+1]] <= integers[roman_number[i]]:
            result += integers[roman_number[i]]
        else:
            result += (integers[roman_number[i+1]] - integers[roman_number[i]])
            i = i+1
        i = i+1
    return result

def galactic_to_roman(line, conversion):
    if line[-1] == "?" : line.pop()
    roman_number = []
    for number in line:
        roman_number.append(conversion[number])
    valid = check_roman_numeral(roman_number)
    if not valid : return False
    return roman_number


def save_metal_price(line, metals_price):
    aux = line[0].split(" ")
    metal = aux[-1]
    aux.pop()
    if len(line) > 1:
        metals_price[metal] = [aux, line[1]]

def check_roman_numeral(numeral):
    invalid_numerals = ["DD", "LL", "VV", "IIII", "XXXX", "CCCC", "MMMM",
    "IL", "IC", "IM", "ID", "XD", "XM", "DM", "LC", "LD", "LM", "VX", "VL",
    "VC", "VD", "VM"]

    numeral = "".join(numeral)
    for n in invalid_numerals:
        if n in numeral:
            return False
    return True

