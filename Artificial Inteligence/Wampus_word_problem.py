import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Use a universal font instead of Stable!
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']

# Data generation for plants
train_num = 200  # Total training samples
test_num = 100   # Not used in this script, but can be added for test set

# Configuration ranges for each feature per plant type
config = {
    'Corn': [[150, 190], [40, 700], [20, 41]],
    'Potato': [[300, 600], [70, 10], [10, 20]],
    'Grass': [[100, 40], [10, 40], [505, 1]]
}

plants = list(config.keys())

# Create empty dataframe with 3 features + 1 label column
dataset = pd.DataFrame(columns=['height(m)', 'leaf length(m)', 'Stem diameter(m)', 'type'])
index = 0

# Generate correct samples (balanced for each class)
for p in config:
    for i in range(int(train_num / 3) - 3):  # Generate equal samples for each plant
        row = []
        for j, (min_val, max_val) in enumerate(config[p]):
            v = round(np.random.rand() * (max_val - min_val) + min_val, 2)
            while v in dataset[dataset.columns[j]].values:
                v = round(np.random.rand() * (max_val - min_val) + min_val, 2)
            row.append(v)
        row.append(p)
        dataset.loc[index] = row
        index += 1

# Add mislabeled data (wrong class on purpose)
for i in range(train_num - index):
    k = np.random.randint(3)
    p = plants[k]
    row = []
    for j, (min_val, max_val) in enumerate(config[p]):
        v = round(np.random.rand() * (max_val - min_val) + min_val, 2)
        while v in dataset[dataset.columns[j]].values:
            v = round(np.random.rand() * (max_val - min_val) + min_val, 2)
        row.append(v)
    # Mislabel with next class cyclically
    row.append(plants[(k + 1) % 3])
    dataset.loc[index] = row
    index += 1

# Shuffle data and reset index
dataset = dataset.sample(frac=1).reset_index(drop=True)

# Save data to CSVs
dataset.iloc[:train_num, :-1].to_csv('potato_train_data.csv', index=False)
dataset.iloc[:train_num, [-1]].to_csv('potato_train_label.csv', index=False)

# Visualization function
def visualize(dataset, labels, features, classes, fig_size=(10, 10), layout=None):
    plt.figure(figsize=fig_size)
    index = 1
    if layout is None:
        layout = [len(features), 1]
    for i in range(len(features)):
        for j in range(i + 1, len(features)):
            p = plt.subplot(layout[0], layout[1], index)
            plt.subplots_adjust(hspace=0.4)
            p.set_title(f"{features[i]} & {features[j]}")
            p.set_xlabel(features[i])
            p.set_ylabel(features[j])
            for k in range(len(classes)):
                p.scatter(dataset[labels == k, i], dataset[labels == k, j], label=classes[k])
            p.legend()
            index += 1
    plt.show()

# Load saved data
dataset = pd.read_csv('potato_train_data.csv')
labels = pd.read_csv('potato_train_label.csv')

# Feature names and class labels
features = list(dataset.columns)
classes = np.array(['Corn', 'Potato', 'Grass'])

for i,cls in enumerate(classes):
    labels.loc[labels['type'] == cls, 'type'] = i

dataset = dataset.values.astype(float)
labels = labels['type'].astype(int).values

visualize(dataset, labels, features[:-1], classes, fig_size=(10, 10), layout=[3, 3])