import numpy as np
a = np.array([23, 34, 27])
b = np.array([-54, 1,  46])
c = np.array([46, 68, 54])

# Пишите здесь команды, который помогут
# найти ответы на вопросы
vectors = [a, b, c]
len_sum_vectors = np.array([np.linalg.norm(b+c), np.linalg.norm(a+c), np.linalg.norm(a+b)])
sum_len_vectors = np.array([np.linalg.norm(b) + np.linalg.norm(c), np.linalg.norm(a) \
                            + np.linalg.norm(c), np.linalg.norm(a) + np.linalg.norm(b)])
print(sum_len_vectors - len_sum_vectors)