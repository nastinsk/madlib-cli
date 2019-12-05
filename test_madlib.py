import pytest

from madlib import read_file, prompts_list, empty_template, print_prompts, handle_IO, write_file


#these tests pass only if run pytest -s command and with inputs "1" or "" - empty input
def test_read():
    expected = 'test {one} test {two} test {three}\n'
    actual = read_file('file_test.txt')
    assert actual == expected

def test_prompts_list():
    expected = ['{one}', '{two}', '{three}']
    actual = prompts_list('\{[a-zA-Z0-9\' -]*\}','test {one} test {two} test {three}')
    assert actual == expected

def test_prompts_list2():
    expected = ['{Adjective}', '{Adjective}', '{A First Name}', '{Past Tense Verb}', '{A First Name}', '{Adjective}', '{Adjective}', '{Plural Noun}', '{Large Animal}', '{Small Animal}', "{A Girl's Name}", '{Adjective}', '{Plural Noun}', '{Adjective}', '{Plural Noun}', '{Number 1-50}', "{First Name's}", '{Number}', '{Plural Noun}', '{Number}', '{Plural Noun}']
    actual = prompts_list('\{[a-zA-Z0-9\' -]*\}', read_file('template_madlib.txt'))
    assert actual == expected

def test_empty_template():
    expected = 'test {} test {} test {}'
    actual = empty_template('\{[a-zA-Z0-9\' -]*\}','test {one} test {two} test {three}')
    assert actual == expected

def test_empty_template2():
    expected = "Make Me A Video Game!\n\nI the {} and {} {} have {}{}'s {} sister and plan to steal her {} {}!\n\nWhat are a {} and backpacking {} to do? Before you can help {}, you'll have to collect the {} {} and {} {} that open up the {} worlds connected to A {} Lair. There are {} {} and {} {} in the game, along with hundreds of other goodies for you to find.\n"
    actual = empty_template('\{[a-zA-Z0-9\' -]*\}',read_file('template_madlib.txt'))
    assert actual == expected

# for these tests we need to use "1"  or "" - empty input for each input

def test_print_prompts():
    expected = ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']
    expected2 = ['','','','','','','','','','','','','','','','','','','','','']
    actual = print_prompts()
    assert actual == expected or expected2

def test_handle_IO():
    expected = "\nHere is your story:\n-------------------\n\nI the 1 and 1 1 have 11's 1 sister and plan to steal her 1 1!\n\nWhat are a 1 and backpacking 1 to do? Before you can help 1, you'll have to collect the 1 1 and 1 1 that open up the 1 worlds connected to A 1 Lair. There are 1 1 and 1 1 in the game, along with hundreds of other goodies for you to find.\n"

    expected2 = ["\nHere is your story:\n-------------------\n\nI the  and   have 's  sister and plan to steal her  !\n\nWhat are a  and backpacking  to do? Before you can help , you'll have to collect the   and   that open up the  worlds connected to A  Lair. There are   and   in the game, along with hundreds of other goodies for you to find.\n"]

    actual = handle_IO()
    assert actual == expected or expected2

def test_write_file():
    expected = "\nHere is your story:\n-------------------\n\nI the 1 and 1 1 have 11's 1 sister and plan to steal her 1 1!\n\nWhat are a 1 and backpacking 1 to do? Before you can help 1, you'll have to collect the 1 1 and 1 1 that open up the 1 worlds connected to A 1 Lair. There are 1 1 and 1 1 in the game, along with hundreds of other goodies for you to find.\n"

    expected2 = "\nHere is your story:\n-------------------\n\nI the  and   have 's  sister and plan to steal her  !\n\nWhat are a  and backpacking  to do? Before you can help , you'll have to collect the   and   that open up the  worlds connected to A  Lair. There are   and   in the game, along with hundreds of other goodies for you to find.\n"
    actual = read_file('madlib_result.txt')
    assert actual == expected or expected2


