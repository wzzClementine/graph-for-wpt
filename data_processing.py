
import numpy as np
import pandas as pd

file_path = "all_simulation_results.csv"

data = pd.read_csv(file_path)

# 删除 DutyValue 小于 0.1 的数据
filtered_data = data[data['DutyValue'] >= 0.1]

# 保存更新后的数据到原始文件
filtered_data.to_csv(file_path, index=False)





