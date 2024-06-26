# ---------------------------------------------------------------------------- Explication --------------------------------------------------------------------------

# ----------------------------------------------------------------------------- Constantes --------------------------------------------------------------------------

from time import sleep

dt = 0.01 # en secondes : pas temporel
DT = 6 # demi-base du pic
T1 = 13.7
T0 = T1 - DT
T2 = T1 + DT + 0.93
T3 = T2 + 0.93

TF = 30 #s temps final
clock = 0


# ------------------------------------------------------------------------------ Pilotage ---------------------------------------------------------------------------

while clock < TF:
    if clock < T0:
        print(0)
    elif clock < T1:
        print(1)
        # Remplir le ballast
    elif clock < T2:
        print(-1)
        # Vider le ballast
    else:
        print(0)
    clock += dt
    sleep(dt)
