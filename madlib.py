import re



# function to take data from template_madlib file


def read_file(file):
    with open(file, 'r') as f:
        template = (f.read())
        return(template)


# print(read_file('template_madlib.txt'))

# function to save data from template_madlib

# function to extract {arguments} from the template to the array:


# print(template)



# call read_file() to read the template_madlib file
template = read_file('template_madlib.txt')

def prompts_list(pattern, template):
    # run regex pattern over the template and extract all words to array prompts
    prompts = re.findall(pattern, template)
    return prompts

def empty_template(pattern, template):
    # extract all {words} from the template
    template = re.sub(pattern, "{}", template)
    return template




empty_template("\{[a-zA-Z0-9' -]*\}", template)

def print_prompts():
    user_words = []
    for el in prompts_list("\{[a-zA-Z0-9' -]*\}", template):
        user_word = input(f'Give me {el[1:-1]}: -----> ')
        user_words.append(user_word)
    return user_words

# function to output welcome message and rules of the game to the screen
if input("**** Welcome to the Mad Libs Game! ****\n \n Mad Libs is a phrasal template word game\n where user(you) need to input different\n words following prompts. At the end you\n will get a story that was created\n using your inputs.\n Please type 'y' if you want to play\n") == "y":

    print(print_prompts())





# function to prompt user to asking for inputs for different words
# function to populate our template with collected user inputs
# fucntion to provide response to user
# write the completed template to the new file
