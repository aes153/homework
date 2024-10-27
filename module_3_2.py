def send_email(message, recipient, *, sender = 'university.help@gmail.com'):

    def is_valid_email(email):
        domains = ('.com', '.ru', '.net')
        return '@' in email and (email.endswith(domains))

    if not is_valid_email(sender) or not is_valid_email(recipient):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    if sender  == recipient:
        print('Нельзя отправить письмо самому себе!')
        return

    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

send_email('Вебинар состоится сегодня в 17.00', 'anna@mail.ru')
send_email('Что в имени тебе моем?', 'natali@mail.ru', sender='pushkin@mail.su')
send_email('Я пришел к тебе с приветом', 'a.fet@mail.ru', sender='a.fet@mail.ru')
send_email('Выхожу один я на дорогу', 'a.fet@mail.ru', sender='a.lermontov@mail.ru')




