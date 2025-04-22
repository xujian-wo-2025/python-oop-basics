class Phone:
    IMEI = 'heima'
    producer = None

    def call_by_4g(self):
        print('4g通话')


class Phone2025(Phone):
    IMEI = 'jx'

    def call_by_5g(self):
        print(Phone.IMEI)
        print('2025年新功能')


phone = Phone2025()
print(phone.IMEI)
phone.call_by_4g()
phone.call_by_5g()
phone1 = Phone()
print(phone1.IMEI)
