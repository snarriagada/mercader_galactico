from validations import *
from helpers import *
import sys

# definimos el archivo txt entregado en la línea de comandos
try:
    input = sys.argv[1]
except:
    print("An exception ocurred with the .txt input")

romans = ["I", "V", "X", "L", "C", "D", "M"]

def main(input):
    conversion = {}
    metals_price = {}
    unit_prices = {}
    with open(input, 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            print(line)
            line = line.split(" is ")
            if is_traduction(line):
                conversion[line[0]] = line[1]
            if is_metal_price(line):
                save_metal_price(line, metals_price)
            if is_conversion_question(line):
                amount = line[1].split(" ")
                roman_number = galactic_to_roman(amount, conversion)
                roman_to_integer(roman_number)
            if is_price_question(line):
                unit_prices = get_unit_metal_prices(metals_price, conversion)
                deal_price = get_deal_price(line[1], unit_prices, conversion)
                print(deal_price)

                
    print("------")
    print("conversion: ", conversion)
    print("metals prices: ",metals_price)
    print("unit prices: ",unit_prices)


main(input)