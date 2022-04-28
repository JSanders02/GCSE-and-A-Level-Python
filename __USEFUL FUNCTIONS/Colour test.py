import sys

try:
    shell = sys.stdout.shell
except AttributeError:
    raise RuntimeError("You must run this program in IDLE")

shell.write("Example","KEYWORD")
shell.write(" of","STRING")
shell.write(" colours","KEYWORD")
shell.write(" in","DEFINITION")
shell.write(" python","KEYWORD")
shell.write(".","COMMENT")
answer = input()

print("here are all the valid tags:\n")

valid_tags = ('SYNC', 'stdin', 'BUILTIN', 'STRING', 'console', 'COMMENT', 'stdout',
              'TODO','stderr', 'hit', 'DEFINITION', 'KEYWORD', 'ERROR', 'sel')

for tag in valid_tags:
    shell.write(tag+ '\n',tag)
