# Сложное условие (логическое "И")
# 6<=hour<12-доброе утро
# 12<=hour<17- добрый день
# 17<=hour<20-добрый вечер
# доброй ночи


hour = 5

# Первый способ
if hour >= 6 and hour < 12:
    print('Доброе утро')
elif hour >= 12 and hour < 17:
    print('Добрый день')
elif hour >= 17 and hour < 20:
    print('Добрый вечер')
else:
    print('Доброй ночи')

#Второй способ
if 6 <= hour < 12:
    print('Доброе утро')
elif 12 <= hour < 17:
    print('Добрый день')
elif 17 <= hour < 20:
    print('Добрый вечер')
else:
    print('Доброй ночи')