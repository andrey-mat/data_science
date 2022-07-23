def get_loto(num):
    import numpy as np
    return np.random.randint(1, 101, size=(num, 5, 5))
    
print(get_loto(3))
