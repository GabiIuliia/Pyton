# Утверждение asseption


length=3

try:
    text=input(f'Введите текст больше {length} символов: ')
    assert len(text)>length #утверждение
    print(f'Вы ввели: {text} который больше {length} символов')
except AssertionError:
    print(f'Нет.Ваш текст короче, чем {length} символа')