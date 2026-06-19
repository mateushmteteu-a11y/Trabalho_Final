import tkinter as tk
from PIL import Image, ImageTk

janela = tk.Tk()
janela.title("Minha Janela com Imagem")
janela.geometry("400x400")


caminho = r"C:\Users\pedro61685786\Downloads\Captura de tela 2026-05-07 113602 2.png"
imagem_pil = Image.open(caminho)


imagem_pil = imagem_pil.resize((300, 300)) 


imagem_tkinter = ImageTk.PhotoImage(imagem_pil)


label_imagem = tk.Label(janela, image=imagem_tkinter)
label_imagem.pack(pady=20)


janela.mainloop()