import wikipedia


class Wikipedia:
    def __init__(self):
        wikipedia.set_lang("pt")

    def search_information(self, information):
        try:
            self.information = wikipedia.summary(information, sentences=2)
            return 1
        except:
            print("[-] Informação não encontrada.")
            self.error = "Desculpe, informação não encontrada."
            return 0

    def get_information(self):
        return self.information

    def get_error_information(self):
        return self.error


