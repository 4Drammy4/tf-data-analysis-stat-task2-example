import numpy as np

from scipy import stats


chat_id = 416934694 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    mean = np.mean(x)
    std = np.std(x, ddof=1)
    t = stats.t.ppf((1 + p) / 2, n - 1)
    margin_of_error = t * std / np.sqrt(n)
    lower = mean - margin_of_error
    upper = mean + margin_of_error

    alpha = 1 - p
    x = alpha / 2 + 0.092
    b = (alpha - 0.092) / x + 0.092
    return (lower, upper)
