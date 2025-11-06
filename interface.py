import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def upload_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Imagens", "*.png *.jpg *.jpeg *.bmp *.gif")]
    )
    if file_path:
        img = Image.open(file_path)
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk  

# Criação da janela principal
root = tk.Tk()
root.title("Upload de Imagem")
root.geometry("400x400")

# Botão de upload
upload_button = tk.Button(root, text="Selecionar Imagem", command=upload_image)
upload_button.pack(pady=10)

# Botão de iniciar processamento
process_button = tk.Button(root, text="Resolver puzzle")
process_button.pack(pady=10)

# Label para exibir a imagem
image_label = tk.Label(root)
image_label.pack()

# Inicia o loop da interface
root.mainloop()
