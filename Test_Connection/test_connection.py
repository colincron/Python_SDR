from rtlsdr import RtlSdr

sdr = RtlSdr()
sdr.sample_rate = 2.048e6 #Hz
sdr.center_freq = 93.1e6 #Hz
sdr.freq_correction = 60 #ppm
sdr.gain = 'auto'

print(len(sdr.read_samples(1024)))
sdr.close()