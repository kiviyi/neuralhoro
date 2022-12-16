from random import randint

from aiogram import Bot, Dispatcher, executor, types
from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer
import torch

class Get_model:
    def __init__(self, path="./"):
        self.model_name_or_path = r'{}'.format(path)

    def turn0n_and_train_torch(self):
        if torch.cuda.is_available():
            self.DEVICE = torch.device("cuda:0")
        else:
            self.DEVICE = torch.device("cpu")
        self.model = GPT2LMHeadModel.from_pretrained(self.model_name_or_path).to(self.DEVICE)
        self.tokenizer = GPT2Tokenizer.from_pretrained("sberbank-ai/rugpt3small_based_on_gpt2")
        self.trainer = Trainer(model=self.model)


class Gen_text:
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

    zz = [['Овнам', 'Овны,'], ['Тельцам', 'Тельцы,'],
            ['Близнецам', 'Близнецы,'], ['Ракам', 'Раки,'],
            ['Львам', 'Львы,'], ['Девам','Девы,'],
            ['Весам', 'Весы,'], ['Скорпионом', 'Скорпионы,'],
            ['Стрельцам', 'Стрельцы,'], ['Козерогам', 'Козероги,'],
            ['Водолеям', 'Водолеи,'], ['Рыбам', 'Рыбы,']]


class Init_bot:
    def __init__(self, TOKEN):
        self.bot = Bot(token=TOKEN, parse_mode='HTML')
        self.dp = Dispatcher(bot=self.bot)
    def return_dispatcher(self):
        return self.dp


class Bot_kb:
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
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

 
class User_mess:
    def __init__(self, dispatcher):
        self.dp = dispatcher
    def get_mess(self):
        @self.dp.message_handler(commands="start")
        async def func(message: types.Message):
            await message.answer("Выберите свой знак Зодиака", reply_markup=bkb.get_keyboard())


class Bot_ans:
    def __init__(self, dispatcher):
        self.dp = dispatcher
    def put_answer(self):
        @self.dp.callback_query_handler(text_startswith="zodiac_")
        async def kbd(callback: types.CallbackQuery):
            action = callback.data.split("_")[1]
            signs = {"oven": 0, "telec": 1, "blizneci": 2, "rak": 3,
                    "lev": 4, "deva": 5, "vesi": 6, "scorpion": 7,
                    "strelec": 8, "kozerog": 9, "vodoley": 10, "ribi": 11
                    }
            p = new_text.zz[signs[action]][randint(0, 1)]
            ansver = new_text.gen(p)
            await callback.message.answer(ansver)


print("start")
if __name__ == "__main__":
    neuro = Get_model(r'C:\Users\asus rog\Documents\parsinghoroscop\rnn\model')
    neuro.turn0n_and_train_torch()
    new_text = Gen_text()

    tg_bot = Init_bot("5837522256:AAEuPRqL8Uhh_ADHFFNZxycFeUZfJUkUxQo")
    bkb = Bot_kb()
    reader = User_mess(tg_bot.return_dispatcher())
    reader.get_mess()
    writer = Bot_ans(tg_bot.return_dispatcher())
    writer.put_answer()
    executor.start_polling(tg_bot.return_dispatcher())
