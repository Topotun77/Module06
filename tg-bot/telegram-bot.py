# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
#
# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')



# from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters   #, ContextTypes
from datetime import datetime
from re import compile, UNICODE
from random import randint
# from os import chdir
word_dic = {
    1: ['купить', 'покупки', '1'],
    2: ['купил', 'купила', '2'],
    3: ['зовут', 'имя', '3'],
    4: ['время', 'времени', 'час', '4'],
    5: ['хорош', 'отличн', 'великолепн'],
    6: ['плох', 'ужасн', 'отвратит'],
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
    '- Рабинович, а ви слышали, шо в будущем не будет денег? \n- Да вы шо, и в будущем тоже?!',
]

def save_log(text):
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
        return emoji_pattern.sub(r':)', text)

    file_ = 'log.txt'
    fl = open(file_, "a")
    # fl = open(file_, "a", encoding='utf-8')
    txt3_ = (str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + remove_smile(text) + '\n')
    fl.write(txt3_)
    fl.close()

def str_log(update, context):
    return (f'   Name={update.message.from_user.first_name}, username=@{update.message.from_user.username},' +
            f' text="{update.message.text}"')


async def start(update, context):
    txt2_ = f'Привет, {update.effective_user.first_name}! Как дела?'
    await update.message.reply_text(txt2_)
    txt2_ = txt2_
    save_log('test \n')
    print(str_log(update, context) + '\nBot message:        ' + txt2_ + '\n')
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

    print(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')), update)
    txt_ = str(update.message.text)
    txt_up = txt_.upper()
    print(txt_up, str(list(word_dic.values())).upper())
    bool_ = False
    txt2_ = ''
    for k, i in word_dic.items():
        for j in i:
            if j.upper() in txt_up:
                txt2_ += '\n'
                if k == 1:      # Список покупок
                    txt2_ += read_list()
                elif k == 2:    # Все купили
                    write_list()
                    txt2_ += read_list()
                elif k == 3:
                    txt2_ += 'Меня зовут Бот Тестовый. Приятно с Вами познакомиться!\n'
                elif k == 5:
                    txt2_ += 'Мне нравится Ваш позитивный настрой!!!\n'
                elif k == 6:
                    txt2_ += ('Жаль, что у вас не очень хорошее настроение, надеюсь анекдот из моей '
                              'базы поднимет его Вам.\n\n')
                    txt2_ += anecdote[randint(0, len(anecdote))] + '\n'
                else:
                    txt2_ += f'Московское время: {str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}\n'
                bool_ = True
    if not bool_:
        txt2_ = (f'Это Вы только что написали: \n__{txt_}__?\nНо я пока не очень умный, поэтому '
                 f'могу разбирать только несколько ключевых слов, позже расскажу каких, '
                 f'пока догадывайтесь сами )))')
        txt2_ += '\n\nТак я отвечал раньше, теперь могу перчислить ключевые слова:\n\n'
        for i in word_dic.values():
            for j in i:
                txt2_ += str(j) + ', '
        txt2_ = txt2_[0:-2]
    await update.message.reply_text(txt2_)
    txt3_ = (str_log(update, context) + '\nBot message:        ' + txt2_ + '\n')
    save_log(txt3_)

app = ApplicationBuilder().token("7203239340:AAEEQUneDEhXnfT3UKkTdGesDLYhuUnYJBA").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, get_text))
print('Бот запущен')
app.run_polling()