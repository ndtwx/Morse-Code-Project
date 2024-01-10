import os

morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '|'
}

morse_dict_swap = {v: k for k, v in morse_dict.items()}
morse_code_list = [value for (key, value) in morse_dict.items()]


# print(morse_dict_swap)
# print(list_of_morse_signs)
def converter(option):
    if option == "1":
        text = input("\nType your text here: ").upper()

        converted_text = ""

        for char in text:
            converted_text += morse_dict[char] + ' '

        print(f"Converted text: {converted_text}\n")

    elif option == "2":
        code = input("\nType your code here: ").split(" ")

        converted_code = ""

        for char in code:
            if char not in morse_code_list:
                print("\nThere are no such codes, please enter again.\n")
                start()

            else:
                converted_code += morse_dict_swap[char]

        print(f"Converted code: {converted_code}\n")

    else:
        print("\nYou have chosen the wrong option, Please choose one of the available options\n")


def start():
    should_continue = True
    while should_continue:
        print("|TEXT/MORSE CODE CONVERTER|")
        print("\n1. Enter 1 to convert text to code")
        print("2. Enter 2 to convert code to text")

        option = input("Enter your option: ").lower()

        converter(option=option)


start()
