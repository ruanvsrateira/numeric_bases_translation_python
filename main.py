decimal_base_value = int(input("Digite um valor na base decimal: "))

def format_final_number(number):
  return number[2:]

def main():
  #Transformando valor para a base binária
  bin_value = format_final_number(bin(decimal_base_value))

  #Transformando valor para a base octal
  oct_value = format_final_number(oct(decimal_base_value))

  #Transformando valor para a base hexadecimal 
  hex_value = format_final_number(hex(decimal_base_value))

  print(f"O valor decimal {decimal_base_value} é correspondente as outras bases, sendo:\nBase binária: {bin_value}\nBase Octal: {oct_value}\nBase hexadecimal: {hex_value}")
if __name__ == "__main__":
  main()