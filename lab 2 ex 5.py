#ex 5
import numpy as np
import scipy.io.wavfile
import sounddevice

frecventa1 = 440
frecventa2 = 880
durata = 2
amplitudine = 0.5

timp1 = np.linspace(0, durata, int(durata * 44100), endpoint=False)
semnal1 = amplitudine * np.sin(2 * np.pi * frecventa1 * timp1)

timp2 = np.linspace(0, durata, int(durata * 44100), endpoint=False)
semnal2 = amplitudine * np.sin(2 * np.pi * frecventa2 * timp2)

semnal_final = np.concatenate((semnal1, semnal2))

scipy.io.wavfile.write('nume.wav', 44100, semnal_final)

rate, data = scipy.io.wavfile.read('nume.wav')

sounddevice.play(data, rate)
sounddevice.wait()

#Putem observa o schimbare in tonalitate intre cele doua segmente ale semnalului audio,
#datorita diferentei de frecventa.