def line_generator_template():
    string = [
    "import codecs",
    "def line_review(filename):",
    "    with codecs.open(filename, encoding='utf_8') as f:",
    "        for review in f:",
    "            yield review.replace('\\\\n', '\\n')"
    ]
    from pygments import highlight
    from pygments.formatters import Terminal256Formatter  # Or TerminalFormatter
    from pygments.lexers import PythonLexer
    # Use Pygments to do syntax highlighting
    lexer = PythonLexer()
    formatter = Terminal256Formatter()
    output = highlight(u'\n'.join(string), lexer, formatter)
    print(output)


def array_to_txt_template():
    string = [
    "import codecs",
    "with codecs.open(output_filepath, 'w', encoding='utf_8') as f:",
    "    for line in list_holder:",
    "        f.write(u' '.join(line) + '\\n')"
    ]
    from pygments import highlight
    from pygments.formatters import Terminal256Formatter  # Or TerminalFormatter
    from pygments.lexers import PythonLexer
    # Use Pygments to do syntax highlighting
    lexer = PythonLexer()
    formatter = Terminal256Formatter()
    output = highlight(u'\n'.join(string), lexer, formatter)
    print(output)
