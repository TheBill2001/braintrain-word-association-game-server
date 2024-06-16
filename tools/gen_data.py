from gensim.models import KeyedVectors
import sys
import numpy as np
import os
import pathlib

def read_vectors(file: str) -> list[np.array]:
    vectors = []
    with open(file, "r") as f:
        for line in f:
            vectors.append(np.array([float(v) for v in line.strip().split()]))
    return vectors

def read_lines(file: str):
    return [line.strip() for line in open(file, "r") if line]


current_dir = pathlib.Path(__file__).parent.resolve()

vectors = read_vectors(
    os.path.join(current_dir, "../word2vec/out/vectors.tsv")
)

keys = read_lines(os.path.join(current_dir, "../word2vec/out/metadata.tsv"))

key_vectors = KeyedVectors(len(vectors[0]))
key_vectors.add_vectors(keys=keys, weights=vectors)

all_sims = key_vectors.most_similar("gia đình", topn=sys.maxsize)

# last_10 = list(reversed(all_sims[-10:]))
# print(last_10)

temp_1 = [t for t in all_sims if t[1] < 0.5]
# temp_2 = list(reversed(temp_1[-10:]))
print(temp_1[:10])