import matplotlib.pyplot as plt

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sample Graph!")

plt.plot([1, 2, 3], [2, 4, 1], 'b')
plt.axis([1, 3, 1, 4])

plt.show()