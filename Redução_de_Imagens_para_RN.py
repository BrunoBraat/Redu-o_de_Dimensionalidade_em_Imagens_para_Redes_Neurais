import cv2

# Carregar a imagem colorida (exemplo: lena.png)
imagem_colorida = cv2.imread("lena.png")

# Converter para níveis de cinza (0 a 255)
imagem_cinza = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)

# Aplicar binarização (thresholding)
# Pixels acima de 127 viram 255 (branco), abaixo viram 0 (preto)
_, imagem_binaria = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)

# Exibir as imagens
cv2.imshow("Imagem Colorida", imagem_colorida)
cv2.imshow("Imagem em Tons de Cinza", imagem_cinza)
cv2.imshow("Imagem Binarizada", imagem_binaria)

cv2.waitKey(0)
cv2.destroyAllWindows()