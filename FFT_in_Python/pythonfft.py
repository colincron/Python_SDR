import numpy as np
import matplotlib.pyplot as plt 

t = np.arange(100)
s = np.sin(0.15*2*np.pi*t)

S = np.fft.fft(s)
# print(S) 

S_mag = np.abs(S)
S_phase = np.angle(S)
plt.plot(t,S_mag,'.-')
plt.savefig("../images/fftmagnitude.svg", bbox_inches='tight')
plt.clf()
plt.plot(t,S_phase,'.-')
plt.savefig("../images/fftphase.svg", bbox_inches='tight')
