import scipy.io.wavfile
import scipy.fftpack
import matplotlib.pyplot as plt

rate, data = scipy.io.wavfile.read("Piano_2.wav")
fft = scipy.fftpack.fft(data)

plt.plot(abs(fft))
plt.show()