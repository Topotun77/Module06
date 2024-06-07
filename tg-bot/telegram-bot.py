# -*- coding: utf-8 -*-
# from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters   #, ContextTypes
from telegram import ReplyKeyboardMarkup
from datetime import datetime
from re import compile, UNICODE
from random import randint
import neural_net

# from os import chdir
word_dic = {
    1: ['купить', 'покупки', 'список'],
    2: ['купил', 'куплен'],
    3: ['зовут', 'имя'],
    4: ['время', 'времен', 'час'],
    5: ['хорош', 'отличн', 'великолепн'],
    6: ['плох', 'ужасн', 'отвратит'],
    7: ['войн'],
    8: ['анекдот']
}
anecdote = [
    'Девушка становится женщиной, когда впервые говорит: «Это хороший пакет, не выбрасывай!»',
    'Мяч еще летел в окно директора, а дети уже играли в прятки.',
    'Прошлой ночью не получилось вызвать такси до дома, так я зашел в кафе, заказал доставку '
    'на свой адрес и уехал вместе с водителем.',
    'Сбербанк отнес стоимость посещения мной платного туалета к категории "Развлечения и хобби". '
    'Вот сижу и думаю, это моё развлечение? Или моё хобби?',
    'Объявление: "Ищу высокого мужчину, чтобы помог снять тюль для стирки. Разовые отношения не '
    'интересуют - потом тюль нужно будет повесить обратно".',
    '  - Рабинович, а ви слышали, шо в будущем не будет денег? \n  - Да вы шо, и в будущем тоже?!',
    'Передача "Жди меня". \n  - Мой муж ушёл из дома 4 года назад. За это время я родила ему '
    'четверых детей. Имей совесть, Алёша. Вернись домой.',
    'Если человек, проходя по улице мимо кота, не говорит ему автоматически кс-кс, то я к '
    'такому человеку сразу отношусь настороженно. Он явно рептилоид, или жук-оборотень, или масон. '
    'Звуковое пингование случайных котов — единственнoe, что отличаeт человека от потусторонней '
    'сущности.',
    'Как определить, кто в дорогом отеле миллиардер, а кто обслуживающий персонал? \n'
    '  -Миллиардер ходит в мятой майке, шортах и шлёпках. А обслуживающий персонал - в '
    'выглаженных деловых костюмах, рубашках и галстуках.',
    '   Фотоальбом наших прабабушек:\n1928 — пошла в школу (1 фото)\n1938 — закончила школу '
    '(3 фото)\n1945 — окончила университет (1 фото)\n1946 — вышла замуж (3 фото).'
    '\n\n   Фотоальбом их правнучек:\n19:38 — пришла в кафе (28 фото)\n19:41 — принесли меню '
    '(19 фото)\n19:52 — принесли Цезарь (20 фото)\n19:56 – принесли отбивные (19 фото)'
    '\n19:58 — пошла в туалет пописять (80 фото)\n20:03 — выходя из туалета встретила '
    'подружку (52 фото)\n20:15 — принесли кофе и мороженку (38 фото)\n20:29 — принесли счет (11 фото)',
    'Весна - она как женщина. Кричит "Иду уже, иду", а сама ещё сидит в ванной с мокрой головой и ногти красит.',
    'Книга получается хорошей, если автор действительно знает то, о чём пишет. Фильм получается хорошим, '
    'если сценарист, режиссёр, актёры хотя бы отчасти пережили то, о чём рассказывают. Поэтому лучше всего '
    'у киношников выходят фильмы про истеричных дегенератов, алкоголиков и проституток, а хуже всего - '
    'про добрых честных людей, хорошо делающих своё дело.'
]


def remove_smile(text):
    emoji_pattern = compile("["
                            u"\U0001F600-\U0001F64F"  # emoticons
                            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                            u"\U0001F680-\U0001F6FF"  # transport & map symbols
                            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            u"\U0001F1F2-\U0001F1F4"  # Macau flag
                            u"\U0001F1E6-\U0001F1FF"  # flags
                            u"\U0001F600-\U0001F64F"
                            u"\U00002702-\U000027B0"
                            u"\U000024C2-\U0001F251"
                            u"\U0001f926-\U0001f937"
                            u"\U0001F1F2"
                            u"\U0001F1F4"
                            u"\U0001F620"
                            u"\u200d"
                            u"\u2640-\u2642"
                            "]+", flags=UNICODE)
    text = emoji_pattern.sub(r':)', text)
    text_2 = ''
    for c in text:
        try:
            print(c, end='')
            text_2 += c
        except:
            print(c.encode().hex(), end='')
            text_2 += c.encode().hex()
    return text_2


def save_log(text):
    file_ = 'log.txt'
    with open(file_, "a", encoding='utf-8') as fl:
        # fl = open(file_, "a", encoding='utf-8')
        # txt3_ = (str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + remove_smile(text) + '\n')
        # txt3_ = (str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + text.encode(encoding='utf-8') + '\n')
        fl.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        # fl.write(str(text.encode(encoding='utf-8')))
        fl.write(text)
        fl.write('\n')


