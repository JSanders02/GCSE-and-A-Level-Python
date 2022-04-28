import sys
import time

def colourWrite(text, tag):
    if COLOUR:
        shell.write('\n' + str(text), tag)
    else:
        print(str(text))

try:
    shell = sys.stdout.shell
    COLOUR = True
except AttributeError:
    COLOUR = False

print("here are all the valid tags:\n")

valid_tags = ('SYNC', 'stdin', 'BUILTIN', 'STRING', 'console', 'COMMENT', 'stdout',
              'TODO','stderr', 'hit', 'DEFINITION', 'KEYWORD', 'ERROR', 'sel')


for tag in valid_tags:
    if COLOUR:
        shell.write(tag+ '\n',tag)
    else:
        print(tag)

time.sleep(1)
print("\n\nUsage : sys.stdout.shell.write(<text>, <tag>)")

colourWrite('Test String', 'COMMENT')
colourWrite('Test String', 'COMMENT')
colourWrite('Test String', 'CMENT')
