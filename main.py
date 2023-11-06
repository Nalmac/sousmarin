from sub import SousMarin
from ballast import Ballast
import matplotlib.pyplot as plt
import numpy as np

ballast = Ballast(1e-3, 1e-4)
s = SousMarin([ballast], 0.5, 1.5e-3)

test = s.plongee(5)

T = np.arange(0, 10, 0.02)