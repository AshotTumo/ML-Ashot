import matplotlib.pyplot as plt
import random

random.seed(42)
data = [random.normalvariate(0, 1) for _ in range(1000)]

plt.hist(data, bins=30, color='green', alpha=.7)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Title')
plt.show()
