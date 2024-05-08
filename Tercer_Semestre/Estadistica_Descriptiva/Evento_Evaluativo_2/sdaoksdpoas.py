# libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a dataframe
df = pd.DataFrame({'group': list(map(chr, range(65, 85))), 'values': np.random.uniform(size=20)})

# Reorder it based on the values:
ordered_df = df.sort_values(by='values')
my_range = range(1, len(df.index) + 1)

# Make the plot
plt.stem(ordered_df['values'])
plt.xticks(my_range, ordered_df['group'])
plt.show()

# Horizontal version
plt.hlines(y=my_range, xmin=0, xmax=ordered_df['values'], color='skyblue')
plt.plot(ordered_df['values'], my_range, "D")
plt.yticks(my_range, ordered_df['group'])
plt.show()