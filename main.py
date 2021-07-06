from morse_code_io import MCInputOutput, MCConvertInput
import morse_code_variables

convert_input = MCConvertInput()
user_text = MCInputOutput()
print(user_text.welcome())
print(user_text.instructions())
while morse_code_variables.exit_program == False:
    clean_input = convert_input.clean_input(user_text.get_input())
    # print(clean_input)  # comment out
    if clean_input:
        converted_text = user_text.get_output(clean_input)
        print(converted_text)

