from random import randint

from aiogram import Bot, Dispatcher, executor, types
from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer
import torch

class Get_model:                                        # подключает нейронку 
    def __init__(self, path="./"):
        self.model_name_or_path = r'{}'.format(path)

    def turn0n_and_train_torch(self):
        if torch.cuda.is_available():       # определяем устройство для запуска нейронки
            self.DEVICE = torch.device("cuda:0")        # запуск на видеокарте
        else:
            self.DEVICE = torch.device("cpu")           # запуск на цп
        self.model = GPT2LMHeadModel.from_pretrained(self.model_name_or_path).to(self.DEVICE)
        self.tokenizer = GPT2Tokenizer.from_pretrained("sberbank-ai/rugpt3small_based_on_gpt2")
        self.trainer = Trainer(model=self.model)


class Gen_text:                                     # генерирует текст гороскопа в методе
    def gen(self, tok):
        input_ids = neuro.tokenizer.encode(tok, return_tensors="pt").to(neuro.DEVICE)
        neuro.model.eval()
        with torch.no_grad():
            out = neuro.model.generate(input_ids,
                                do_sample=True,
                                num_beams=2,
                                temperature=1.5,
                                top_p=0.9,
                                max_length=100,
                                )

        generated_text = list(map(neuro.tokenizer.decode, out))[0]
        # print()
        return generated_text[:generated_text.rfind('.')+1]

    zz = [['Овнам', 'Овны,'], ['Тельцам', 'Тельцы,'],           # c этого слова будет начинаться гороскоп
            ['Близнецам', 'Близнецы,'], ['Ракам', 'Раки,'],
            ['Львам', 'Львы,'], ['Девам','Девы,'],
            ['Весам', 'Весы,'], ['Скорпионом', 'Скорпионы,'],
            ['Стрельцам', 'Стрельцы,'], ['Козерогам', 'Козероги,'],
            ['Водолеям', 'Водолеи,'], ['Рыбам', 'Рыбы,']]


class Init_bot:                 # создает бота и его диспетчер
    def __init__(self, TOKEN):
        self.bot = Bot(token=TOKEN, parse_mode='HTML')
        self.dp = Dispatcher(bot=self.bot)


class Bot_kb:                   # конструирует и возвращает клавиатуру 
    def get_keyboard(self):
        buttons = [
            [
                types.InlineKeyboardButton(text="♈️Овен", callback_data="zodiac_oven"),
                types.InlineKeyboardButton(text="♉️Телец", callback_data="zodiac_telec"),
                types.InlineKeyboardButton(text="♊️Близнецы", callback_data="zodiac_blizneci")
            ],
            [
                types.InlineKeyboardButton(text="♋️Рак", callback_data="zodiac_rak"),
                types.InlineKeyboardButton(text="♌️Лев", callback_data="zodiac_lev"),
                types.InlineKeyboardButton(text="♍️Дева", callback_data="zodiac_deva")

            ],
            [
                types.InlineKeyboardButton(text="♎️Весы", callback_data="zodiac_vesi"),
                types.InlineKeyboardButton(text="♏️Скорпион", callback_data="zodiac_scorpion"),
                types.InlineKeyboardButton(text="♐️Стрелец", callback_data="zodiac_strelec")

            ],
            [
                types.InlineKeyboardButton(text="♑️Козерог", callback_data="zodiac_kozerog"),
                types.InlineKeyboardButton(text="♒️Водолей", callback_data="zodiac_vodoley"),
                types.InlineKeyboardButton(text="♓️Рыбы", callback_data="zodiac_ribi")
            ]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)      # клавиатура будет прикреплена к сообщению-ответу
        return keyboard

 
class User_mess:            # принимает сообщение пользователя и отсылает клавиатуру
    def __init__(self, dispatcher):
        self.dp = dispatcher
    def get_mess(self):
        @self.dp.message_handler(commands="start")  # бот будет реагировать на сообщение юзера "/start"
        async def func(message: types.Message):
            await message.answer("Выберите свой знак Зодиака", reply_markup=bkb.get_keyboard()) # отправка клавиатуры в юзеру


class Bot_ans:              # вызывает генератор текста и отправляет полученный гороскоп
    def __init__(self, dispatcher):
        self.dp = dispatcher
    def put_answer(self):
        @self.dp.callback_query_handler(text_startswith="zodiac_")  # получаем сообщение от одной из кнопок бота
        async def kbd(callback: types.CallbackQuery):
            action = callback.data.split("_")[1]                # отделяем в сообщении название знака зодиака
            signs = {"oven": 0, "telec": 1, "blizneci": 2, "rak": 3,
                    "lev": 4, "deva": 5, "vesi": 6, "scorpion": 7,
                    "strelec": 8, "kozerog": 9, "vodoley": 10, "ribi": 11
                    }
            p = new_text.zz[signs[action]][randint(0, 1)]       # с названия знака зодика будет начинаться сообщение
            ansver = new_text.gen(p)                            # здесь вызываем метод генерирующий текст гороскопа
            await callback.message.answer(ansver)


if __name__ == "__main__":
    neuro = Get_model('./model/')     # указываем путь до модели
    neuro.turn0n_and_train_torch()
    new_text = Gen_text()           # получаем генератор текста

    tg_bot = Init_bot("")              # активируем бота с токеном полученным от BotFather
    bkb = Bot_kb()                  # получаем класс-строитель клавиатуры
    reader = User_mess(tg_bot.dp)   
    reader.get_mess()               # получаем сообщение от пользователя
    writer = Bot_ans(tg_bot.dp)
    writer.put_answer()             # отвечаем на сообщение пользователя
    executor.start_polling(tg_bot.dp)
