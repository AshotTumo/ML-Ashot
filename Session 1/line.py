import matplotlib.pyplot as plt

years = [2010, 2012, 2014, 2016, 2018, 2020]
population = [8.5, 15, 9.8, 10.5, 20, 11.9]

plt.plot(years, population, marker='o', linestyle = '--', color='blue')
plt.xlabel('Year')
plt.ylabel('Population (in billions)')
plt.title('Population growth over years')
plt.show()
