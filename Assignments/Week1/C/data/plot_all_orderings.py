import os.path as path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams



def read_timings(output_file):
    data_file = path.join(path.dirname(__file__), output_file)
    return pd.read_csv(data_file, comment="#", header=0, delim_whitespace=True)


def check_diff(timings, threshold=1e-10):
    print(timings)
    max_diff = timings["diff"].abs().max()
    assert max_diff < threshold, "Hmmm, better check if there is an accuracy problem"





if __name__ == '__main__':
    rcParams["font.family"] = "serif"
    orders = ["IJP", "IPJ", "JIP", "JPI", "PIJ", "PJI"]
    fig, ax = plt.subplots(figsize=(16, 10))

    for order in orders:
        # read timing data
        output = "output_" + order + ".txt"
        timings = read_timings(output)
        check_diff(timings)
    
        # plot timing data 
        ax.plot(timings["n"],
                timings["GFLOPS.1"],
                linestyle=(0, (5,5)), # dashed linestlye
                marker='o', # circular marker
                fillstyle='none', # transparent marker
                label=order
                )
        ax.set_ylabel('GFlops')
        ax.set_xlabel('Matrix dimension m=n=k')
        ax.legend()
    plt.show()
