from WhatsAppBot import WhatsAppBot
from Wikipedia import Wikipedia

class Controller:
    def __init__(self, contact_name):
        self.bot = WhatsAppBot()
        self.wikipedia = Wikipedia()
        self.contact_name = contact_name

    def controller_whatsapp_wikipedia(self):
        self.bot.open_whatsapp()
        self.bot.search_contact(self.contact_name)
        first_message = "Bot do Wikipedia ativado! Digite 'O que é ___?' para saber a resposta!"
        magic_key = "o que é"
        self.bot.send_message(first_message)
        while(True):
            self.last_message = self.bot.read_last_message()
            if self.last_message[:len(magic_key)] == magic_key and "?" in self.last_message:
                self.information = self.last_message.lower().split("o que é")[1]
                self.information = self.information.replace("?", "")
                print(self.information)

                if self.wikipedia.search_information(self.information) == 1:
                   self.bot.send_message(self.wikipedia.get_information())
                else:
                    self.bot.send_message(self.wikipedia.get_error_information())









