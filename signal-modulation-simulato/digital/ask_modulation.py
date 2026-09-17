"""ASK — Amplitude-Shift Keying.

The carrier frequency and phase stay constant; amplitude switches between A0
and A1 depending on the transmitted bit.
"""

import numpy as np

from _common import ensamblar_señal, validar_bits


def generar_señal_modulada_ASK(bits, fc, Tb, A0, A1, N):
    bits = validar_bits(bits)

    tb = np.linspace(0, Tb, N)
    portadora_bit0 = A0 * np.cos(2 * np.pi * fc * tb)
    portadora_bit1 = A1 * np.cos(2 * np.pi * fc * tb)

    return ensamblar_señal(bits, portadora_bit0, portadora_bit1, Tb, N)
