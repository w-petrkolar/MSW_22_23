import csv
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

csv_data = []

# Načtení dat z csv
with open('barcelona_precipitations_1786.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')
    next(csv_reader)    # přeskočí první řádek

    for row in csv_reader:
        csv_data.append(row)

# Průměry měsíců
means = []

for i in range(1, 13):  # první je rok, ne data
    hodnota = [float(row[i]) for row in csv_data]  # zapíše hodnotu daného řádku (roku)
    prumer = sum(hodnota) / len(csv_data)  # Spočítá průměr
    means.append(prumer)

# Koláčový graf
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.figure(figsize=(8, 8))  # Figure size
plt.pie(means, labels=months, autopct='%1.1f%%', startangle=110, colors=plt.cm.Paired.colors)
                                                                        # automaticky generuje "pěkné" barvy
plt.title('Průměrné zastoupení srážek')

plt.tight_layout()
plt.show()