
import numpy as np
import pandas as pd

file_path = "all_simulation_results.csv"

data = pd.read_csv(file_path)

# 增加一列 phase_shift_angle_deg，计算 phase_shift_angle 的角度值
data['phase_shift_angle_deg'] = np.degrees(data['phase_shift_angle'])

# 将 'phase_shift_angle_deg' 列移动到 'phase_shift_angle' 列的后面
columns = data.columns.tolist()
columns.insert(columns.index('phase_shift_angle') + 1, columns.pop(columns.index('phase_shift_angle_deg')))
data = data[columns]

# Save the modified data to a new file
data.to_csv(file_path, index=False)



