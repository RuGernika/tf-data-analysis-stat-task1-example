import pandas as pd
import numpy as np


chat_id = 1902092480 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t=10 
    return x.mean() # Ваш ответ

# 1 Условие
# На заводе проводится тестирование модели машины для проверки коэффициента ускорения. В рамках эксперимента выбирается п машин этой модели и измеряется скорость машины через 10 секунд. Предполагается, что ошибки измерения скорости н.о.р. и имеют распределение -43 + еxp(1). Постройте точечную оценку коэффициента ускорения.
# 2 Входные данные
# Одномерный массив numpy.ndarray измерений скорости (в м/с) машин одной модели.
# 3 Возвращаемое значение
# Оценка коэффициента ускорения (в м/с2).
# 4 Оценка
# +1 балл, если на выборках размера 1000 MSE оценки 0.000951.
# +1 балл, если на выборках размера 1000 MSE оценки < 0.0000951.
# +1 балл, если на выборках размера 100 MSE оценки < 0.000283.
