import webbrowser

# build a browser searcher - enter a keyword and use it to search google
# receive a search term from user and open browser with search term

user_term = input("Enter a search term: ").replace(" ", "+")

# open function of webbrowser module, expects parameters: URL, new, and autoraise
webbrowser.open("https://www.google.com/search?q=" + user_term)