import numpy as np
import matplotlib.pyplot as plt


data = np.genfromtxt('data1.csv', delimiter=';')

with open('data1.csv', 'r') as file:
    header = file.readline().strip().split(';')


column1_name = str(header[0])
column4_name = str(header[3])
column10_name = str(header[9])


column1 = data[:, 0]
column4 = data[:, 3]
column10 = data[:, 9]

# Грпфики зависимости
plt.figure(figsize=(12, 6))


plt.scatter(column1, column4, edgecolor='k', alpha=0.7, label=f'{column1_name} относительно {column4_name}')


plt.scatter(column1, column10, edgecolor='r', alpha=0.7, label=f'{column1_name} относительно {column10_name}')

plt.legend()
plt.title('Наложенные графики зависимости')
plt.xlabel(column1_name)
plt.ylabel(f'Значения {column4_name} и {column10_name}')
plt.grid(True)

# Грпфик корреляции
correlation = np.corrcoef(column4, column10)[0, 1]


plt.figure(figsize=(6, 6))
plt.scatter(column4, column10, edgecolor='k', alpha=0.7)
plt.title(f'График корреляции между {column4_name} и {column10_name} ')
plt.xlabel(column4_name)
plt.ylabel(column10_name)
plt.grid(True)


plt.tight_layout()
plt.show()
