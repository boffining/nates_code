#from __future__ import absolute_import;
def w2v():
    """ Prints gensim word2vec template"""
    string = [
    "from gensim.models import Word2Vec\n",
    "parsed_sents = LineSentence('txt_filepath')",
    "word2vec_local_filepath = 'intermediate/word2vec_model_all'",
    "sent_count = len([i for i in parsed_sents])\n",
    "# the code below can be time consuming so set to true if you want to train the model.",
    "if 1 == 0:",
    "    import logging",
    "    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',level=logging.INFO)",
    "    # initiate the model and perform the first epoch of training",
    "    localvec = Word2Vec(parsed_sents, size=50, window=10, min_count=5, workers=4)",
    "    localvec.save(word2vec_local_filepath)",
    "    # perform another 24 epochs of training",
    "    for i in range(24):",
    "        localvec.train(parsed_sents, total_examples=sent_count, epochs=localvec.iter)",
    "        localvec.save(word2vec_local_filepath)\n",
    "# load the finished models from disk",
    "localvec = Word2Vec.load(word2vec_local_filepath)",
    "localvec.init_sims()",
    "print u'localvec, {} training epochs so far.'.format(localvec.train_count)"
    ]
    from pygments import highlight
    from pygments.formatters import Terminal256Formatter  # Or TerminalFormatter
    from pygments.lexers import PythonLexer
    # Use Pygments to do syntax highlighting
    lexer = PythonLexer()
    formatter = Terminal256Formatter()
    output = highlight(u'\n'.join(string), lexer, formatter)
    print(output)


def most_similar():
    """Prints a function for finding the most cosine similar words in an array."""
    string = [
    "def most_similar(word, a_input, v_input):",
    "    idi = v_input.index(word)",
    "    results = []",
    "    for idx, i in enumerate(a_input):",
    "        if idx != idi:",
    "            results.append((1-cosine(a_input[idi,:], a_input[idx,:]), v_input[idx]))",
    "    for x in sorted(results)[::-1][0:25]:",
    "        print x[0], x[1]"
    ]
    from pygments import highlight
    from pygments.formatters import Terminal256Formatter  # Or TerminalFormatter
    from pygments.lexers import PythonLexer
    # Use Pygments to do syntax highlighting
    lexer = PythonLexer()
    formatter = Terminal256Formatter()
    output = highlight(u'\n'.join(string), lexer, formatter)
    print(output)


def sentence_joiner():
    "Prints custom function to undo wrapped text."
    string = [
    "# find the first sentence ending punctuation.",
    "    # The first letter of that word should not be capitalized.",
    "    # The next word should be capitalized.",
    "    # Run a test to detect titles of people and proper noun places.",
    "# Continually concat new words to that capitalized word until sentence end is detected.\n",
    "def sentence_joiner(doc_holder_input):",
    "    sent_ends = ['.', '!', '?', '..', '."', ".'", '!"', "!'", '?"', "?'"]",
    "    doc_joined = []",
    "    sent_hold = []",
    "    for i in doc_holder_input:",
    "        doc = u' '.join(i.split()) # removes trailing spaces and blank lines.",
    "        if len(doc) > 0:",
    "            line = doc.split()",
    "            # find the first sent-ending punct.",
    "            for idl, l in enumerate(line):",
    "                end = l[-2:]",
    "                if len([x for x in sent_ends if x in end]) > 0:",
    "                    if len(line) == idl+1:",
    "                        sent_hold.append(l[:-1])",
    "                        doc_joined.append(u' '.join(sent_hold).lower())",
    "                        sent_hold = []",
    "                    elif line[idl+1][0].isupper() == True:",
    "                        if l[0].isupper() == True:",
    "                            if len(l) < 5:",
    "                                if l[:-1].isupper() == True: # Catch all caps short words like 'UK', and 'EU'.",
    "                                    sent_hold.append(l[:-1])",
    "                                    doc_joined.append(u' '.join(sent_hold).lower())",
    "                                    sent_hold = []",
    "                                else:",
    "                                    sent_hold.append(l)",
    "                            elif line[idl-1][0].isupper() == True: # Check for title, else its probably the end.",
    "                                if len(line[idl-1]) < 5:",
    "                                    sent_hold.append(l)",
    "                                else:",
    "                                    sent_hold.append(l[:-1])",
    "                                    doc_joined.append(u' '.join(sent_hold).lower())",
    "                                    sent_hold = []",
    "                            else:",
    "                                sent_hold.append(l[:-1])",
    "                                doc_joined.append(u' '.join(sent_hold).lower())",
    "                                sent_hold = []",
    "                        else:",
    "                            sent_hold.append(l[:-1])",
    "                            doc_joined.append(u' '.join(sent_hold).lower())",
    "                            sent_hold = []",
    "                    else:",
    "                        sent_hold.append(l)",
    "                else:",
    "                    sent_hold.append(l)",
    "    return doc_joined"
    ]
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


def make_tfidf_corpus():
    string = [
    "from textblob import TextBlob",
    "from collections import Counter",
    "import math\n",
    "def corpus_counter(corpus): # Run TFIDF on the vocabulary before you feed it into the algorithm.",
    "    holder = []",
    "    counter = 0",
    "    for i in corpus:",
    "        x = i.split()",
    "        holder += x",
    "        counter += 1",
    "    return holder\n",
    "def make_bloblist(column): # get a bloblist for the text using textblob.",
    "    holder = []",
    "    for i in column:",
    "        doc = TextBlob(i)",
    "        holder.append(doc)",
    "    return holder\n",
    "def tfidf_blob_speed_check(bloblist, n_containing_lookup):",
    "    status = 0",
    "    batch = 0",
    "    holder = []",
    "    for blob in bloblist:",
    "        holdera = []",
    "        for word in blob.split():",
    "            try:",
    "                tf = (float)(blob.words.count(word)) / (float)(len(blob.words))  # get the term freqency",
    "                n_containing = n_containing_lookup.get(word)                     # get the n_docs containing the word",
    "                idf = math.log(len(bloblist) / (float)(1 + n_containing))        # calculate the idf, also note we're adding 1 to the n_containing.",
    "                tfidf = tf * idf                                                 # calculate the tfidf",
    "                holdera.append((word,tfidf))                                     # add the word and tfidf score to a list",
    "            except:",
    "                continue",
    "        holder.append(holdera)                                                   # append the sentence with tfidf scores to holder.",
    "        status += 1",
    "        if status == 100000:",
    "            batch += status",
    "            status = 0",
    "    return holder\n",
    "def get_tfidf_corpus(corpus):",
    "    corpus_processed = [u' '.join(i) for i in corpus]",
    "    doc_counter = corpus_counter(corpus_processed)",
    "    term_doc_freq = Counter(doc_counter)",
    "    n_containing_lookup = dict(term_doc_freq)",
    "    bloblist = make_bloblist(corpus_processed)",
    "    tfidfs = tfidf_blob_speed_check(bloblist, n_containing_lookup)",
    "    return tfidfs"
    ]
    from pygments import highlight
    from pygments.formatters import Terminal256Formatter  # Or TerminalFormatter
    from pygments.lexers import PythonLexer
    # Use Pygments to do syntax highlighting
    lexer = PythonLexer()
    formatter = Terminal256Formatter()
    output = highlight(u'\n'.join(string), lexer, formatter)
    print(output)
