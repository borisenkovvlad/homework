from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Информация'),
            KeyboardButton(text='Рассчитать')
        ],
        [KeyboardButton(text='Купить')]
    ], resize_keyboard=True
)

check_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories")],
        [InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")]
    ]
)

buy_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Product1", callback_data="product_buying"),
            InlineKeyboardButton(text="Product2", callback_data="product_buying"),
            InlineKeyboardButton(text="Product3", callback_data="product_buying"),
            InlineKeyboardButton(text="Product4", callback_data="product_buying")
        ]
    ]
)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=start_menu)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    with open("BOMBBAR.png", "rb") as BOMBBAR:
        await message.answer_photo(BOMBBAR, f"Название: Product1 | Описание: BOMBBAR | Цена: {1*100}")
    with open("Nattys.jpg", "rb") as Nattys:
        await message.answer_photo(Nattys, f"Название: Product2 | Описание: Nattys | Цена: {2*100}")
    with open("R.A.W.LIFE.jpg", "rb") as LIFE:
        await message.answer_photo(LIFE, f"Название: Product3 | Описание: R_A_W_LIFE | Цена: {3*100}")
    with open("Kultlab.jpg", "rb") as Kultlab:
        await message.answer_photo(Kultlab, f"Название: Product4 | Описание: Kultlab | Цена: {4*100}")
    await message.answer("Выберите продукт для покупки:", reply_markup=buy_menu)


@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer("Выберите опцию", reply_markup=check_menu)


@dp.callback_query_handler(text="formulas")
async def get_formulas(call):
    await call.message.answer("10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")
    await call.answer()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    a = int(data["weight"])
    b = int(data["growth"])
    c = int(data["age"])
    norma = 10*a+6.25*b-5*c+5
    await message.answer(f'Ваша норма калорий {norma}')
    await state.finish()


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
