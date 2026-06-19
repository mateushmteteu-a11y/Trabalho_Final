import tkinter as tk
from PIL import Image, ImageTk

janela = tk.Tk()
janela.title("Minha Janela com Imagem")
janela.geometry("400x400")


caminho = r"C:\Users\pedro61685786\Pictures\Screenshots\1000013567_82c8130114e74e0a66a51f36d74fc2bc-17_06_2026, 13_33_00.jpg"
imagem_pil = Image.open(caminho)


imagem_pil = imagem_pil.resize((300, 300)) 


imagem_tkinter = ImageTk.PhotoImage(imagem_pil)


label_imagem = tk.Label(janela, image=imagem_tkinter)
label_imagem.pack(pady=20)


janela.mainloop()