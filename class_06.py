class Phone:
    IMEI = 'heima'
    producer = None

    def call_by_4g(self):
        print('4g通话')


class Phone2025(Phone):
    face_id = '10001'

    def call_by_5g(self):
        print('2025年新功能')
        

phone = Phone2025()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()



