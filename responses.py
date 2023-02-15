import random
import datetime
from datetime import timedelta
import pytz

log = [] 
last_monu_time = None
last_monu2_time = None

def get_response(message: str) -> str:
    p_message = message.lower()

    global last_monu_time
    global last_monu2_time

    # Tr zamanı
    turkey_tz = pytz.timezone('Turkey')

    if p_message == '!monu':
        now = datetime.datetime.now(turkey_tz)
        if last_monu_time is not None and (now - last_monu_time) < timedelta(minutes=89):
            return '⌛ Monu çıkış saati halihazırda belirlenmiştir. Lütfen bir önceki bot mesajını kontrol ediniz. Göremiyorsanız **!log** komutunu kullanabilirsiniz.'

        current_time = datetime.datetime.now(turkey_tz)
        new_time = current_time + timedelta(minutes=90)
        formatted_time = new_time.strftime('%H:%M')
        formatted_time2 = current_time.strftime('%H:%M:%S %m-%d-%Y')
        result = f'>>> **Bir sonraki monu çıkış saati ➡️ __{formatted_time}__ ⏰ ** \n`{formatted_time2} tarihinde kesilen monuya 90 dakika eklenmiştir.` @here'
        log.append((message, result))
        last_monu_time = now
        return result

    if p_message == '!monu2':
        now = datetime.datetime.now(turkey_tz)
        if last_monu2_time is not None and (now - last_monu2_time) < timedelta(minutes=89):
            return '⌛ DV2 monu çıkış saati halihazırda belirlenmiştir. Lütfen bir önceki bot mesajını kontrol ediniz. Göremiyorsanız **!log** komutunu kullanabilirsiniz.'

        current_time = datetime.datetime.now(turkey_tz)
        new_time = current_time + timedelta(minutes=90)
        formatted_time = new_time.strftime('%H:%M')
        formatted_time2 = current_time.strftime('%H:%M:%S %m-%d-%Y')
        result = f'>>> **__DV 2__ bir sonraki monu çıkış saati ➡️ __{formatted_time}__ ⏰ ** \n`{formatted_time2} tarihinde kesilen monuya 120 dakika eklenmiştir.` @here'
        log.append((message, result))
        last_monu2_time = now
        return result

    if p_message == '!yardim' or p_message == '!yardım':
        return '- Monument kesildikten hemen sonra **!monu**, DV 2 için **!monu2** yazınız. Bot bir sonraki monu çıkış saatini yazacaktır.\n- Bot tarafından girilmiş olan son saatleri görmek için **!log** yazabilirsiniz.'

    if p_message == '!log':
        if log:
            return 'Bot tarafından girilmiş olan son saatler aşağıdadır:\n\n' + '\n\n'.join([f'{i+1}. {log[i][1]}' for i in range(len(log)-1, -1, -1)])
        else:
            return 'Kayıt bulunamadı'
