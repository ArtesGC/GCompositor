import pyaudio
import wave


class GCR:
    def reprodutorMp3(self):
        pass

    def reprodutorWav(self, _audio: str):
        CHUNK = 1024

        # definindo a localização do audio para a sua leitura
        audio_file = wave.open(_audio, 'rb')

        # iniciando a instância do PyAudio
        player = pyaudio.PyAudio()

        # criando o stream do audio
        stream = player.open(format=player.get_format_from_width(audio_file.getsampwidth()),
                             channels=audio_file.getnchannels(),
                             rate=audio_file.getframerate(),
                             output=True)

        data = audio_file.readframes(CHUNK)

        while data != '':
            stream.write(data)
            data = audio_file.readframes(CHUNK)

        # definindo o fim do streamming e da instancia
        # no final da reprodução
        stream.stop_stream()
        stream.close()
        player.terminate()
