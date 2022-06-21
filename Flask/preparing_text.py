import pandas as pd

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.corpus import wordnet


### CREATE A CLASS ###

def tokenizer_and_remove_punctuation(row):

    tokens = word_tokenize(row["text"])

    return [token.lower() for token in tokens if token.isalpha()]

def get_wordnet_pos(token):

    tag = nltk.pos_tag([token], lang="eng")[0][1][0].upper()
    tag_dict = {"N": wordnet.NOUN,
                "J": wordnet.ADJ,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)


def lemmatizer_with_pos(row):
    lm = WordNetLemmatizer()

    return [lm.lemmatize(token, get_wordnet_pos(token)) for token in row["tokenized"]]

def remove_sw(row):
    return list(set(row["lemmatized"]).difference(stopwords.words()))


def re_blob(row):
    return " ".join(row["no_stopwords"])

### UNTIL HERE ###


def df_tex_treat(text):
    l_text = [text]
    text_df = pd.DataFrame(l_text, columns=["text"])

    text_df["tokenized"] =  text_df.apply(tokenizer_and_remove_punctuation, axis=1)
    text_df["lemmatized"] = text_df.apply(lemmatizer_with_pos, axis=1)
    text_df["no_stopwords"] = text_df.apply(remove_sw, axis=1)
    text_df["clean_blob"] =  text_df.apply(re_blob, axis = 1)

    return text_df["clean_blob"]