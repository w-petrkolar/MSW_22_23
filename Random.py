import pyautogui, time, datetime, keyboard, psutil


def poloha_mys():
    x, y = pyautogui.position()
    #  print(f"Pozice kurzoru: x={x}, y={y}")
    rnd_no = x+y
    return rnd_no


def cas_nahoda():
    datum = datetime.datetime.now()
    hh = datum.hour
    mm = datum.minute
    ss = datum.second
    d = datum.day
    m = datum.month
    y = datum.year
    datum_nahoda = hh + mm + ss + d + m + y
    return datum_nahoda


def volna_ram():
    ram = psutil.virtual_memory()
    free_ram = ram.available
    free_ram_mb = free_ram / (1024 ** 2)  # převod na MB
    return free_ram_mb


def mezernik():
    print("Stiskni dvakrát mezerník.")

    prvni_cas = None
    druhy_cas = None

    while True:
        event = keyboard.read_event()

        if event.event_type == keyboard.KEY_DOWN and event.name == "space":
            if prvni_cas is None:
                prvni_cas = time.time()
            else:
                druhy_cas = time.time()
                break

    if prvni_cas is not None and druhy_cas is not None:
        cas_mezernik = druhy_cas - prvni_cas    # ma 16 des. mist
        print(f'Input čas stisku: {cas_mezernik}')
        return cas_mezernik
    else:
        return None


def generator(a, b, c, d):
    # na základě polohy kurzoru, volné ram, aktuálního data a uživatelského vstupu
    # generuje náhodné číslo v zadaném rozmezí
    dolni = -100
    horni = 100

    if horni == dolni:
        print(f'Tvoje "náhodné" číslo je: {dolni}')

    elif dolni > horni:
        print(f'To asi nepůjde, špatné meze: ')

    else:
        rozsah = horni - dolni
        seed = (((a + b + c) * d) % 1) * rozsah
        print(f'Seed: {seed}')
        xx = seed

        if dolni <= xx < horni:
            nahodne_cislo = round(xx)
            print(f'Náhodné číslo: {nahodne_cislo}')

        else:
            nahodne_cislo = xx
            while not dolni <= nahodne_cislo <= horni:
                if nahodne_cislo > horni:
                    while nahodne_cislo > horni:
                        nahodne_cislo = nahodne_cislo * (-0.5)
                        # je-li nad intervalem, budeme ho postupně půlit

                else:
                    while nahodne_cislo < dolni:
                        nahodne_cislo = nahodne_cislo * (-3)
                        # je-li po intervalem, budeme ho postupně násobit, bude nakonec nad intervalem a kladné

            nahodne_cislo = round(nahodne_cislo)
            print(f'Náhodné číslo: {nahodne_cislo}')


generator(poloha_mys(), cas_nahoda(), volna_ram(), mezernik())

"""print(f'mezernik {mezernik()}')
print(f'myš {poloha_mys()}')
print(f'date {cas_nahoda()}')
print(f'ram {volna_ram()}')"""
