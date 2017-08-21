def train_test_split():
    string = [
    "from sklearn.cross_validation import train_test_split",
    "train, test, labelsTrain, labelsTest = train_test_split(data, labels, test_size=0.3, random_state=42)",
    ]
    from pygments import highlight
    from pygments.formatters import Terminal256Formatter  # Or TerminalFormatter
    from pygments.lexers import PythonLexer
    # Use Pygments to do syntax highlighting
    lexer = PythonLexer()
    formatter = Terminal256Formatter()
    output = highlight(u'\n'.join(string), lexer, formatter)
    print(output)

def grid_search():
    string = [
    "from sklearn.grid_search import GridSearchCV\n",
    "grid_piping = PipelineClassifier() # Instantiate the classifier.\n",
    "# add parameters to the param grid. ",
    "#NOTE: that there is a handle for each model in the pipeline before the parameter.",
    "# This allows arguments for specific parts of the pipeline to be passed to the grid search.",
    "parameters = {'sgdclassifier__alpha': (1e-2, 1e-3, 1e-4)}\n",
    "# Run the grid search. NOTE: That the .pipe property is used on the instantiated class",
    "# to adjust the models arguments.",
    "gs_clf = GridSearchCV(grid_piping.pipe, parameters, n_jobs=-1, cv=5, scoring='accuracy')\n",
    "# Fit the data.",
    "gs_clf = gs_clf.fit(train, labelsTrain)\n",
    "# Show the results.",
    "print 'Best score =', gs_clf.best_score_",
    "print 'Best params =',gs_clf.best_params_",
    ]
    from pygments import highlight
    from pygments.formatters import Terminal256Formatter  # Or TerminalFormatter
    from pygments.lexers import PythonLexer
    # Use Pygments to do syntax highlighting
    lexer = PythonLexer()
    formatter = Terminal256Formatter()
    output = highlight(u'\n'.join(string), lexer, formatter)
    print(output)

def sklearn_twenty_newsgroups():
    string = [
    "# Import the data",
    "from sklearn.datasets import fetch_20newsgroups",
    "categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']",
    "twenty_train = fetch_20newsgroups(categories=categories, shuffle=True, remove=('headers', 'footers'))",
    "corpus_raw = twenty_train.data",
    "responses = map(lambda x: twenty_train.target_names[x], twenty_train.target)"
    ]
    from pygments import highlight
    from pygments.formatters import Terminal256Formatter  # Or TerminalFormatter
    from pygments.lexers import PythonLexer
    # Use Pygments to do syntax highlighting
    lexer = PythonLexer()
    formatter = Terminal256Formatter()
    output = highlight(u'\n'.join(string), lexer, formatter)
    print(output)
