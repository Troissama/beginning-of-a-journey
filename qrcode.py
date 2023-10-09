import qrcode
imagem = qrcode.make("https://www.youtube.com/watch?v=O9A-bD0en8I")
imagem.save("meuqrcode.jpg")