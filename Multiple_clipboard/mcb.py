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


#TODO: List keywords and load content

mcbShelf.close()
