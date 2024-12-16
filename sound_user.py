import speech_recognition as sr
import keyboard


enabled = True

def transcribir_audio():
    r = sr.Recognizer()
    print("Presiona 'S' para empezar a grabar. Mantén presionada la tecla 'S' para grabar.")

    while True:
        if keyboard.is_pressed('s'):
            print("Grabando... (mantén 'S' presionada para continuar)")
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)

            print("Grabación finalizada. Procesando...")

            try:
                texto = r.recognize_google(audio, language="es-ES")
                print("Has dicho: " + texto)
            except sr.UnknownValueError:
                print("No se pudo entender el audio")
            except sr.RequestError as e:
                print(f"No se pudo solicitar resultados; {e}")

        if keyboard.is_pressed('esc'):
            print("Saliendo...")
            break

if __name__ == "__main__":
    transcribir_audio()
