"""PSK — Phase-Shift Keying (binary).

Amplitude and frequency stay constant; the carrier phase shifts by pi radians
for a '1', which is what makes BPSK more noise-resistant than ASK at the same
transmitted power.
"""

import numpy as np

from _common import ensamblar_señal, validar_bits


def generar_señal_modulada_PSK(bits, Ac, Tb, fc, N):
    bits = validar_bits(bits)

    tb = np.linspace(0, Tb, N)
    portadora_bit0 = Ac * np.cos(2 * np.pi * fc * tb)
    portadora_bit1 = Ac * np.cos(2 * np.pi * fc * tb + np.pi)

    return ensamblar_señal(bits, portadora_bit0, portadora_bit1, Tb, N)
