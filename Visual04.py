import csv
import matplotlib.pyplot as plt

csv_data = []

# Načtení dat z csv
with open('barcelona_precipitations_1786.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')
    next(csv_reader)  # přeskočí první řádek
    for row in csv_reader:
        csv_data.append(row)

roky = [item[0] for item in csv_data]

jul = [float(item[7]) for item in csv_data]
oct = [float(item[10]) for item in csv_data]




# Vykreslí graf
plt.figure(figsize=(10, 6))  # Rozměr grafu
plt.plot(roky, jul, marker='o', color='blue', linestyle='-', markersize=1, label='Jul')
plt.plot(roky, oct, marker='o', color='red', linestyle='-', markersize=1, label='Oct')
plt.xlabel('Rok')
plt.ylabel('Srážky (mm)')
plt.title('Červen / Říjen')
plt.grid(True)
plt.legend()

xticks = [rok for rok in roky if int(rok) % 20 == 0]    # zobraz roky v kroku 20
plt.xticks(xticks)

plt.tight_layout()
plt.show()