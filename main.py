import customtkinter as ctk

# Configuración inicial
ctk.set_appearance_mode("Dark")  # Modo oscuro
ctk.set_default_color_theme("blue")  # Tema azul


# Función para calcular
def calcular():
    try:
        gramos = float(entry_gramos.get().replace(",", "."))
        precio_kg = float(entry_precio.get().replace(",", "."))
        horas = float(entry_horas.get().replace(",", "."))
        coste_luz = float(entry_luz.get().replace(",", "."))

        precio_gramo = precio_kg / 1000
        precio_filamento = gramos * precio_gramo
        precio_luz_total = horas * coste_luz
        precio_total_impresion = precio_filamento + precio_luz_total
        precio_final_beneficio = precio_total_impresion * 1.5

        resultado_var.set(
            f"Filamento: {precio_filamento:.2f} €\n"
            f"Luz: {precio_luz_total:.2f} €\n"
            f"Total impresión: {precio_total_impresion:.2f} €\n"
            f"Precio final (+50%): {precio_final_beneficio:.2f} €"
        )
    except ValueError:
        resultado_var.set("❌ Por favor, ingresa valores válidos.")


# Ventana principal
root = ctk.CTk()
root.title("Calculadora 3D")
root.geometry("400x500")
root.resizable(False, False)

# Labels y entradas
ctk.CTkLabel(root, text="Calculadora 3D", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=20)

entry_gramos = ctk.CTkEntry(root, placeholder_text="Gramos usados" , width=200, justify="center")
entry_gramos.pack(pady=10, padx=40)

entry_precio = ctk.CTkEntry(root, placeholder_text="Precio del filamento (€/kg)", width=200, justify="center")
entry_precio.pack(pady=10, padx=40)

entry_horas = ctk.CTkEntry(root, placeholder_text="Horas de impresión", width=200, justify="center")
entry_horas.pack(pady=10, padx=40)

entry_luz = ctk.CTkEntry(root, placeholder_text="Precio de la luz (€/kWh)", width=200, justify="center")
entry_luz.pack(pady=10, padx=40)

# Botón calcular
ctk.CTkButton(root, text="Calcular", command=calcular).pack(pady=20)

# Resultado
resultado_var = ctk.StringVar()
resultado_label = ctk.CTkLabel(root, textvariable=resultado_var, font=ctk.CTkFont(size=18), justify="center")
resultado_label.pack(pady=20)

# Iniciar aplicación
root.mainloop()
