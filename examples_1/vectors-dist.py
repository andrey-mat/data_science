import numpy as np
a = np.array([23, 34, 27])
b = np.array([-54, 1,  46])
c = np.array([46, 68, 54])

# Пишите здесь команды, который помогут
# найти ответы на вопросы
vectors = np.array([a, b, c])
diff_vectors = np.array([np.linalg.norm(a-b), np.linalg.norm(a-c), np.linalg.norm(b-c)])
print(diff_vectors)
