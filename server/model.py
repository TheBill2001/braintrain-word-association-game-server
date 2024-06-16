from gensim.models import KeyedVectors
# import numpy as np
import pathlib
import os

from underthesea import text_normalize

__current_dir = pathlib.Path(__file__).parent.resolve()
        
INSTANCE = KeyedVectors.load(os.path.join(__current_dir, "model.bin"), mmap='r')
        
__CATEGORIES : dict[str, list[str]] = dict()
with open(os.path.join(__current_dir, "categories.txt"), "r") as f:
    for line in f:
        l = [w.strip() for w in line.split(",")]
        __CATEGORIES[l[0]] = l
        
CATEGORIES = [cat for cat in list(__CATEGORIES.keys())]
VOCABULARY = INSTANCE.wv.key_to_index.keys()

def get_category_positive(cat: str):
    if not cat in __CATEGORIES:
        return None
    
    return __CATEGORIES[cat]

def is_word_in_vocab(word):
    word = text_normalize(word)
    return word in VOCABULARY