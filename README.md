# File IO and Exceptions

**Author**: Anastasia Lebedeva
**Version**: 1.1.0

## Overview
The terminal version of the Mad Libs Game. Mad Libs is a phrasal template word game where user need to input different words to following prompts. At the end user will get a story that was created using their inputs.


## Getting Started
1. In terminal navigate to the folder with the madlib.py.
2. Run command "python madlib.py".
3. Read through the rules, type "y" to play, type other to quit
4. Input the words following the prompt (21 words)
5. Receive your output
6. Check you current result in the madlib_result.txt file


## Architecture
* Python 3.7.5
* Pipenv
* Regex module for Python
* Pytest

*             write_file()
*                   |
*          _____handle_IO()_____
*         |                     |
*   print_prompts()   |     empty_template()
*       |
*   prompt_list()
*       |
*   read_file()


## API
1. read_file(file) -  function to take data from template_madlib file, takes file path as parameter
2. prompts_list(pattern, template) - function to run regex pattern over the template and extract all words to array prompts, takes two parameters - reGex pattern as a string and a string that need to be checked
3. empty_template(pattern, template) -  extracts all {words} following reGex patter from the string. takes two parameters - reGex pattern as a string and a string that need to be modified
4. print_prompts() - print prompts to user and return array of users inputs
5. handle_IO() - F() to output welcome message and rules of the game to the screen
6. write_file(file, contents) - F() to write program results to the file, taket two parameters - file path and contents that need to be placed in file


## Change Log

* 12/04/2019 19:03 - Initial folder setup
* 12/04/2019 20:56 - REgex pattern created
* 12/04/2019 21:49 - Functions for communication with user added
* 12/04/2019 22:46 - Game complited
* 12/04/2019 23:24 - README.md documentation added
