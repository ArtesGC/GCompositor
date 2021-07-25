import pyaudio
import wave


def reprodutor():
    print("""
    [*] REPRODUZINDO UM ARQUIVO DE AUDIO (.wav) [*]
-------------------------------------------------------""")

    CHUNK = 1024
    AUDIO = "../sound/Idrada.wav"

    # definindo a localização do audio para a sua leitura
    wf = wave.open(AUDIO, 'rb')

    # iniciando a instância do PyAudio
    p = pyaudio.PyAudio()

    # criando o stream do audio
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)

    # definindo o fim do streamming e da instancia
    # no final da reprodução
    stream.stop_stream()
    stream.close()
    p.terminate()


if __name__ == '__main__':
    reprodutor()