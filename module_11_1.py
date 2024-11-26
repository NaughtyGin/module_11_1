import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# requests
r = requests.get('https://api.github.com/events')  # объект класса Response для получения данных с сайта GitHub
print(r)  # возвращает результат обработки запроса (<Response [200]> - значит, всё хорошо)
print(f'Содержимое ответа сервера:\n{r.text}')  # вывод содержимого страницы
print()

print(f'Содержимое ответа сервера (JSON-данные):\n{r.json()}')  # вывод содержимого страницы для данных в формате JSON
print(r.raise_for_status())  # запрос обработанных исключений
print(r.status_code)  # возвращает код статуса отработки запроса (200 - значит, всё хорошо)
print()

r = requests.post('https://httpbin.org/post', data={'key': 'value'})  # POST-запрос для передачи данных на сервер
print(r.url)  # проверка правильности переданного URL-адреса
print(f'Кодировка: {r.encoding}')  # возвращает текущую кодировку

# pandas и numpy
s = pd.Series([1, 3, 5, np.nan, 6, 8])  # создание одномерного массива
print(s)  # вывод массива и типа данных

d = {"b": 1, "a": 0, "c": 2}
print(pd.Series(d))  # создание и вывод массива-словаря
d['a'] = -3
print(pd.Series(d))  # изменение значения по ключу
e = {"one": [1.0, 2.0, 3.0, 4.0], "two": [4.0, 3.0, 2.0, 1.0]}
print(pd.DataFrame(e))
pd.DataFrame(e, index=["a", "b", "c", "d"])
print(pd.DataFrame(e))

data = pd.read_csv('data_module_11_1.csv')  # Чтение данных из CSV-файла
print(data.head())  # Вывод первых пяти строк
print(data.head(3))  # Вывод первых трёх строк
print(data.describe())  # Описание данных: количество строк, в т.ч. уникальных, 1-я строка и частота её упомнинаия
print()
# matplotlib и numpy
x = np.linspace(0, 2 * np.pi, 200)  # получаем 200 равномерно распределенных значений на длине 2 Пи
y = np.sin(x)

fig, ax = plt.subplots()  # создание графика и осей как отдельных сущностей
ax.plot(x, y)
plt.show()  # вывод графика функции
plt.close('all')  # очистка всех графиков и освобождение памяти

np.random.seed()
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100
print(data)

fig1, ax1 = plt.subplots(sharey=True, figsize=(10, 8), layout='constrained')
ax1.scatter('a', 'b', c='c', s='d', data=data)
# x1 = np.linspace
ax1.plot('a', 'b', '', markeredgewidth=5, data=data, color='r')

ax1.set_xlabel('Значение a')
ax1.set_ylabel('Значение b')
ax1.set_title('Диаграмма рассеяния случайных значений a и b с рандомным размером и цветом маркера')
ax1.legend()
plt.show()
plt.close('all')
