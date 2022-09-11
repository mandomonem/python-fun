import time
from termcolor import colored

def print_str(text=str):
    print(text)


def print_colorized(text=str, color=str):
    print(colored(text, color))


def wait(secs=float):
    time.sleep(secs)


def get_score(score_result=float):
    score = score_result
    if score_result == str:
        print_str(score)
    elif score_result == float:
        score = score_result
        print_str(str(score))
    elif score_result == None or score_result == "":
        print_colorized("Score was not specified", "red")
        return 1
    else:
        print_colorized("Unrecognized score", "red")
