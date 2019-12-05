# import ReGex module
import re

def read_file(file):
    """F() to take data from template_madlib file"""
    with open(file, 'r') as f:
        template = (f.read())
        return template

# call read_file() to read the template_madlib file
template_file = read_file('template_madlib.txt')


def prompts_list(pattern, template):
    """F()to run regex pattern over the template and extract all words to array prompts"""
    prompts = re.findall(pattern, template)
    return prompts

def empty_template(pattern, template):
    """F() to extract all {words} from the template using pattern"""
    template = re.sub(pattern, "{}", template)
    return template


def print_prompts():
    """Print prompts to user and return array of users inputs"""
    user_words = []
    for el in prompts_list("\{[a-zA-Z0-9\' -]*\}", template_file):
        user_word = input(f'Give me {el[1:-1]}: -----> ')
        user_words.append(user_word)
    return user_words


def handle_IO():
    """F() to output welcome message and rules of the game to the screen"""

    # ask if user wants to play
    if input("\n***************************************\n**** Welcome to the Mad Libs Game! ****\n \n Mad Libs is a phrasal template word game\n where user(you) need to input different\n words following prompts. At the end you\n will get a story that was created\n using your inputs.\n \nPlease type 'y' if you want to play:\n") == "y":

        # store return from print_promts()
        user_words = print_prompts()

        # store the empty template in new var
        template = empty_template("\{[a-zA-Z0-9\' -]*\}", template_file)

        # return template formated with users inputs
        formatted_template = f'\nHere is your story:\n-------------------\n{template.format(*user_words)[22:]}'

        # print results to user
        print(formatted_template)

        return formatted_template



def write_file(file, contents):
    """F() to write program results to the file"""
    with open(file, 'w') as f:
        template = (f.write(contents))

# write the completed template to the new file
write_file('madlib_result.txt', handle_IO())

