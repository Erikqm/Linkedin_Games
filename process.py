import cv2
import numpy as np

class imageProcess:

    @staticmethod
    def ResizeImage(img):
        # Usa INTER_LINEAR como interpolação padrão
        resized = cv2.resize(img, (200, 20), interpolation=cv2.INTER_LINEAR)
        return resized

    @staticmethod
    def EncontraMatriz (img):

        # Carregar imagem
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Aplicar suavização e detecção de bordas
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blur, 50, 150)

        # Encontrar contornos
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            # Aproxima o contorno para reduzir número de pontos
            approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)

            # Se tiver 4 vértices, pode ser um retângulo/quadrado
            if len(approx) == 4:
                # Desenha o contorno encontrado
                cv2.drawContours(img, [approx], 0, (0, 255, 0), 3)

                # Opcional: verificar se é retângulo (ângulos ~90°)
                # ou se é apenas um quadrilátero qualquer
                # Aqui podemos calcular bounding box:
                x, y, w, h = cv2.boundingRect(approx)
                aspect_ratio = float(w) / h
                print(f"Retângulo encontrado em ({x},{y}), largura={w}, altura={h}, razão={aspect_ratio:.2f}")

        # Mostrar resultado
        cv2.imshow("Retângulos detectados", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
