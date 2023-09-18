# Lotka-Voltera model, řešení obyčejných diferenciálních rovnic

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# rovnice modelu Lotka-Volterra
def lv_model(y, t, a, b, c, p):
    Z, L = y
    dZdt = a * Z - b * Z * L
    dLdt = -c * L + p * Z * L
    return [dZdt, dLdt]


# Počáteční podmínky
Z1 = 50  # Počáteční populace zajíců
L1 = 5   # Počáteční populace lišek
a = 0.1  # koeficient množení zajíců
b = 0.05  # koeficient predace
c = 0.3  # koeficient úhynu lišek
p = 0.01  # koeficient množení lišek na jednoho zajíce

# Body na časové ose
t = np.linspace(0, 200, 500)   # počátek, konec, počet bodů

# Řešení rovnic
y0 = [Z1, L1]
solution = odeint(lv_model, y0, t, args=(a, b, c, p))
Z, L = solution.T   # uloží řešení jako 2 seznamy L a Z


# Vykreslení grafu
plt.figure(figsize=(12, 6))   # velikost plochy grafu
plt.plot(t, Z, label="Zajíci")
plt.plot(t, L, label="Lišky")
plt.xlabel("Čas")
plt.ylabel("Populace")
plt.title("Populační dynamika lišek a zajíců")
plt.legend()
plt.grid(True)
plt.show()
