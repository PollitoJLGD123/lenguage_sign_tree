from django.http import StreamingHttpResponse
from django.shortcuts import render
from .modelo.testing import todito
import joblib
import cv2

# Función generadora para capturar video desde la cámara
def gen_camera():
    # cap = cv2.VideoCapture(0)  # Captura desde la cámara (0 es la cámara predeterminada)
    # while True:
    #     ret, frame = cap.read()
    #     if not ret:
    #         break
    #     #aplicar filtro gris
    #     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #     # Codifica el frame en formato JPEG
    #     _, buffer = cv2.imencode('.jpg', frame)
    #     frame = buffer.tobytes()

    #     # Devuelve el frame como un stream
    #     yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    # cap.release()
    # cv2.imread('modelo/roc.png')
    yield from todito()


# Vista que muestra el video desde la cámara
def camera_feed(request):
    return StreamingHttpResponse(gen_camera(), content_type='multipart/x-mixed-replace; boundary=frame')

# Vista principal para la página de video
def video_page(request):
    return render(request, 'video_page.html')
def index(request):
    return render(request, 'home.html')