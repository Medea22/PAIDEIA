import pickle
from click import secho
import pandas as pd
from preparing_text import df_tex_treat


def vct_df(bow_array, bow_model):

    df_bow = pd.DataFrame(bow_array, columns=bow_model.get_feature_names_out())
    return df_bow


def dic_models():
    # files = os.listdir('BOWVect')
    # bow_model_names = [model_name for model_name in files if model_name != '.DS_Store']
    
    bow_model_names = {'W': 'bv_ssat.p',
                        'V': 'bv_med.p',
                        'T': 'bv_ep.p',
                        'Z' : 'bv_am.p',
                        'X': 'bv_be.p',
                        'U': 'bv_lc.p', 
                        'Y': 'bv_kf.p'}

    km_model_names = {'W': 'km_ssat.p',
                    'V': 'km_med.p',
                    'T': 'km_ep.p',
                    'Z' : 'km_am.p',
                    'X': 'km_be.p',
                    'U': 'km_lc.p', 
                    'Y': 'km_kf.p'}


    return bow_model_names, km_model_names


def get_cluser(genere = '', text=''):

    genere = genere.upper()

    data = pd.read_pickle('data/books_with_section.p')

    data_g = data[data['section'] == genere]

    text_df = df_tex_treat(text)
    
    bow_di, km_di = dic_models()

    bow = bow_di[genere]
    km = km_di[genere]

    bow_v = pickle.load(open(f'BOWVect/{bow}', 'rb'))
    km_mode = pickle.load(open(f'KMModels/{km}', 'rb'))
    
    X = bow_v.transform(text_df).toarray()
    bow_df = vct_df(X, bow_v)
    
    pred = km_mode.predict(bow_df)[0]

    section_df_by_g = data_g[data_g['class'] == pred]
    column_names = ["title", "authors", "year", "Genre", "section", "shelf", "id", "description", "format"]
    section_df_by_g = section_df_by_g[column_names]
    section_df_by_g["year"] = section_df_by_g["year"].astype("int")
    section_df_by_g["shelf"] = section_df_by_g["shelf"].astype("int")
    return section_df_by_g.sample(n=5)


