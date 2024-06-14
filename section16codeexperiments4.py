import webbrowser

# will build a good searcher - enter a keyword and use it to search google

user_term = input("Enter a search term: ").replace(" ", "+")

webbrowser.open("http://www.google.com/search?q=" + user_term)
