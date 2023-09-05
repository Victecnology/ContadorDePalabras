import tkinter as tk

# Definimos la función para contar el número de palabras
def count_words():
  # Obtenemos el texto del usuario
  text = text_entry.get()

  # Contamos las palabras
  words = text.split()
  count = len(words)

  # Mostramos el número de palabras
  count_label.config(text=f"El número de palabras es {count}")

# Creamos la ventana principal
root = tk.Tk()
root.title("Contador de palabras")

# Creamos el cuadro de entrada
text_entry = tk.Entry(root)
text_entry.grid(row=0, column=0)

# Creamos el botón para contar las palabras
count_button = tk.Button(root, text="Contar", command=count_words)
count_button.grid(row=1, column=0)

# Creamos el cuadro de texto para mostrar el número de palabras
count_label = tk.Label(root, text="")
count_label.grid(row=2, column=0)

# Ejecutamos el bucle principal
root.mainloop()