from .UUID_generator import generate_random_string
import os

generated_function = []
def_tag = "def "
UUID_tag = generate_random_string()
function_name = (UUID_tag)+"_function"
user_input = "text = ‘world’,print(‘hello’),print(text)"

def generate_function(text):
    tab_characters = "    "
    random_function = def_tag+function_name+"():\n"+tab_characters+text
    # print(random_function)
    generate_function = random_function
    return generate_function
    # exit()
    # for i in range(0, len(uuid_fuction_file)):
    #     line_of_code = tab_characters, [text]
    #     function_build = line_of_code
    # function_build = []
    # working_function = (f'{random_function} \n {function_build}')


f = open('/Users/machd/Dropbox/Mac/Documents/VISUAL CODE/ASSIGNMENT 003 FUNCTION GENERATOR/utility_functions/generated_functions_list.py', "a")
f.write(generate_function(f"{user_input}\n").replace(f",", "\n    "))
print(f"SUCCESS: {function_name}")
f.close()
    
exit()