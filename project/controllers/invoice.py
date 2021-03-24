class InvoiceController():
    def get_invoice_data(self, items):
        invoiceNumber = None
        value = None
        verificationCode = None
        for index, item in enumerate(items):
            if invoiceNumber and verificationCode and value:
                break
            if not invoiceNumber and "N°" in item:
                invoiceNumber = item
            elif not verificationCode and "AUTORIZAÇÃO" in item:
                verificationCode = items[index+1].split(' ')[0]
            elif not value and "VALOR TOTAL DA NOTA" in item:
                value = items[index+4]
        return {
                "invoiceNumber": invoiceNumber,
                "value": value,
                "verificationCode": verificationCode
            }
