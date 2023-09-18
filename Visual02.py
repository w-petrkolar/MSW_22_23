import csv
import matplotlib.pyplot as plt

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

# print(means)

# Sloupcový graf
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.figure(figsize=(10, 6))  # Figure size
sloupce = plt.bar(months, means, color='skyblue')
plt.xlabel('Měsíc')
plt.ylabel('Průměrné srážky (mm)')
plt.title('Průměrné měsíční srážky')
plt.xticks(months, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid(axis='y')

for bar, mean in zip(sloupce, means):   # přidá popisky na vrchol sloupce
    zobraz = "{:.2f}".format(mean)  # zaokrouhlí na 2 des místa
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, str(zobraz), fontsize=10, ha='center')
    # vyhledá střed sloupce                        a výšku sloupce  pro pozici zobrazení popisku
plt.tight_layout()
plt.show()
