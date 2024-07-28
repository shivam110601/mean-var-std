import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    tens = np.reshape(list, (3, 3))
    
    calculations = {
                    'mean': [np.mean(tens, axis=0).tolist(), np.mean(tens, axis=1).tolist(), np.mean(tens)],
                    'variance': [np.var(tens, axis=0).tolist(), np.var(tens, axis=1).tolist(), np.var(tens)],
                    'standard deviation': [np.std(tens, axis=0).tolist(), np.std(tens, axis=1).tolist(), np.std(tens)],
                    'max': [np.max(tens, axis=0).tolist(), np.max(tens, axis=1).tolist(), np.max(tens)],
                    'min': [np.min(tens, axis=0).tolist(), np.min(tens, axis=1).tolist(), np.min(tens)],
                    'sum': [np.sum(tens, axis=0).tolist(), np.sum(tens, axis=1).tolist(), np.sum(tens)]
                    }
    return calculations