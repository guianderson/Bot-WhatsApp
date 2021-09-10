from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])


class helper:
    @staticmethod
    def bootstrap():
        data = {
            1: "Envio de Mensagem",
            2: "ChatBot",
            3: "Sair"
        }
        print("Escolha uma opção: ")
        for options in sorted(data):
            print("{} - {}".format(options, data[options]))
        value = input("Opção: ")
        if not value.isdigit() or not int(value) in data:
            helper.invalid_value(value)
        elif value == "1":
            obj = whatsBot('https://web.whatsapp.com/')
            obj.openWhats()
        elif value == "2":
            print("Em desenvolvimento...")
        elif value == "3":
            print("Finalizando chatbot...")

    @staticmethod
    def invalid_value(value):
        print("À opção " + value + " é inválida, selecione outra opção\n")
        helper.bootstrap()


class whatsBot:
    def __init__(self, site_name):
        self.site_name = site_name

    def openWhats(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get(self.site_name)
        self.sendMessage(driver)

    @staticmethod
    def sendMessage(driver):
        chatName = input('Entre com o nome: ')
        chatMsg = input('Entre com a mensagem: ')
        noCount = int(input('Quantas vezes? '))

        input('Enter Anything after Scanning or Code')
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(chatName))

        user.click()
        msg_box = driver.find_element_by_xpath("//div[@class='_1UWac _1LbR4 focused']//div[@role='textbox']")
        for i in range(noCount):
            msg_box.send_keys(chatMsg)
            button = driver.find_element_by_class_name('_1Ae7k')
            button.click()
