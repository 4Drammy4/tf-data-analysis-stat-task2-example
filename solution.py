import numpy as np
from scipy import stats


chat_id = 416934694 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    mean = np.mean(data)
    std = np.std(data, ddof=1)
    t = stats.t.ppf((1 + confidence) / 2, n - 1)
    margin_of_error = t * std / np.sqrt(n)
    lower = mean - margin_of_error
    upper = mean + margin_of_error
    
    alpha = 1 - confidence
    p = alpha / 2 + 0.092
    b = (alpha - 0.092) / p + 0.092
    return (lower, upper)
