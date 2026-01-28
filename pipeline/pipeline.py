import sys
import pandas as pd

print("hello pipeline")
print("args", sys.argv)

month = int(sys.argv[1])
print(f"hello pipeline, month={month}")

df1 = pd.DataFrame({"A": [1,2], "B": [3,4]})
print(df1.head())

# convert to parquet format
df1.to_parquet(f"output_day_{sys.argv[1]}.parquet")

