import numpy as np

def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(input_list).reshape(3, 3)

    calculations = {
        'mean': [
            arr.mean(axis=0).tolist(),    # axis1 mean
            arr.mean(axis=1).tolist(),    # axis2 mean
            arr.mean().item()             # flattened mean
        ],
        'variance': [
            arr.var(axis=0).tolist(),    # axis1 variance
            arr.var(axis=1).tolist(),    # axis2 variance
            arr.var().item()             # flattened variance
        ],
        'standard deviation': [
            arr.std(axis=0).tolist(),    # axis1 std
            arr.std(axis=1).tolist(),    # axis2 std
            arr.std().item()             # flattened std
        ],
        'max': [
            arr.max(axis=0).tolist(),    # axis1 max
            arr.max(axis=1).tolist(),    # axis2 max
            arr.max().item()             # flattened max
        ],
        'min': [
            arr.min(axis=0).tolist(),    # axis1 min
            arr.min(axis=1).tolist(),    # axis2 min
            arr.min().item()             # flattened min
        ],
        'sum': [
            arr.sum(axis=0).tolist(),    # axis1 sum
            arr.sum(axis=1).tolist(),    # axis2 sum
            arr.sum().item()             # flattened sum
        ]
    }

    return calculations