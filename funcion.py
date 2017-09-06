import numpy as np
import matplotlib.pyplot as plt
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)
t1=np.arange(0.0,5.0,0.1)
t2=np.arange(0.0,5.0,0.02)
plt.figure(1)
plt.subplot(211)
plt.plot(t1,f(t1),'ro',t2,f(t2),'y-')
plt.subplot(212)
plt.plot(t1,np.cos(2*np.pi*t1),'k--')
plt.savefig('dosgraficas.png')
plt.show()

