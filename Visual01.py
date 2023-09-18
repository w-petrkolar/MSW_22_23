import csv
import matplotlib.pyplot as plt

csv_data = []

# Načtení dat z csv
with open('barcelona_precipitations_1786.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')

    for row in csv_reader:
        csv_data.append(row)

# Graf 1
# Celkové srážky každý rok
uhrn = {}

for row in csv_data[1:]:  # Až od druhého řádku, první jsou nadpisy tabulky
    rok = row[0]  # první hodnota je rok
    srazky = [float(x) for x in row[1:]]  # Ostatní hodnoty jsou čísla
    suma_srazek = sum(srazky)  # spočte sumu
    uhrn[rok] = suma_srazek  # uloží do slovníku

roky = list(uhrn.keys())
uhrny = list(uhrn.values())

# Vykreslí graf
plt.figure(figsize=(10, 6))  # Rozměr grafu
plt.plot(roky, uhrny, marker='o', color='blue', linestyle='-', markersize=2, label='Srážky')
plt.xlabel('Rok')
plt.ylabel('Srážky (mm)')
plt.title('Roční srážky')
plt.grid(True)
plt.legend()

xticks = [rok for rok in roky if int(rok) % 20 == 0]    # zobraz roky v kroku 20
plt.xticks(xticks)

plt.tight_layout()
plt.show()
