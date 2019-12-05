import re



# function to take data from template_madlib file


def read_file(file):
    with open(file, 'r') as f:
        template = (f.read())
        return(template)

template = read_file('template_madlib.txt')
# print(read_file('template_madlib.txt'))

# function to save data from template_madlib

# function to extract {arguments} from the template to the array:


# print(template)




# 1.make a regex pattern that will find the words between {}
# 2.run regex pattern over the template and extract all words to array
# 3.extract this values from the template

pattern = "\{[a-zA-Z0-9' -]*\}"

empty_template = re.sub(pattern, "{}", template, flags = re.IGNORECASE|re.MULTILINE)
print(empty_template)




# function to output welcome message and rules of the game to the screen
# function to prompt user to asking for inputs for different words
# function to popelate our template with collected user inputs
# fucntion to provide response to user
# write the completed template to the new file
