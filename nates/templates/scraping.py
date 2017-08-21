def packages():
    """ Prints common packages for scraping."""
    string = ['from bs4 import BeautifulSoup',
            'import requests',
            'import urllib',
            'from time import sleep',
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

def OMDB_plot_scraper():
    string = [
    "import requests",
    "from time import sleep",
    "def OMDB_plot_scraper(movie_id):",
    "    r = requests.get('http://www.omdbapi.com/?i='+movie_id+'&plot=full&r=json')",
    "    info = r.json()",
    "    if info['Response'] == 'True':",
    "        sleep(float(round(random.uniform(0.5, 1.9),1)))",
    "        return (info['Plot'])",
    "    else:",
    "        return 'NONE'\n",
    "plot_holder = [get_plot_data(i) for i in df.movie_id]",
    ]
    from pygments import highlight
    from pygments.formatters import Terminal256Formatter  # Or TerminalFormatter
    from pygments.lexers import PythonLexer
    # Use Pygments to do syntax highlighting
    lexer = PythonLexer()
    formatter = Terminal256Formatter()
    output = highlight(u'\n'.join(string), lexer, formatter)
    print(output)
