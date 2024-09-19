import requests
import pandas as pd
from datetime import datetime, timedelta

# Твой ключ API
access_key = 'your_api_key_here'

# Указываем заголовки, включающие ключ API
headers = {
    'X-Yandex-API-Key': access_key
}

# Координаты Калининграда (широта и долгота)
lat = 54.71016312
lon = 20.51013756

# Начало и конец сентября 2024
start_date = datetime(2024, 9, 1)
end_date = datetime(2024, 9, 30)

# Список для хранения данных
weather_data = []

# Проходим по каждому дню сентября
current_date = start_date
while current_date <= end_date:
    # Формируем запрос к API
    url = f'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&limit=1&hours=false&extra=false'

    # Делаем запрос
    response = requests.get(url, headers=headers)

    # Проверяем, успешен ли запрос
    if response.status_code == 200:
        # Извлекаем данные из ответа
        data = response.json()
        forecast = data['fact']

        # Извлекаем нужные данные: температура, влажность, скорость ветра
        temperature = forecast['temp']
        humidity = forecast['humidity']
        wind_speed = forecast['wind_speed']

        # Добавляем данные в список
        weather_data.append({
            'Дата': current_date.strftime('%Y-%m-%d'),
            'Температура': temperature,
            'Влажность': humidity,
            'Скорость ветра': wind_speed
        })
    else:
        print(f"Ошибка получения данных за {current_date.strftime('%Y-%m-%d')}: {response.status_code}")

    # Переходим к следующему дню
    current_date += timedelta(days=1)

# Создаем DataFrame
df = pd.DataFrame(weather_data)

# Записываем данные в Excel
df.to_excel('weather_data_september_2024.xlsx', index=False)

print("Данные успешно записаны в weather_data_september_2024.xlsx")
