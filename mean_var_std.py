import numpy as np

def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(input_list).reshape(3, 3)

    calculations = {
        'mean': [
            arr.mean(axis=0).tolist(),    # column-wise mean
            arr.mean(axis=1).tolist(),    # row-wise mean
            arr.mean().item()             # overall mean
        ],
        'variance': [
            arr.var(axis=0).tolist(),    # column-wise variance
            arr.var(axis=1).tolist(),    # row-wise variance
            arr.var().item()             # overall variance
        ],
        'standard deviation': [
            arr.std(axis=0).tolist(),    # column-wise std
            arr.std(axis=1).tolist(),    # row-wise std
            arr.std().item()             # overall std
        ],
        'max': [
            arr.max(axis=0).tolist(),    # column-wise max
            arr.max(axis=1).tolist(),    # row-wise max
            arr.max().item()             # overall max
        ],
        'min': [
            arr.min(axis=0).tolist(),    # column-wise min
            arr.min(axis=1).tolist(),    # row-wise min
            arr.min().item()             # overall min
        ],
        'sum': [
            arr.sum(axis=0).tolist(),    # column-wise sum
            arr.sum(axis=1).tolist(),    # row-wise sum
            arr.sum().item()             # overall sum
        ]
    }

    return calculations