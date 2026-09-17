"""FSK — Frequency-Shift Keying.

Amplitude stays constant; the carrier frequency switches between F0 and F1
depending on the transmitted bit.
"""

import numpy as np

from _common import ensamblar_señal, validar_bits


def generar_señal_modulada_FSK(bits, Ac, Tb, F0, F1, N):
    bits = validar_bits(bits)

    tb = np.linspace(0, Tb, N)
    portadora_bit0 = Ac * np.cos(2 * np.pi * F0 * tb)
    portadora_bit1 = Ac * np.cos(2 * np.pi * F1 * tb)

    return ensamblar_señal(bits, portadora_bit0, portadora_bit1, Tb, N)
