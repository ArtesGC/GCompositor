from mutagen import Tags, File


class GCT:
    def __init__(self, _nome_fich: str):
        self.ficheiro = File(_nome_fich, easy=True)
