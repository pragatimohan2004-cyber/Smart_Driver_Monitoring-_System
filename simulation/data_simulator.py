import numpy as np
import time
import random

def generate_sample(drowsy=False):
    if not drowsy:
        return {
            "hr": random.randint(70, 85),
            "spo2": random.randint(96, 99),
            "ax": np.random.normal(0.2, 0.05),
            "ay": np.random.normal(0.1, 0.05),
            "az": np.random.normal(9.7, 0.1),
        }
    else:
        return {
            "hr": random.randint(55, 70),
            "spo2": random.randint(93, 96),
            "ax": np.random.normal(0.05, 0.02),
            "ay": np.random.normal(0.03, 0.02),
            "az": np.random.normal(9.6, 0.05),
        }


def stream_data(window_size=20):
    data = []
    state = random.choice([True, False])

    for _ in range(window_size):
        data.append(generate_sample(drowsy=state))

    return data, state