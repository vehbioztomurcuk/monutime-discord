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

    # Setting Turkey time zone
    turkey_tz = pytz.timezone('Turkey')

    if p_message.startswith('!monu'):
        adjustment = 0
        if len(p_message) > 5:
            try:
                adjustment = int(p_message[5:])
            except ValueError:
                return '>>> Geçersiz parametre girdiniz lütfen sayı kullanın. !yardim'

        if adjustment < -90:
            return 'Adjustment value cannot be less than -90.'

        now = datetime.datetime.now(turkey_tz)
        if p_message == '!monu' and last_monu_time is not None and (now - last_monu_time) < timedelta(minutes=60):
            return '⌛ Monu çıkış saati halihazırda belirlenmiştir. Lütfen bir önceki bot mesajını kontrol ediniz. Göremiyorsanız **!log** komutunu kullanabilirsiniz.'

        current_time = datetime.datetime.now(turkey_tz)
        new_time = current_time + timedelta(minutes=(90 + adjustment))
        formatted_time = new_time.strftime('%H:%M')
        formatted_time2 = current_time.strftime('%H:%M')
        result = f'>>> **Bir sonraki monu çıkış saati ⏰ __{formatted_time}__ ⏰ ** \n`{formatted_time2} saatinde kesilen monuya {90 + adjustment} dakika eklenmiştir.` @here'
        log.append((message, result))
        if p_message == '!monu':
            last_monu_time = now
        return result

    if p_message == '!monu2':
        now = datetime.datetime.now(turkey_tz)
        if last_monu2_time is not None and (now - last_monu2_time) < timedelta(minutes=60):
            return '⌛ DV2 monu çıkış saati halihazırda belirlenmiştir. Lütfen bir önceki bot mesajını kontrol ediniz. Göremiyorsanız **!log** komutunu kullanabilirsiniz.'

        current_time = datetime.datetime.now(turkey_tz)
        new_time = current_time + timedelta(minutes=90)
        formatted_time = new_time.strftime('%H:%M')
        formatted_time2 = current_time.strftime('%H:%M')
        result = f'>>> **__DV 2__ bir sonraki monu çıkış saati ⏰ __{formatted_time}__ ⏰ ** \n`{formatted_time2} saatinde kesilen monuya 90 dakika eklenmiştir.` @here'
        log.append((message, result))
        last_monu2_time = now
        return result
    
    
    if p_message == '!yardim':
        return '**!monu**\n`Anlık zamana 90 dakika ekleyerek bir sonraki monu çıkış saatini belirler. Monu kesildiği an yazılmalıdır.\n`**!monu2**\n`!monu komutunun aynısı Dv2 için`\n**!monu-x**\n`Monu saatini x dakika çıkararak söyler. Ör: !monu-5 anlık zamana 90 yerine 85 dakika ekler. (aynısı !monu2-x için de geçerlidir)`\n**!monureset**\n`Tüm monu zamanlarını resetler ve komut tekrarı kısıtlamalarını kaldırır.`\n**!log**\n`Bot tarafından girilmiş son zamanları gösterir.`'

    if p_message == '!log':
        if log:
            return 'Bot tarafından girilmiş olan son saatler aşağıdadır:\n\n' + '\n\n'.join([f'{i+1}. {log[i][1]}' for i in range(len(log)-1, -1, -1)])
        else:
            return 'Kayıt bulunamadı'


    if p_message == '!monureset':

     log.clear()
    last_monu_time = None
    last_monu2_time = None
    return '>>> Monu saati sıfırlanmıştır.'