def str_log(update, context):
    # return (f'   username=@{update.message.from_user.username},' +
    #         f' text="{update.message.text}"')
    # return (f'   Name={update.message.from_user.first_name}, username=@{update.message.from_user.username},' +
    #         f' text="{update.message.text}"')
    return str(update)


async def start(update, context):
    buttons = [['Список покупок', 'Пометить как "куплено"'], ['Хочу анекдот']]
    my_kb = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    txt2_ = f'Привет, {update.effective_user.first_name}! Как дела?'
    await update.message.reply_text(txt2_, reply_markup=my_kb)
    # txt2_ = txt2_
    # save_log('test \n')
    print(remove_smile(str_log(update, context) + '\nBot message:        ' + txt2_ + '\n'))
    save_log(str_log(update, context) + '\nBot message:        ' + txt2_ + '\n')


async def get_text(update, context):
    def read_list():
        txt_ = ''
        file_ = 'list.txt'
        fl = open(file_, "r")
        while True:
            ln = fl.readline()
            if not ln:
                break
            txt_ += ln
        fl.close()
        return txt_

    def write_list():
        file_ = 'list.txt'
        fl = open(file_, "a")
        fl.write('\n ____По этому списку куплено____\n')
        fl.close()

    # print(str(update)[140:400])
    print(remove_smile(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + remove_smile(str(update))))
    txt_ = str(update.message.text)
    txt_up = txt_.upper()
    print(remove_smile(txt_up), str(list(word_dic.values())).upper())
    bool_ = False
    txt2_ = ''
    for k, i in word_dic.items():
        for j in i:
            if txt_up.isnumeric() and int(txt_up) == k:
                txt_up = word_dic[k][0].upper()
            if j.upper() in txt_up:
                txt2_ += '\n'
                if k == 1:  # Список покупок
                    txt2_ += read_list()
                elif k == 2:  # Все купили
                    write_list()
                    txt2_ += read_list()
                elif k == 3:
                    txt2_ += 'Меня зовут Бот Тестовый. Приятно с Вами познакомиться!\n'
                elif k == 5:
                    txt2_ += 'Мне нравится Ваш позитивный настрой!!!\n'
                elif k == 6:
                    txt2_ += ('Жаль, что у вас не очень хорошее настроение, надеюсь анекдот из моей '
                              'базы поднимет его Вам.\n\n')
                    txt2_ += anecdote[randint(0, len(anecdote))-1] + '\n'
                elif k == 7:
                    txt2_ += ('Тема войны, конечно, сейчас очень актуальна, но все же меня создавали '
                              'не для ее обсуждение. Когда меня подключат к нейронной сити, мы с вами обсудим '
                              'и эту тему, а пока лучше спросите что-то еще, нажмите на /start или '
                              'пожалуйтесь на плохое настроение\n')
                elif k == 8:
                    txt2_ += ('Вы хотели анекдот? Тогда слушайте:\n\n')
                    txt2_ += anecdote[randint(0, len(anecdote))-1] + '\n'
                else:
                    txt2_ += f'Московское время: {str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}\n'
                bool_ = True
    if not bool_:
        re_chat = chatterer.chat(N=200, out_file_name='return', space_num=0, start_txt=txt_)
        if re_chat[0]:
            txt2_ = f'Моя супернейросеть сгенерировала для Вас вот такой ответ:\n\n' + re_chat[1]
            txt2_ = txt2_[0:txt2_.rfind(' ')] + '.'
        else:
            txt2_ = (f'Это Вы только что написали: \n__{txt_}__?\nНо я пока не очень умный, поэтому '
                     f'могу разбирать только несколько ключевых слов, позже расскажу каких, '
                     f'пока догадывайтесь сами )))')
            txt2_ += ('\n\nТак я отвечал раньше, теперь могу перечислить ключевые слова и сообщить, '
                      'что могу отвечать на более длинные запросы:\n\n')
            for i in word_dic.values():
                for j in i:
                    txt2_ += str(j) + ', '
            txt2_ = txt2_[0:-2] + '\n\n     Попробуйте еще раз /start\n'
    await update.message.reply_text(txt2_)
    txt3_ = (str_log(update, context) + '\nBot message:        ' + txt2_ + '\n')
    save_log(txt3_)


chatterer = neural_net.Chatterer(file_name='text.txt')
chatterer.collect()
chatterer.prepare()
# chatterer.chat(N=10000, out_file_name='out.txt')
# re_txt = chatterer.chat(N=200, out_file_name='return', space_num=0,
#                      start_txt='Я бы очень хотел от вас услышать ответ на один вопрос')

app = ApplicationBuilder().token("XXX").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, get_text))
print('Бот запущен')
app.run_polling()
