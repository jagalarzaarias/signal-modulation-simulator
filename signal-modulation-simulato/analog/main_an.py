import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from am_modulation import generar_señal_amplitud_modulada
from fm_modulation import generar_señal_frecuencia_modulada
from pm_modulation import generar_señal_fase_modulada


# Ax y fx son amplitud y frecuencia de la señal base, respectivamente
def generar_señal_base(Ax, fx, duracion, tasa_muestreo):
    tiempo = np.linspace(0, duracion, int(tasa_muestreo * duracion), endpoint=False)
    señal_base = Ax * np.sin(2 * np.pi * fx * tiempo)
    return tiempo, señal_base

# Ac y fc son amplitud y frecuencia de la señal portadora, respectivamente
def generar_señal_portadora(Ac, fc, duracion, tasa_muestreo):
    tiempo = np.linspace(0, duracion, int(tasa_muestreo * duracion), endpoint=False)
    señal_portadora = Ac * np.sin(2 * np.pi * fc * tiempo)
    return tiempo, señal_portadora

def graficar_señales(opcion_grafica, opcion_modulacion):
    Ax = float(amplitude_base_entry.get())
    fx = float(frequency_base_entry.get())
    Ac = float(amplitude_carrier_entry.get())
    fc = float(frequency_carrier_entry.get())
    duracion = float(duration_entry.get())
    tasa_muestreo = float(sampling_rate_entry.get())

    tiempo, señal_base = generar_señal_base(Ax, fx, duracion, tasa_muestreo)
    _, señal_portadora = generar_señal_portadora(Ac, fc, duracion, tasa_muestreo)
    
    # Obtener el valor del parámetro de modulación correspondiente
    if opcion_modulacion == 'FM':
        indice_modulacion = float(beta_entry.get())
    elif opcion_modulacion == 'PM':
        indice_modulacion = float(phase_deviation_entry.get())

    # Generar la señal modulada según el tipo de modulación
    if opcion_modulacion == 'AM':
        señal_modulada = generar_señal_amplitud_modulada(duracion, tasa_muestreo, Ax, fx, Ac, fc)
    elif opcion_modulacion == 'FM':
        _, señal_modulada = generar_señal_frecuencia_modulada(duracion, tasa_muestreo, fx, Ax, fc, Ac, indice_modulacion)
    elif opcion_modulacion == 'PM':
        señal_modulada = generar_señal_fase_modulada(señal_base, señal_portadora, float(phase_deviation_entry.get()))


    # Graficar la señal
    plt.figure(figsize=(10, 3))

    if opcion_grafica == 'Señal Base':
        plt.plot(tiempo, señal_base, label='Señal Base')
        plt.title('Señal Base')
    elif opcion_grafica == 'Portadora':
        plt.plot(tiempo, señal_portadora, label='Señal Portadora')
        plt.title('Señal Portadora')
    elif opcion_grafica == 'Modulada':
        plt.plot(tiempo, señal_modulada, label=f'Señal Modulada ({opcion_modulacion})')
        plt.title(f'Señal Modulada ({opcion_modulacion})')

    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.xlim(0, tiempo[-1])
    plt.legend()
    plt.grid(True)
    # Call plt.show() to display the plot
    plt.show()  

# Crear la ventana principal
root = tk.Tk()
root.title("Modulación analógica")
root.geometry("500x500")

# Crear widgets
plot_label = ttk.Label(root, text="Selecciona la señal a graficar:")
plot_label.pack()

plot_choice = ttk.Combobox(root, values=["Señal Base", "Portadora", "Modulada"])
plot_choice.pack()

modulation_label = ttk.Label(root, text="Selecciona el tipo de modulación:")
modulation_label.pack()

modulation_choice = ttk.Combobox(root, values=["AM", "FM", "PM"])
modulation_choice.pack()

generate_button = ttk.Button(root, text="Generar Gráfica", command=lambda: graficar_señales(plot_choice.get(), modulation_choice.get()))
generate_button.pack()

# Parámetros de las señales
params_frame = ttk.LabelFrame(root, text="Parámetros de las Señales")
params_frame.pack(pady=10)

amplitude_base_label = ttk.Label(params_frame, text="Amplitud Base:")
amplitude_base_label.grid(row=0,column=0, padx=5, pady=5)
amplitude_base_entry = ttk.Entry(params_frame)
amplitude_base_entry.grid(row=0, column=1, padx=5, pady=5)

frequency_base_label = ttk.Label(params_frame, text="Frecuencia Base (Hz):")
frequency_base_label.grid(row=1, column=0, padx=5, pady=5)
frequency_base_entry = ttk.Entry(params_frame)
frequency_base_entry.grid(row=1, column=1, padx=5, pady=5)

amplitude_carrier_label = ttk.Label(params_frame, text="Amplitud Portadora:")
amplitude_carrier_label.grid(row=2, column=0, padx=5, pady=5)
amplitude_carrier_entry = ttk.Entry(params_frame)
amplitude_carrier_entry.grid(row=2, column=1, padx=5, pady=5)

frequency_carrier_label = ttk.Label(params_frame, text="Frecuencia Portadora (Hz):")
frequency_carrier_label.grid(row=3, column=0, padx=5, pady=5)
frequency_carrier_entry = ttk.Entry(params_frame)
frequency_carrier_entry.grid(row=3, column=1, padx=5, pady=5)


beta_label = ttk.Label(params_frame, text="Parámetro de Modulación Beta:")
beta_label.grid(row=5, column=0, padx=5, pady=5)
beta_entry = ttk.Entry(params_frame)
beta_entry.grid(row=5, column=1, padx=5, pady=5)
beta_label.grid_remove()
beta_entry.grid_remove()

phase_deviation_label = ttk.Label(params_frame, text="Desviación de Fase (rad):")
phase_deviation_label.grid(row=6, column=0, padx=5, pady=5)
phase_deviation_entry = ttk.Entry(params_frame)
phase_deviation_entry.grid(row=6, column=1, padx=5, pady=5)
phase_deviation_entry.insert(0, "0.0")
phase_deviation_label.grid_remove()
phase_deviation_entry.grid_remove()

duration_label = ttk.Label(params_frame, text="Duración (s):")
duration_label.grid(row=7, column=0, padx=5, pady=5)
duration_entry = ttk.Entry(params_frame)
duration_entry.grid(row=7, column=1, padx=5, pady=5)

sampling_rate_label = ttk.Label(params_frame, text="Tasa de Muestreo (Hz):")
sampling_rate_label.grid(row=8, column=0, padx=5, pady=5)
sampling_rate_entry = ttk.Entry(params_frame)
sampling_rate_entry.grid(row=8, column=1, padx=5, pady=5)


# Función para mostrar u ocultar los parámetros según el tipo de modulación seleccionado
def mostrar_ocultar_parametros(event=None):
    modulacion = modulation_choice.get()
    if modulacion == "FM":
        beta_label.grid()
        beta_entry.grid()
        phase_deviation_label.grid_remove()
        phase_deviation_entry.grid_remove()
    elif modulacion == "PM":
        beta_label.grid_remove()
        beta_entry.grid_remove()
        phase_deviation_label.grid()
        phase_deviation_entry.grid()
    elif modulacion == "AM":
        beta_label.grid_remove()
        beta_entry.grid_remove()
        phase_deviation_label.grid_remove()
        phase_deviation_entry.grid_remove()


# Vincular la función mostrar_ocultar_parametros al evento de cambio de selección del tipo de modulación
modulation_choice.bind("<<ComboboxSelected>>", mostrar_ocultar_parametros)

root.mainloop()

