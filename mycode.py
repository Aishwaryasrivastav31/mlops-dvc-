import pandas as pd
import os

# Ensure all columns have the same length
df = {
    "name": ["a", "b", "c"],
    "age": [20, 24, 28],     # 3 values
    "marks": [100, 90, 80]
}
data = pd.DataFrame(df)

# Directory path (not the data)
data_dir = "data_dir"
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, "sample.csv")
data.to_csv(file_path, index=False)

print("file saved successfully at", file_path)