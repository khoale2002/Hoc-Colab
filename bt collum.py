import matplotlib.pyplot as plt, numpy as np

bt, bt_std = (4, 7, 3, 5, 2), (3, 4, 5, 2, 3)
btvn, btvn_std = (1, 1, 9, 13, 7), (4, 6, 3, 4, 4)
ind = np.arange(len(bt))
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, bt, width, yerr=bt_std,
                label='Bài tập ',color='#74b9ff')
rects2 = ax.bar(ind + width/2, btvn, width, yerr=btvn_std,
                label='BTVN',color='#d63031')
ax.set_xticks(ind)
ax.set_xticklabels(('Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5'))
plt.title('''   Biểu đồ thể hiện so bai tap
   bài tập lập trình ''')
plt.xlabel("Thời gian trải qua")
plt.ylabel("Số bài tập ")
ax.legend()
plt.show()