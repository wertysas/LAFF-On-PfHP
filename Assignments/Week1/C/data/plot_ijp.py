import os.path as path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

data_file = path.join(path.dirname(__file__), "output_IJP.txt")

timings = pd.read_csv(data_file, comment="#", header=0, delim_whitespace=True)

# Maximmum difference
max_diff = timings["diff"].abs().max()
assert max_diff < 1e-10, "Hmmm, better check if there is an accuracy problem"


rcParams["font.family"] = "serif"

fig, ax = plt.subplots(figsize=(16, 10))
ax.plot(timings["n"], timings["time.1"])
ax.set_ylabel('Time (in sec.)')
ax.set_xlabel('Matrix dimension m=n=k')
plt.show()
