import csv
import matplotlib.pyplot as plt

csv_data = []

# Načtení dat z csv
with open('barcelona_precipitations_1786.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')
    next(csv_reader)  # přeskočí první řádek

    for row in csv_reader:
        csv_data.append(row)

kumulace = []
kum = float(0)
for i in range(len(csv_data)):
    rok = 0
    for j in range(1, len(csv_data[i])):
        rok = rok + float(csv_data[i][j])

    kum = kum + rok
    kumulace.append(kum)




# Vykreslí graf
osa_x = range(1786, 1786 + len(kumulace))
plt.figure(figsize=(10, 6))  # Rozměr grafu
plt.plot(osa_x, kumulace, marker='o', color='blue', linestyle='-', markersize=0, label='Srážky')
plt.xlabel('Rok')
plt.ylabel('Srážky (mm)')
plt.title('Roční srážky')
plt.grid(True)
plt.legend()

xticks = [rok for rok in osa_x if int(rok) % 10 == 0]    # zobraz roky v kroku 20
plt.xticks(xticks, rotation = 45)

plt.tight_layout()
plt.show()