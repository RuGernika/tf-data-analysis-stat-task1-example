import pandas as pd
import numpy as np


chat_id = 1902092480 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    speeds = x
    num = len(x)
    error_dist = lambda x: -43 + np.random.exponential(1)
    measurements =[]
    for i in range(num):
      measurements = speeds + np.array([error_dist(x) for x in range(num)])
    variances = []
    for i in range(num):
      variances.append(1/np.exp(i+1)**2)
    weights = 1/np.asarray(variances)
    theta_hat = np.sum(weights * measurements) / np.sum(weights)
    return theta_hat

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
