import spacy
nlp = spacy.load('en')
from spacy import en

#def punct_space(token):
    #return token.is_punct or token.is_space

def spaCy_parser_en(corpus):
    """Holds corpus in memory. Modify template function if corpus too large."""
    holder = []
    for doc in nlp.pipe(corpus, batch_size=1000, n_threads=4):
        #lem_doc = [token.lemma_ for token in doc if not punct_space(token)]     # lemmatize,
        lem_doc = [token.lemma_ for token in doc if not token.is_punct or token.is_space]     # lemmatize,
                                                                                # remove punctuation,
                                                                                # remove whitespace
        stop_doc = [term for term in lem_doc if term not in spacy.en.STOPWORDS] # remove stopwords.
        clean_doc = u' '.join(stop_doc)
        holder.append(clean_doc)
    return holder

def spaCy_name_joiner(corpus):
    """Holds corpus in memory. Modify template function if corpus too large."""
    holder = []
    for doc in nlp.pipe(corpus, batch_size=1000, n_threads=4):
        match = 0
        holder = 0
        sentence = []
        for token in doc:
            if token.ent_type_ == u"PERSON":
                if match == 1:
                    name = u'_'.join([holder, token.orth_])
                    sentence.append(name)
                    match = 0
                else:
                    match = 1
                    holder = token.orth_
            elif match == 1:
                sentence.append(holder)
                sentence.append(token.orth_)
                holder = 0
                match = 0
            else:
                sentence.append(token.orth_)
        holder.append(u' '.join(sentence))
    return holder
