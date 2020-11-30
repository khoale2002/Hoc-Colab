import matplotlib.pyplot as plt
color_names = ["Hung", "Hai", "Hung", "Khanh", "Long"]
colors = ["#3498db", "#fd79a8", "#f1c40f", "#273c75", "#e74c3c"]
num_favorite = [10,3,4,5,6]
xs = [i + 0.03 for i, _ in enumerate(color_names)]
plt.bar(xs, num_favorite, color=colors)
plt.title("Hoc sinh lop 9")
plt.xticks([i+0.1 for i, _ in enumerate(color_names)], color_names)
plt.xlabel("Ten")
plt.ylabel("Diem")
plt.show()