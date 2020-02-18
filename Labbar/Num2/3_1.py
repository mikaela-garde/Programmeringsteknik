from scipy.io import wavfile as wav
from scipy.fftpack import fft, ifft
import numpy as np
import matplotlib.pyplot as plt

rate, data = wav.read("Piano_1_C.wav")
n = len(data)
t = float(n)/float(rate)

time = np.arange(0, t, t/n)
plt.plot(time, data)
plt.show()

frq = fft(data)
x = np.arange(0, n)*rate/n

plt.plot(abs(x[0:int(n/2)]), abs(frq[0:int(n/2)]))

plt.show()
