"""Shared waveform-assembly logic for the digital modulation schemes.

All three schemes (ASK, FSK, PSK) build their output the same way: one carrier
waveform per symbol value, concatenated once per input bit. Only the two
per-symbol waveforms differ between schemes, so that assembly lives here.
"""

import numpy as np


def validar_bits(bits):
    """Return the bit string, or raise ValueError if it is not binary.

    Rejects empty input and any character other than '0' or '1', so the caller
    gets a clear error instead of a silently malformed signal.
    """
    bits = bits.strip()
    if not bits:
        raise ValueError("La cadena binaria está vacía.")
    if any(b not in "01" for b in bits):
        raise ValueError("La cadena binaria solo puede contener '0' y '1'.")
    return bits


def ensamblar_señal(bits, onda_bit0, onda_bit1, Tb, N):
    """Assemble the baseband and modulated signals from per-symbol waveforms.

    Builds a list of array references and concatenates once at the end.
    Concatenating inside the loop would reallocate and copy the whole signal
    on every bit — O(n^2) in the number of bits — which becomes noticeable
    with long bit strings or a high sample count per bit.

    Returns (t, x, y): time vector, baseband bit sequence, modulated carrier.
    """
    Nb = len(bits)
    t = np.linspace(0, Tb * Nb, N * Nb)

    ceros = np.zeros(N)
    unos = np.ones(N)

    piezas_x = [unos if b == "1" else ceros for b in bits]
    piezas_y = [onda_bit1 if b == "1" else onda_bit0 for b in bits]

    x = np.concatenate(piezas_x)
    y = np.concatenate(piezas_y)

    return t, x, y
