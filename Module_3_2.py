
index_dog_sender = 0
index_dog_recipient = 0
home = 'university.help@gmail.com'
def send_email (massage, recipient, sender = "university.help@gmail.com"):
    global home
    index_dog_sender = sender.find('@')
    index_dog_recipient = recipient.find('@')
    if index_dog_sender < 0 or index_dog_recipient < 0:
        print(f'Невозможно отправить письмо с адреса: {sender} на адрес: {recipient}')

    dot_com = '.com'
    dot_ru = '.ru'
    dot_net = '.net'
    dot_uk = '.uk'
    idx_ext_sender = sender.find(dot_com) + sender.find(dot_ru) + sender.find(dot_net)
    idx_ext_recipient = recipient.find(dot_com) + recipient.find(dot_ru) + recipient.find(dot_net)
    idx_uk_sender = sender.find(dot_uk)
    idx_uk_recipient = recipient.find(dot_uk)
    a = home != sender and recipient != sender

    if idx_ext_sender and idx_ext_recipient < -2:
                print(f'DOT Невозможно отправить письмо с адреса: {sender} на адрес: {recipient}')
    if recipient == sender:
        print('Нельзя отправить письмо самому себе')
    if home == sender and recipient != sender:
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    if idx_uk_sender > 0:
        print(f'DOT Невозможно отправить письмо с адреса: {sender} на адрес: {recipient}')
    elif (idx_uk_sender < 0) and a == True:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
        return ()

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')