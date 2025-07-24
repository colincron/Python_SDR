from rtlsdr import RtlSdr
import numpy as np
import matplotlib.pyplot as plt 

sdr = RtlSdr()
sdr.sample_rate = 2.048e6 #Hz
sdr.center_freq = 100e6 #Hz
sdr.freq_correction = 60 #Hz
print(sdr.valid_gains_db)
sdr.gain = 49.6
print("SDR Gain: " + str(sdr.gain))

fft_size = 512
num_rows = 500
x = sdr.read_samples(2048) # get rid of initial empty samples
x = sdr.read_samples(fft_size*num_rows) # get all the samples we need for the spectrogram
spectrogram = np.zeros((num_rows, fft_size))
for i in range(num_rows):
    spectrogram[i,:] = 10*np.log(np.abs(np.fft.fftshift(np.fft.fft(x[i*fft_size:(i+1)*fft_size])))**2)
extent = [(sdr.center_freq + sdr.sample_rate/-2)/1e6,
            (sdr.center_freq + sdr.sample_rate/2)/1e6,
            len(x)/sdr.sample_rate, 0]
sdr.close()
plt.imshow(spectrogram, aspect='auto', extent=extent)
plt.xlabel("Frequency [MHz]")
plt.ylabel("Time [s]")
plt.savefig("../images/spectrogram.svg", bbox_inches='tight')
plt.show()