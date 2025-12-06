# Purchase Amount Distribution by Customer Segment
# Generated for: 22f3000162@ds.study.iitm.ac.in

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sns.set_style("whitegrid")
sns.set_context("talk")

np.random.seed(42)
data = pd.DataFrame({
    'category': np.random.choice(['A', 'B', 'C', 'D'], 100),
    'value': np.random.randn(100) * 10 + 50
})

plt.figure(figsize=(8, 8))
sns.boxplot(data=data, x='category', y='value', palette='viridis')
plt.title('Purchase Amount Distribution by Customer Segment', fontsize=16, pad=20)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.tight_layout()
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
print("Chart saved as chart.png (512x512 pixels)")
