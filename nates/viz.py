def packages():
    string = [
    "import seaborn as sns",
    "import matplotlib.pyplot as plt",
    "%matplotlib inline",
    "plt.style.use('fivethirtyeight')"
    ]
    from pygments import highlight
    from pygments.formatters import Terminal256Formatter  # Or TerminalFormatter
    from pygments.lexers import PythonLexer
    # Use Pygments to do syntax highlighting
    lexer = PythonLexer()
    formatter = Terminal256Formatter()
    output = highlight(u'\n'.join(string), lexer, formatter)
    print(output)

def text_label_scatter_plot_template():
    string = [
    "y=[0,2,3,4,6]",
    "z=[7,3,4,1,3]",
    "n=['a','b','c','d','e']",
    "fig, ax = plt.subplots(figsize=(10,10))",
    "ax.scatter(z, y)",
    "for i, txt in enumerate(n):",
    "    ax.annotate(txt, (z[i],y[i]))",
    "plt.savefig('output.png')",
    "plt.show()"
    ]
    from pygments import highlight
    from pygments.formatters import Terminal256Formatter  # Or TerminalFormatter
    from pygments.lexers import PythonLexer
    # Use Pygments to do syntax highlighting
    lexer = PythonLexer()
    formatter = Terminal256Formatter()
    output = highlight(u'\n'.join(string), lexer, formatter)
    print(output)
