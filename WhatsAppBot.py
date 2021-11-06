from selenium import webdriver
from time import sleep
import os


class WhatsAppBot:
    def __init__(self):
        self.path = os.getcwd()
        self.chromedriver = self.path + "\chromedriver.exe"
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument(r"user-data-dir=" + self.path + "\profile\wpp")
        self.driver = webdriver.Chrome(self.chromedriver, chrome_options=self.chrome_options)
        self.waits = self.driver.implicitly_wait(30)

    def open_whatsapp(self):
        try:
            self.driver.get("https://web.whatsapp.com/")
            self.waits
            print("[+]: Abrindo Whatsapp;")
            return 1
        except:
            print("[Error]: Não foi possível abrir o Whatsapp.")
            return 0

    def search_contact(self, contact):
        try:
            search_box = self.driver.find_element_by_class_name("_13NKt")
            search_box.send_keys(contact)
            self.waits
            contact_chat = self.driver.find_element_by_css_selector("[title ^= {}]".format(contact))
            contact_chat.click()
            print("[+]: Contato Encontrado;")
            sleep(3)
            return 1
        except:
            print("[Error]: Contato não encontrado.")
            return 0


    def send_message(self, message):
        try:
            message_box = self.driver.find_elements_by_class_name("_13NKt")
            message_box[1].send_keys(message)
            self.driver.implicitly_wait(15)
            send_button = self.driver.find_element_by_xpath("//span[@data-testid='send']")
            send_button.click()
            print("[+]: Mensagem enviada com sucesso;")
            sleep(3)
            return 1
        except:
            print("[Error]: Não foi possível enviar a mensagem.")
            return 0

    def read_last_message(self):
        messages = self.driver.find_elements_by_class_name("_1Gy50")
        index = len(messages) - 1
        text = messages[index].text
        return text

    def close_window(self):
        self.driver.close()
        print("[+]: Encerrando a aplicacão.")
