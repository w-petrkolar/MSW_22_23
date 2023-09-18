import random

# Pravděpodobnost stavu počasí další den na základě předchozího
pravdepodobnost = {
    "Dest": {"Dest": 0.2, "Slunce": 0.5, "Mraky": 0.3},
    "Slunce": {"Dest": 0.2, "Slunce": 0.4, "Mraky": 0.4},
    "Mraky": {"Dest": 0.1, "Slunce": 0.4, "Mraky": 0.5}
}

# Počet iterací Monte Carlo
montecarlo = 1000

# Inicializace počítadel
destivo = 0
oblacno = 0
slunecno = 0

for _ in range(montecarlo):
    # Náhodně zvolené počasí první den
    dnes = random.choice(["Dest", "Slunce", "Mraky"])

    for _ in range(365):  # Simuluje počasí 1 rok
        # Odhaduje počasí následující den na základě předchozího, pravděpodobnost podle úvodních parametrů
        zitra = random.choices(["Dest", "Slunce", "Mraky"],
                                    weights=[pravdepodobnost[dnes]["Dest"],
                                             pravdepodobnost[dnes]["Slunce"],
                                             pravdepodobnost[dnes]["Mraky"]])[0]

        if zitra == "Dest":
            destivo += 1
        elif zitra == "Mraky":
            oblacno += 1
        elif zitra == "Slunce":
            slunecno += 1

        dnes = zitra

# spočte průměrný počet dnů s daným počasím
dny = montecarlo * 365  # celkový počet zkoumaných dnů
odhad_destivo = (destivo / dny) * 365
odhad_oblacno = (oblacno / dny) * 365
odhad_slunecno = (slunecno / dny) * 365

print("Předpokládaný počet deštivých dnů:", round(odhad_destivo))
print("Předpokládaný počet oblačných dnů:", round(odhad_oblacno))
print("Předpokládaný počet slunečných dnů:", round(odhad_slunecno))
