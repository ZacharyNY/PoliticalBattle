import character
from crudder import *

'''
using this file to test things
'''


c = Crudder()
print c.get_party("Donald Trump")
print c.get_health("Donald Trump")


char = character.Character("Hillary Clinton")
char.get_picture("left")
