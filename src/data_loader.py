import pandas as pd

def load_features(path):
    return pd.read_csv(path, sep='\s+', header=None)

def load_labels(path):
    return pd.read_csv(path, header=None)
