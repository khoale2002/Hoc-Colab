import matplotlib.pyplot as plt, numpy as np
x = np.random.randn(30) + np.arange(0, 30)*0.75 + 10
y = np.random.randn(10) + np.arange(0, 10)*1.0 +20
z = np.random.randn(10) + np.arange(0, 10)*0.5 + 5
t = np.random.randn(40) + np.arange(0, 40)*0.4 + 0.0

plt.boxplot([x, y, z, t],
            labels = ['Mùa Xuân', 'Mùa Hạ', 'Mùa Thu','Mùa Đông'],
            showfliers = True)

plt.title('''bieu do the hien su bien thien nhiet do''')
plt.xlabel('Mùa')
plt.ylabel('Chỉ số nhiệt độ ')
plt.show()