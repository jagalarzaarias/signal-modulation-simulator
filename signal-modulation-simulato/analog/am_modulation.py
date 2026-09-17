import numpy as np


def generar_señal_amplitud_modulada(duracion, tasa_muestreo, Ax, fx, Ac, fc):
    t = np.linspace(0, duracion, int(tasa_muestreo * duracion))
    x = Ax * np.cos(2 * np.pi * fx * t)
    c = Ac * np.cos(2 * np.pi * fc * t)
    m = Ax / Ac
    am_signal = (1 + m * x / Ax) * c
    return am_signal
