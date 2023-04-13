import os

K_NEIGHBORS = 10

MODEL_OUTPUT = f'{os.path.abspath(".")}/models/knn_.bin'

MODEL_INPUT = f'{os.path.abspath(".")}/data/data_by_artist.csv'

LOOKUP_TABLE = f'{os.path.abspath(".")}/data/train_lookup.csv'

MASTER_TABLE = f'{os.path.abspath(".")}/data/data.csv'