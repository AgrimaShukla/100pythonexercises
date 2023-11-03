import webbrowser

ques = input("Search: ")
webbrowser.open("https://google.com/search?q=%s" %ques)