import numpy as np

def generar_señal_frecuencia_modulada(duracion, tasa_muestreo, fx, Ax, fc, Ac, beta):
    # Crear el vector de tiempo
    t = np.linspace(0, duracion, int(tasa_muestreo * duracion))

    xint = Ax * np.sin(2 * np.pi * fx * t)

    # Generar la señal FM
    fm_signal = Ac * np.cos(2 * np.pi * fc * t + beta * xint)

    return t, fm_signal
