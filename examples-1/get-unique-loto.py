def get_unique_loto(num):
    import numpy as np
    loto = []
    possible_loto = np.arange(1, 101)
    for i in range(num):
        loto.append(np.random.choice(possible_loto, size=(5, 5), replace=False))
    loto = np.array(loto)
                    
    return loto
    
print(get_unique_loto(3))
