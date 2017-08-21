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


def pdf_scraper():
    string = [
    "import os",
    "import codecs",
    "from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter",
    "from pdfminer.converter import TextConverter",
    "from pdfminer.layout import LAParams",
    "from pdfminer.pdfpage import PDFPage",
    "from cStringIO import StringIO\n",
    "def list_files(directory):",
    "    file_paths = []",
    "    for dirname, dirnames, filenames in os.walk(directory):",
    "        # print path to all filenames.",
    "        for filename in filenames:",
    "            file_paths.append(os.path.join(dirname, filename))",
    "    return file_paths\n",
    "def convert_pdf_to_txt(path):",
    "    rsrcmgr = PDFResourceManager()",
    "    retstr = StringIO()",
    "    codec = 'utf-8'",
    "    laparams = LAParams()",
    "    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)",
    "    fp = file(path, 'rb')",
    "    interpreter = PDFPageInterpreter(rsrcmgr, device)",
    "    password = ''",
    "    maxpages = 0",
    "    caching = True",
    "    pagenos=set()",
    "    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):",
    "        interpreter.process_page(page)",
    "    text = retstr.getvalue()",
    "    fp.close()",
    "    device.close()",
    "    retstr.close()",
    "    return text\n",
    "%%time",
    "with codecs.open('output.txt', 'w') as f:",
    "    files = list_files('folder_input')",
    "    count = len(files)",
    "    completed = 0",
    "    for i in files:",
    "        try:",
    "            text = convert_pdf_to_txt(i)",
    "            f.write(text)",
    "            completed += 1",
    "            print completed, 'of', count, 'textified.'",
    "        except:",
    "            print 'error converting pdf to text'"
    ]
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
