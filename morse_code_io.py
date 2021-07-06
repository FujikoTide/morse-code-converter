import string
import re
import morse_code_variables
from morse_code_dict import MorseCodeDict


class MCInputOutput:
    def __init__(self):
        pass

    def welcome(self):
        self.welcome_text = 'Welcome to the Morse Code Converter!'
        return self.welcome_text

    def instructions(self):
        """
        Prints instruction message
        """
        self.instruction_text = 'Please enter some text you wish to convert to or from morse code, or [exit] to exit.\n' \
                                'for example:\n' \
                                '\t..-\n' \
                                '\tplain text characters\n' \

        return self.instruction_text

    def get_input(self):
        user_input = input('Your message for conversion:\n').upper()
        return user_input

    def get_output(self, user_input: str) -> str:
        mcd = MorseCodeDict()
        clean_chars_regex = re.compile('[A-Z0-9 ]')
        dot_dash_regex = re.compile(r'[\.\- ]')
        if clean_chars_regex.match(user_input):
            # print(user_input)
            converted_text = [mcd.letter_to_mc[letter] for letter in user_input]
            converted_text = ' '.join(converted_text)
            return converted_text
        elif dot_dash_regex.match(user_input):
            converted_text = [mcd.mc_to_letter[word] for word in user_input.split()]
            converted_text = ''.join(converted_text)
            return converted_text


class MCConvertInput:
    def __init__(self):
        pass

    def clean_input(self, user_input: str = "") -> str:
        clean_characters = string.ascii_uppercase + string.digits + ' '
        dot_dash = '.- '
        clean_chars_regex = re.compile('[A-Z0-9 ]')
        dot_dash_regex = re.compile(r'[\.\- ]')
        if user_input == '[EXIT]':
            morse_code_variables.exit_program = True
        elif clean_chars_regex.match(user_input):
            cleaned_input = ''.join([letter for letter in user_input if letter in clean_characters])
            clean_input = ' '.join(cleaned_input.split())
            return clean_input
        elif dot_dash_regex.match(user_input):
            cleaned_input = ''.join([letter for letter in user_input if letter in dot_dash])
            clean_input = ' '.join(cleaned_input.split())
            return clean_input
        else:
            print('You have not entered something I understand, please try again')
            print(MCInputOutput.instructions(self))
