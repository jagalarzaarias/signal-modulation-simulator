import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox
from ask_modulation import generar_señal_modulada_ASK
from fsk_modulation import generar_señal_modulada_FSK
from psk_modulation import generar_señal_modulada_PSK

# Graficar señales moduladas ASK
def graficar_modulacion_ASK(bits, fc, Tb, A0, A1, N):
    t, x, y = generar_señal_modulada_ASK(bits, fc, Tb, A0, A1, N)
    plt.figure(1)
    plt.plot(t, x)
    plt.axis([0, Tb * len(bits), -0.5, 1.5])
    plt.title('Señal Moduladora (Bits)')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.figure(2)
    plt.plot(t, y)
    plt.title('Señal Modulada ASK')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.show()

# Graficar señales moduladas FSK
def graficar_modulacion_FSK(bits, Ac, Tb, F0, F1, N):
    t, x, y = generar_señal_modulada_FSK(bits, Ac, Tb, F0, F1, N)
    plt.figure(1)
    plt.plot(t, x)
    plt.axis([0, Tb * len(bits), -0.5, 1.5])
    plt.title('Señal Moduladora (Bits)')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.figure(2)
    plt.plot(t, y)
    plt.title('Señal Modulada FSK')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.show()

# Graficar señales moduladas PSK
def graficar_modulacion_PSK(bits, Ac, Tb, fc, N):
    t, x, y = generar_señal_modulada_PSK(bits, Ac, Tb, fc, N)
    plt.figure(1)
    plt.plot(t, x)
    plt.axis([0, Tb * len(bits), -0.5, 1.5])
    plt.title('Señal Moduladora (Bits)')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.figure(2)
    plt.plot(t, y)
    plt.title('Señal Modulada PSK')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.show()

# Función para graficar la señal seleccionada
def graficar_señal():
    tipo_modulacion = modulation_choice.get()
    if not tipo_modulacion:
        messagebox.showwarning("Falta seleccionar", "Selecciona un tipo de modulación.")
        return

    bits = binary_entry.get()

    try:
        _graficar(tipo_modulacion, bits)
    except ValueError as e:
        # Cubre tanto los bits inválidos (validar_bits) como los campos
        # numéricos vacíos o con texto (float()/int() lanzan ValueError).
        messagebox.showerror("Parámetros inválidos", str(e))


def _graficar(tipo_modulacion, bits):
    if tipo_modulacion == 'ASK':
        fc = float(frequency_carrier_entry.get())
        Tb = float(bit_duration_entry.get())
        A0 = float(amplitude_bit0_entry.get())
        A1 = float(amplitude_bit1_entry.get())
        N = int(points_wave_entry.get())
        graficar_modulacion_ASK(bits, fc, Tb, A0, A1, N)
    elif tipo_modulacion == 'FSK':
        Ac = float(amplitude_carrier_entry.get())
        Tb = float(bit_duration_entry.get())
        F0 = float(frequency_bit0_entry.get())
        F1 = float(frequency_bit1_entry.get())
        N = int(points_wave_entry.get())
        graficar_modulacion_FSK(bits, Ac, Tb, F0, F1, N)
    elif tipo_modulacion == 'PSK':
        Ac = float(amplitude_carrier_entry.get())
        Tb = float(bit_duration_entry.get())
        fc = float(frequency_carrier_entry.get())
        N = int(points_wave_entry.get())
        graficar_modulacion_PSK(bits, Ac, Tb, fc, N)

# Función para mostrar y ocultar campos según el tipo de modulación
def actualizar_campos(event):
    tipo_modulacion = modulation_choice.get()
    if tipo_modulacion == 'ASK':
        frequency_carrier_label.pack()
        frequency_carrier_entry.pack()
        amplitude_bit0_label.pack()
        amplitude_bit0_entry.pack()
        amplitude_bit1_label.pack()
        amplitude_bit1_entry.pack()

        amplitude_carrier_label.pack_forget()
        amplitude_carrier_entry.pack_forget()
        frequency_bit0_label.pack_forget()
        frequency_bit0_entry.pack_forget()
        frequency_bit1_label.pack_forget()
        frequency_bit1_entry.pack_forget()
    elif tipo_modulacion == 'FSK':
        amplitude_carrier_label.pack()
        amplitude_carrier_entry.pack()
        frequency_bit0_label.pack()
        frequency_bit0_entry.pack()
        frequency_bit1_label.pack()
        frequency_bit1_entry.pack()

        frequency_carrier_label.pack_forget()
        frequency_carrier_entry.pack_forget()
        amplitude_bit0_label.pack_forget()
        amplitude_bit0_entry.pack_forget()
        amplitude_bit1_label.pack_forget()
        amplitude_bit1_entry.pack_forget()
    elif tipo_modulacion == 'PSK':
        amplitude_carrier_label.pack()
        amplitude_carrier_entry.pack()
        frequency_carrier_label.pack()
        frequency_carrier_entry.pack()

        amplitude_bit0_label.pack_forget()
        amplitude_bit0_entry.pack_forget()
        amplitude_bit1_label.pack_forget()
        amplitude_bit1_entry.pack_forget()
        frequency_bit0_label.pack_forget()
        frequency_bit0_entry.pack_forget()
        frequency_bit1_label.pack_forget()
        frequency_bit1_entry.pack_forget()

# Crear la ventana principal
root = tk.Tk()
root.title("Modulación digital")
root.geometry("400x500")

# Crear widgets
plot_label = ttk.Label(root, text="Selecciona el tipo de modulación:")
plot_label.pack()

modulation_choice = ttk.Combobox(root, values=["ASK", "FSK", "PSK"])
modulation_choice.bind("<<ComboboxSelected>>", actualizar_campos)
modulation_choice.pack()

generate_button = ttk.Button(root, text="Generar Gráfica", command=graficar_señal)
generate_button.pack()

binary_label = ttk.Label(root, text="Datos Binarios:")
binary_label.pack()
binary_entry = ttk.Entry(root)
binary_entry.pack()

# Parámetros para ASK y PSK
frequency_carrier_label = ttk.Label(root, text="Frecuencia de la portadora (fc):")
frequency_carrier_entry = ttk.Entry(root)

amplitude_bit0_label = ttk.Label(root, text="Amplitud para bit 0 (A0):")
amplitude_bit0_entry = ttk.Entry(root)

amplitude_bit1_label = ttk.Label(root, text="Amplitud para bit 1 (A1):")
amplitude_bit1_entry = ttk.Entry(root)

# Parámetros para FSK y PSK
amplitude_carrier_label = ttk.Label(root, text="Amplitud de la portadora (Ac):")
amplitude_carrier_entry = ttk.Entry(root)

frequency_bit0_label = ttk.Label(root, text="Frecuencia para bit 0 (F0):")
frequency_bit0_entry = ttk.Entry(root)

frequency_bit1_label = ttk.Label(root, text="Frecuencia para bit 1 (F1):")
frequency_bit1_entry = ttk.Entry(root)

# Parámetros comunes
bit_duration_label = ttk.Label(root, text="Duración de un bit (Tb):")
bit_duration_label.pack()
bit_duration_entry = ttk.Entry(root)
bit_duration_entry.pack()

points_wave_label = ttk.Label(root, text="Número de puntos en una onda (N):")
points_wave_label.pack()
points_wave_entry = ttk.Entry(root)
points_wave_entry.pack()

root.mainloop()
