import qrcode
""" В качестве примера взят кусок кода, который (код в целом)
  использует в качестве входных параметров файл .pdf, каждая страница которого представляет собой квитанцию по 
          оплате коммунальных услуг, 
  из каждой страницы выбирает необходимые данные, 
  собирает в строку и из неё генерирует QR-код, создает файл .jpg с данным QR-кодом 
   затем вставляет QR-код в необходимое место страницы.
   На выходе получается многостраничный файл .pdf c квитанциями с QR-кодами"""

# Обертка обрабатывает строку в QR-код и запоминает его в файл .jpg
def decorator_in_file(func):
    def wrapper(*args):
        print('принт в декораторе')
        res = func(*args)
        img = qrcode.make(res)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(res)
        qr.make(fit=True)
        type(img)  # qrcode.image.pil.PilImage
        img.save('C:/Users/User/промежуточный.png')
        print('после функции в декораторе')
        # return 'res'
    return wrapper

@decorator_in_file
#  здесь собирается строка с данными
def personal_account(PersAcc, LastName, FirstName, MiddleName, Kv, Summ, Period):
    total = ('ST00012|Name=ТСЖ "17-Б-6"|PersonalAcc=40703810300730004855|BankName=' +
    '"АО Банк ДОМ.РФ"|BIC=044525266|CorrespAcc=30101810345250000266|PayeeINN=6321098920|Category=' +
     'Оплата за коммунальные услуги|PersAcc=' + PersAcc +
     '|LastName=' + LastName + '|FirstName=' + FirstName + '|MiddleName=' + MiddleName +
     '|PayerAddress=ТОЛЬЯТТИ, пр-т СТЕПАНА РАЗИНА, д.82, ' + Kv + '|Sum=' + Summ + '|paymPeriod=' + Period)
    return total

pa = personal_account('50044650055', 'Кривенко', 'Евгений', 'Иванович', '1','3203042', '03.2024')
