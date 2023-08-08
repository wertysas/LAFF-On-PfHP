import matplotlib.pyplot as plt
from matplotlib import rcParams
from plot_helpers import read_timings, check_diff


if __name__ == '__main__':
    rcParams["font.family"] = "serif"
    kernels = ["P_Ger_I_Axpy", "P_Ger_J_Axpy"]
    fig, ax = plt.subplots(figsize=(16, 10))

    for kernel in kernels:
        # read timing data
        output = "output_" + kernel + ".txt"
        timings = read_timings(output)
        check_diff(timings)
    
        # plot timing data 
        ax.plot(timings["n"],
                timings["GFLOPS.1"],
                linestyle=(0, (5,5)), # dashed linestlye
                marker='o', # circular marker
                fillstyle='none', # transparent marker
                label=kernel
                )
        ax.set_ylabel('GFlops')
        ax.set_xlabel('Matrix dimension m=n=k')
        ax.legend()
    plt.show()

