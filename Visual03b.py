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
cmap = plt.colormaps['rainbow']  # načte barevnou mapu z matplotlib
normalize = plt.Normalize(min(means), max(means))
colors = cmap(normalize(means))
# nebo
# colors = cmap(np.linspace(0, 1, len(means)))    # vybere pravidelně 12 barev, rozdělí 0-1 na 12 dílů (12 je len(means)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Create a pie chart with lines between sections
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(means, labels=None, autopct='%1.1f%%', startangle=110, colors=colors, wedgeprops={'linewidth': 1, 'edgecolor': 'black'})



plt.title('Průměrné zastoupení srážek')

plt.tight_layout()
plt.show()