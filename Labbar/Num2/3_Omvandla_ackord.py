from scipy.io import wavfile as wav
from scipy.fftpack import fft, ifft
import numpy as np
import matplotlib.pyplot as plt

rate, data = wav.read("Cdur.wav")
n = len(data)
t = float(n)/float(rate)

time = np.arange(0, t, t/n)

x = np.arange(0, n)*(rate/n)
frq_data = fft(data)

for i in range(len(x)):
    if x[i] > 640 and x[i] < 680 :
        frq_data[i-75] = frq_data[i]
        frq_data[len(x)-i] = frq_data[i]
        frq_data[i] = 0
        frq_data[len(x) - i] = 0
    if (x[i] > 320 and x[i] < 340):
        frq_data[i - 38] = frq_data[i]
        frq_data[len(x) - i] = frq_data[i]
        frq_data[i] = 0
        frq_data[len(x) - i] = 0

plt.plot(abs(x), abs(frq_data))
plt.show()

new_signal = np.real(ifft(frq_data))
wav.write("new.wav", rate, new_signal*0.00001)

