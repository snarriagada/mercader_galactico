from validations import *
from helpers import *
import sys

# definimos el archivo txt entregado en la línea de comandos
try:
    input = sys.argv[1]
except:
    print("An exception ocurred with the .txt input")

error_message = "El input no sigue el formato esperado"

def main(input):
    conversion = {}
    metals_price = {}
    unit_prices = {}
    output_lines = []

    with open(input, 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            line = line.split(" is ")
            if is_traduction(line):
                conversion[line[0]] = line[1]
            elif is_metal_price(line):
                save_metal_price(line, metals_price)
            elif is_conversion_question(line):
                try:
                    amount = line[1].split(" ")
                    roman_number = galactic_to_roman(amount, conversion)
                    result = roman_to_integer(roman_number)
                    response = line[1][:-1]+"is "+str(result)
                    output_lines.append(response)
                except Exception as e:
                    output_lines.append("I cannot resolve this question")
            elif is_price_question(line):
                try:
                    unit_prices = get_unit_metal_prices(metals_price, conversion)
                    deal_price = get_deal_price(line[1], unit_prices, conversion)
                    response = line[1][:-1]+"is "+str(deal_price)+" Credits"
                    output_lines.append(response)
                except Exception as e:
                    output_lines.append("I cannot resolve this question")
            else:
                output_lines.append("I have no idea what you are talking about")
        write_output(output_lines)

        #print("conversion: ", conversion)
        #print("metals prices: ",metals_price)
        #print("unit prices: ",unit_prices)

def write_output(output_lines):
    with open('output.txt', 'w') as file:
        file.write('\n'.join(output_lines))
    return
                



main(input)