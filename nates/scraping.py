def packages():
    """ Prints common packages for scraping."""
    string = ['from bs4 import BeautifulSoup',
            'import requests',
            'import urllib',
            'from selenium import webdriver',
            'from selenium.webdriver.common.keys import Keys',
            'from selenium.webdriver.support.ui import Select',
            'chrome_options = webdriver.ChromeOptions()',
            "chrome_options.add_argument('--incognito')"]
    from pygments import highlight
    from pygments.formatters import Terminal256Formatter  # Or TerminalFormatter
    from pygments.lexers import PythonLexer
    # Use Pygments to do syntax highlighting
    lexer = PythonLexer()
    formatter = Terminal256Formatter()
    output = highlight(u'\n'.join(string), lexer, formatter)
    print(output)
