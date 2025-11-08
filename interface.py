import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from process import imageProcess
import cv2
import numpy as np


def upload_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Imagens", "*.png *.jpg *.jpeg *.bmp *.gif")]
    )
    if file_path:
        img = Image.open(file_path)
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk  
        start_process(img) 

def start_process(uploaded_img):
    if uploaded_img is not None:
       
        img_cv = cv2.cvtColor(np.array(uploaded_img), cv2.COLOR_RGB2BGR)
        
        #img_resized = imageProcess.ResizeImage(img_cv)
        
        img_resized_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)

        imageProcess.EncontraMatriz(img_resized_rgb)

        pil_resized = Image.fromarray(img_resized_rgb)
        
        img_tk_resized = ImageTk.PhotoImage(pil_resized)

        image_label.config(image=img_tk_resized)
         
        image_label.image = img_tk_resized
    else:
        print("Nenhuma imagem carregada!")



# Criação da janela principal
root = tk.Tk()
root.title("Upload de Imagem")
root.geometry("400x400")

# Botão de upload
upload_button = tk.Button(root, text="Selecionar Imagem", command=upload_image)
upload_button.pack(pady=10)

# Label para exibir a imagem
image_label = tk.Label(root)
image_label.pack()

# Inicia o loop da interface
root.mainloop()

