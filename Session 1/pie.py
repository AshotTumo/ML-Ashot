import matplotlib.pyplot as plt

categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5']
persentiges = [25, 30, 15, 30, 5]

explode = [0, 0.1, 0, 0, .2]
colors = ['red', 'blue', 'green', 'orange', 'black']

plt.pie(persentiges, explode=explode, labels= categories, colors=colors, shadow= True)
plt.title('Persantage Destribution')
plt.legend(categories)
plt.show()
