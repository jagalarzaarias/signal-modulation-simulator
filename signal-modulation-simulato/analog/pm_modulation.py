# pm_modulation.py

import numpy as np

def generar_señal_fase_modulada(señal_base, señal_portadora, indice_modulacion):
    pm_signal = np.sin(2 * np.pi * señal_portadora + indice_modulacion * señal_base)
    return pm_signal
