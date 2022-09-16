import matplotlib.pyplot as plt

time = [i for i in range(0,19)]
pn = [5,18,29,47,71,119,174,257,350,441,513,559,594,629,640,651,655,659,663]
plt.title('model')
plt.xlabel('time')
plt.ylabel('number')
plt.plot(time, pn)
plt.show()