import random
import datetime

log = []

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '!monu':
        current_time = datetime.datetime.now()
        new_time = current_time + datetime.timedelta(minutes=90)
        formatted_time = new_time.strftime('%H:%M')
        formatted_time2 = current_time.strftime('%H:%M:%S %m-%d-%Y')
        result = f'>>> **Bir sonraki monu çıkış saati ➡️ __{formatted_time}__ ⌛ ** \n`{formatted_time2} tarihinde kesilen monuya 90 dakika eklenmiştir.` @here'
        log.append((message, result))
        return result

    

    if p_message == '!yardim':
        return '`!monukayit` mevcut saatten itibaren 90 dakika sonrasının kaydını alır, monu kesildikten hemen sonra kullanın. `!monutime` son alınan kaydı gösterir.'

    if p_message == '!log':
        if log:
            return log[-1][1]
        else:
            return 'Kayıt bulunamadı.'

