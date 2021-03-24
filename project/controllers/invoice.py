import re
import datetime
class InvoiceController():
    def __init__(self):
        self.invoiceNumber = None
        self.value = None
        self.verificationCode = None
        self.ship_field_pos = 0
        self.total_field_pos = 0

    def get_invoice_data(self, items):
        for index, item in enumerate(items):
            if self.invoiceNumber and self.verificationCode and self.value:
                break
            self.check_invoice_number(item)
            self.check_value(item, items, index)
            self.check_verification_code(item, items, index)
        return {
                "invoiceNumber": self.invoiceNumber,
                "value": self.value,
                "verificationCode": self.verificationCode
            }


    def check_invoice_number(self, item):
        #checkar se existe o número da nota utilizando regex pois o 
        # formato do número da nota é ${N} ${numero da nota}
        if not self.invoiceNumber and re.search(r'\d{3}\.\d{3}\.\d{3}', item):
                self.invoiceNumber = item.split()[-1]


    def check_verification_code(self, item, items, index):
        # checkar se é o campo de código de verificação vendo se tem a data
        # e também vendo se após a data tem a hora pois o formato
        #  do campo é ${numero da autorizacao} ${data} ${hora}
        # caso ele não consiga transformar a entrada em data e hora significa
        # que não é o campo que procuro
        if not self.verificationCode:
                splitted_items = item.split(' ')
                for index, split_item in enumerate(splitted_items):
                    try:
                        datetime.datetime.strptime(split_item,"%d/%m/%Y")
                        datetime.datetime.strptime(splitted_items[index+1],"%H:%M:%S")
                        self.verificationCode = splitted_items[0]
                    except:
                        pass


    def check_value(self, item, items, index):
        # pegar a posição onde se encontra o texto valor do frete(x)
        # e pegar a posição que se encontra o texto valor total(y) pois
        # o valor total se encontra y-x+1 casas a distancia da posição atual
        if not self.value:
                        if "VALOR DO FRETE" in item:
                            self.ship_field_pos = index
                        elif "VALOR TOTAL DA NOTA" in item:
                            self.total_field_pos = index
                            value_pos = index + self.total_field_pos - self.ship_field_pos + 1
                            self.value = items[value_pos]