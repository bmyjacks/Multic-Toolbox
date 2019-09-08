#! python3
#HOStudio
#LICENSE MIT
#Version:V0.0.1
#Usage:
#   python3 mcb.py save <keyword> -Save clipboard to keyword.
#   python3 mcb.py <keyword> -Loads keyword to clipboard.
#   python3 mcb.py list -Loads all keywords to clipboard


import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2] ] = pyperclip.paste()
elif len (sys.argv) == 2:
    #List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
