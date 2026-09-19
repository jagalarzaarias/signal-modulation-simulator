# pm_modulation.py

import numpy as np


def generar_señal_fase_modulada(duracion, tasa_muestreo, Ax, fx, Ac, fc, indice_modulacion):
    """Generate a phase-modulated carrier from raw signal parameters.

    Previously this took precomputed señal_base / señal_portadora arrays and
    did sin(2*pi*señal_portadora + indice_modulacion*señal_base). That's
    wrong: señal_portadora is already the amplitude-scaled carrier waveform
    (Ac*sin(2*pi*fc*t)), not the linear phase argument (fc*t), so the result
    was a sine of a sine rather than a real phase-modulated carrier.

    This mirrors how AM and FM already work: build t and the baseband signal
    internally from the raw parameters, then add the phase deviation
    directly to the carrier's phase argument.
    """
    t = np.linspace(0, duracion, int(tasa_muestreo * duracion), endpoint=False)
    señal_base = Ax * np.sin(2 * np.pi * fx * t)
    pm_signal = Ac * np.cos(2 * np.pi * fc * t + indice_modulacion * señal_base)
    return pm_signal
