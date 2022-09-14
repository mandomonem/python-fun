import time
from termcolor import colored


def print_str(text):
    print(text)


def print_colorized(text, color):
    print(colored(text, color))


def wait(secs):
    time.sleep(secs)


def get_score(score_result):
    score = score_result
    if score_result == str:
        print_str(score)
    elif score_result == float:
        score = score_result
        print_str(str(score))
    elif score_result == None:
        print_colorized("Score was not specified", "red")
        return 1
    else:
        print_colorized("Unrecognized score", "red")
        return 1


def ask(question):
    input(question)


def ask_colorized(question, color):
    ask(colored(question, color))