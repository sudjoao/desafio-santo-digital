import re
import datetime
class InvoiceController():
    def __init__(self):
        self.invoice_number = None
        self.value = None
        self.verification_code = None
        self.ship_field_pos = 0
        self.total_field_pos = 0

    def get_invoice_data(self, items):
        for index, item in enumerate(items):
            if self.invoice_number and self.verification_code and self.value:
                break
            self.check_invoice_number(item)
            self.check_value(item, items, index)
            self.check_verification_code(item, items, index)
        return {
                "invoice_number": self.invoice_number,
                "value": self.value,
                "verification_code": self.verification_code
            }


    def check_invoice_number(self, item):
        #checkar se existe o número da nota utilizando regex pois o 
        # formato do número da nota é ${N} ${numero da nota}
        if not self.invoice_number and re.search(r'\d{3}\.\d{3}\.\d{3}', item):
                self.invoice_number = item.split()[-1]


    def check_verification_code(self, item, items, index):
        # checkar se é o campo de código de verificação vendo se tem a data
        # e também vendo se após a data tem a hora pois o formato
        # do campo é ${numero da autorizacao} ${data} ${hora}
        # caso ele não consiga transformar a entrada em data e hora significa
        # que não é o campo que procuro
        if not self.verification_code:
                splitted_items = item.split(' ')
                if len(splitted_items)>=3:
                    for index, split_item in enumerate(splitted_items):
                        try:
                            datetime.datetime.strptime(split_item,"%d/%m/%Y")
                            if ':' in splitted_items[index+1]:
                                hour_char=':'
                            else:
                                hour_char='.'
                            datetime.datetime.strptime(splitted_items[index+1],f"%H{hour_char}%M{hour_char}%S")
                        except:
                            continue
                        self.verification_code = splitted_items[0]
                        break
                    


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