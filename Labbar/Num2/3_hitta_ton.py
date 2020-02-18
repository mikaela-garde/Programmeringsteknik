from scipy.io import wavfile as wav
from scipy.fftpack import fft, ifft
import numpy as np
import matplotlib.pyplot as plt

fil = input("Vilken fil vill du läsa in?")

rate, data = wav.read(fil+".wav")
n = len(data)
t = float(n)/float(rate)

time = np.arange(0, t, t/n)

x = np.arange(0, n)*rate/n
frq_data = fft(data)
max_amp = np.argmax(abs(frq_data))
frq = x[max_amp]

def name_of_tone(frq):
    tone = ""
    while frq >= 880 or frq < 440:
        if frq < 440:
            frq = frq * 2
        elif frq >= 880:
            frq = frq / 2
    if frq < 453:
        tone = "A"
    elif frq < 480:
        tone = "A#"
    elif frq < 509:
        tone = "B"
    elif frq < 538:
        tone = "C"
    elif frq < 570:
        tone = "C#"
    elif frq < 605:
        tone = "D"
    elif frq < 640:
        tone = "D#"
    elif frq < 679:
        tone = "E"
    elif frq < 720:
        tone = "F"
    elif frq < 762:
        tone = "F#"
    elif frq < 807:
        tone = "G"
    elif frq < 855:
        tone = "A"
    elif frq < 880:
        tone = "A#"
    return tone

print("Ton:" + name_of_tone(frq))