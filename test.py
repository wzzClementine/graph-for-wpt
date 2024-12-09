
import numpy as np


def calculate_phase_shift(duty_cycle):
    """
    根据占空比计算移相角（弧度和角度）。

    Args:
        duty_cycle (float): 占空比 (0 < D < 1)

    Returns:
        phase_shift_rad (float): 移相角（弧度）
        phase_shift_deg (float): 移相角（角度）
    """
    if 0 < duty_cycle <= 1:
        phase_shift_rad = np.pi * duty_cycle
        phase_shift_deg = np.degrees(phase_shift_rad)
        return phase_shift_rad, phase_shift_deg
    else:
        raise ValueError("占空比应在 (0, 1) 之间")


# 示例: 占空比 0.6
duty_cycle = 0.6
phase_shift_rad, phase_shift_deg = calculate_phase_shift(duty_cycle)

print(f"占空比: {duty_cycle}")
print(f"移相角: {phase_shift_rad:.2f} 弧度, {phase_shift_deg:.2f} 度")
