import numpy as np

def compute_rmssd(rr_intervals):
    diff = np.diff(rr_intervals)
    return np.sqrt(np.mean(diff**2))


def compute_jerk(accel_data):
    accel_data = np.array(accel_data)
    jerk = np.diff(accel_data, axis=0)
    return np.mean(np.linalg.norm(jerk, axis=1))


def extract_features(data_window):
    hr_values = [d["hr"] for d in data_window]
    accel = [[d["ax"], d["ay"], d["az"]] for d in data_window]

    rr_intervals = 60 / np.array(hr_values)

    return [
        compute_rmssd(rr_intervals),
        compute_jerk(accel),
        np.mean(hr_values),
    ]