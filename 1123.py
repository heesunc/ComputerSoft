import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(0)
data = np.random.randn(100, 2)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Descriptive Statistics
mean_vals = np.mean(data, axis=0)
median_vals = np.median(data, axis=0)

axes[0, 0].bar(['Mean', 'Median'], mean_vals, color=['blue', 'green'], alpha=0.7, label=['Variable 1', 'Variable 2'])
axes[0, 0].legend()
axes[0, 0].set_title('Descriptive Statistics: Mean and Median')

# Correlation Analysis
sns.heatmap(np.corrcoef(data.T), annot=True, ax=axes[0, 1], cmap='coolwarm')
axes[0, 1].set_title('Correlation Analysis')

# Histograms
bins = 15
colors = ['blue', 'green']

for i in range(2):
    axes[1, 0].hist(data[:, i], bins=bins, color=colors[i], alpha=0.7, label=f'Variable {i+1}')

axes[1, 0].legend()
axes[1, 0].set_title('Histogram of Variables')

# Scatter Plot
axes[1, 1].scatter(data[:, 0], data[:, 1], alpha=0.7)
axes[1, 1].set_xlabel('Variable 1')
axes[1, 1].set_ylabel('Variable 2')
axes[1, 1].set_title('Scatter Plot of Variable 1 vs Variable 2')

plt.tight_layout()
plt.show()
