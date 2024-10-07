def calculate (Some_number1, Some_number2, Some_operathin):
    if Some_operathin == '+':
        return Some_number1 + Some_number2
    elif Some_operathin == '-':
        return Some_number1 - Some_number2
    elif Some_operathin == '*':
        return Some_number1 * Some_number2
    elif Some_operathin == '/':
        if Some_number2 != 0:
            return Some_number1 / Some_number2
        else:
            return "Error: division by zero!"
    else: return "Error: Unknown operation!"

while True:
    try:
        Some_number1 = float(input("Tipe some number"))
        Some_operathin = input("Tipe some operation (+, -, *, /): ")
        Some_number2 = float(input("Tipe some number"))
        Some_result = calculate(Some_number1,Some_number2, Some_operathin)
        print(f"{Some_result}")
    except ValueError:
        print ("Error: Invalid number entered!")

    continua_calc = input("Want to continua?(yes/no)")
    if continua_calc != "yes" :
        print("The program is complete.")
        break