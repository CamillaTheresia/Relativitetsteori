import numpy as np
import matplotlib.pyplot as plt

#Indlæser data for cepheiden V1 (tid som funktion af den tilsyneladende lyssttyrke mellem V1 og S1)
tid, m = np.loadtxt('data.txt',unpack=True, skiprows=1)

#Plotter data
plt.figure()
plt.xlabel('Tid [dage]')
plt.ylabel('Tilsyneladende lysstyrke')
plt.plot(tid,m)
plt.savefig('lysstyrke.pdf')

#Finder perioden med et faseplot
P = 3.78
phase = tid%P

#Plotter data som funktion af fasen
plt.figure()
plt.xlabel('Tid [dage]')
plt.ylabel('Tilsyneladende størrelsesklasse')
plt.plot(phase,m,'o')
plt.savefig('faseplot.pdf')

#Absolut størelsesklasse
M = -2.43*(np.log10(P)-1)-4.05
print('M = ',M)

#Lysstyrke
L = 3.0128*10**(28)*10**(-0.4*M) #Watt

#Flux
F = 1.36*10**(-14) #W/M^2

#Afstand
d = np.sqrt(L/(4*np.pi*F))/(3.0857*10**(16)) #parsec
print('Afstand = ', d, ' parsec')