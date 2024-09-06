# This code implements a simple browser search. It is a Google searcher. Ask for an input from user and search for
# that input in google

import webbrowser

user_term = input("Enter a search term: ").replace(" ", "+")

webbrowser.open("https://www.google.com/search?q=" + user_term)

