def get_chess(x=1):
    import numpy as np
    arr = np.zeros((x, x), dtype=np.int64)
    arr[::2,1::2] = 1
    arr[1::2,::2] = 1
    return arr
    
    
print(get_chess(30))