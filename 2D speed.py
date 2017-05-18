#In this second part of the case study, we are going to #visualize 2D speed vs Frequency for the gull named “Eric”.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
 
# storing the indices of the bird Eric
ix = birddata.bird_name == "Eric"
speed = birddata.speed_2d[ix]
 
plt.figure(figsize = (8,4))
ind = np.isnan(speed)
plt.hist(speed[~ind], bins = np.linspace(0,30,20), normed=True)
plt.xlabel(" 2D speed (m/s) ")
plt.ylabel(" Frequency ")
plt.show()