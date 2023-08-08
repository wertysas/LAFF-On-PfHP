import os.path as path
import pandas as pd


def read_timings(output_file):
    data_file = path.join(path.dirname(__file__), output_file)
    return pd.read_csv(data_file, comment="#", header=0, delim_whitespace=True)


def check_diff(timings, threshold=1e-10):
    print(timings)
    max_diff = timings["diff"].abs().max()
    assert max_diff < threshold, "Hmmm, better check if there is an accuracy problem"


