import librosa
import numpy as np
import tensorflow as tf
from tkinter import Tk, Button, Label, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

Input = tf.keras.layers.Input
Conv2D = tf.keras.layers.Conv2D
MaxPooling2D = tf.keras.layers.MaxPooling2D
Flatten = tf.keras.layers.Flatten
Dense = tf.keras.layers.Dense
Model = tf.keras.models.Model
Adam = tf.keras.optimizers.Adam
to_categorical = tf.keras.utils.to_categorical
resize = tf.image.resize
load_model = tf.keras.models.load_model


# Função para carregar e preprocessar o arquivo de áudio
def test_audio(file_path, model):
    audio_data, sample_rate = librosa.load(file_path, sr=None)
    mel_spectrogram = librosa.feature.melspectrogram(y=audio_data, sr=sample_rate)
    mel_spectrogram = resize(np.expand_dims(mel_spectrogram, axis=-1), target_shape)
    mel_spectrogram = tf.reshape(mel_spectrogram, (1,) + target_shape + (1,))
    predictions = model.predict(mel_spectrogram)
    class_probabilities = predictions[0]
    predicted_class_index = np.argmax(class_probabilities)
    return mel_spectrogram, class_probabilities, predicted_class_index


# Função para selecionar o arquivo e exibir os resultados
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])
    if file_path:
        mel_spectrogram, class_probabilities, predicted_class_index = test_audio(file_path, model)
        predicted_class = classes[predicted_class_index]
        result_label.config(text=f"Número: {predicted_class}")
        show_spectrogram(mel_spectrogram)


# Função para exibir o espectrograma
def show_spectrogram(mel_spectrogram):
    global canvas
    if canvas:
        canvas.get_tk_widget().pack_forget()  # Remove o espectrograma anterior

    fig, ax = plt.subplots()
    ax.imshow(mel_spectrogram.numpy().squeeze(), aspect="auto", origin="lower")
    ax.set_title("Espectrograma Mel")
    ax.set_xlabel("Tempo")
    ax.set_ylabel("Frequência")

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=20)


# Carregar o modelo salvo
model = tf.keras.models.load_model("audio_classification_model.keras")

# Definir as classes e a forma alvo
classes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
target_shape = (128, 128)

# Criar a interface gráfica
root = Tk()
root.title("Numeric Digit Recognizer")

canvas = None  # Inicializa a variável canvas

select_button = Button(root, text="Selecionar arquivo .wav", command=select_file)
select_button.pack(pady=20)

result_label = Label(root, text="")
result_label.pack(pady=20)

root.mainloop()
