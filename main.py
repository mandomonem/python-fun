from helper import print_colorized, ask, ask_colorized
import helper
import test
name = ask("What's your name? ")
if name == None or name == "Not telling you my name" or name == "Not telling you":
    print_colorized("ERROR: It's required to specify your name.", "red")
    helper.wait(2)
    name = ask_colorized("Please enter your name. ", "red")
else:
    test.print_hi(name)
