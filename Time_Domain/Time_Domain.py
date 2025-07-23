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

x = sdr.read_samples(4096)
sdr.close()

plt.plot(x.real)
plt.plot(x.imag)
plt.legend(["I", "Q"])
plt.savefig("../images/rtl_sdr-gain.svg", bbox_inches='tight')
plt.show()
