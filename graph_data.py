
# 元器件节点定义
transmitter_nodes = [
    ("Udc", {
        "type": "voltage_source",  # 直流电源
        "voltage": 50  # 输入电压大小
    }),
    ("Cp", {
        "type": "tx_capacitor",  # 谐振网络电容 Cp
        "capacitance": 3.5059e-08,  # 电容值 (F)
        "resistance": 0.0001  # 内阻值 (Ohm)
    }),
    ("Lp", {
        "type": "tx_inductor",  # 谐振网络电感 Lp
        "inductance": 1.0e-4,  # 自感值 (H)
        "resistance": 0.1  # 内阻值 (Ohm)
    })
]

receiver_nodes = [
    ("Cs", {
        "type": "rx_capacitor",  # 谐振网络电容 Cs
        "capacitance": 3.5059e-08,  # 电容值 (F)
        "resistance": 0.0001  # 内阻值 (Ohm)
    }),
    ("Ls", {
        "type": "rx_inductor",  # 谐振网络电感 Ls
        "inductance": 1.0e-4,  # 自感值 (H)
        "resistance": 0.1  # 内阻值 (Ohm)
    }),
    ("RL", {
        "type": "load",  # 负载电阻 RL
        "resistance": 30  # 内阻值 (Ohm)
    }),
]

# 添加边（定义节点连接关系）
transmitter_edges = {
    "S1S4": [
        ("Udc", "S1", {"type": "dc", "current": 0.0}),
        ("S1", "Cp", {"type": "ac", "current": 0.0}),
        ("Cp", "Lp", {"type": "ac", "current": 0.0}),
        ("Lp", "S4", {"type": "ac", "current": 0.0}),
        ("S4", "Udc", {"type": "dc", "current": 0.0})
    ],
    "S1S3_freewheeling": [
        ("S1", "Cp", {"type": "ac", "current": 0.0}),
        ("Cp", "Lp", {"type": "ac", "current": 0.0}),
        ("Lp", "S3", {"type": "ac", "current": 0.0}),
        ("S3", "S1", {"type": "ac", "current": 0.0}),
    ],
    "S1S3_commutation": [
        ("S3", "Lp", {"type": "ac", "current": 0.0}),
        ("Lp", "Cp", {"type": "ac", "current": 0.0}),
        ("Cp", "S1", {"type": "ac", "current": 0.0}),
        ("S1", "S3", {"type": "ac", "current": 0.0}),
    ],
    "S2S3": [
        ("Udc", "S3", {"type": "dc", "current": 0.0}),
        ("S3", "Lp", {"type": "ac", "current": 0.0}),
        ("Lp", "Cp", {"type": "ac", "current": 0.0}),
        ("Cp", "S2", {"type": "ac", "current": 0.0}),
        ("S2", "Udc", {"type": "dc", "current": 0.0})
    ],
    "S2S4_freewheeling": [
        ("S2", "S4", {"type": "ac", "current": 0.0}),
        ("S4", "Lp", {"type": "ac", "current": 0.0}),
        ("Lp", "Cp", {"type": "ac", "current": 0.0}),
        ("Cp", "S2", {"type": "ac", "current": 0.0})
    ],
    "S2S4_commutation": [
        ("S4", "S2", {"type": "ac", "current": 0.0}),
        ("S2", "Cp", {"type": "ac", "current": 0.0}),
        ("Cp", "Lp", {"type": "ac", "current": 0.0}),
        ("Lp", "S4", {"type": "ac", "current": 0.0})
    ],
}

receiver_edges = {
    "D1D4": [
        ("Ls", "Cs", {"type": "ac", "current": 0.0}),
        ("Cs", "D1", {"type": "ac", "current": 0.0}),
        ("D1", "RL", {"type": "dc", "current": 0.0}),
        ("RL", "D4", {"type": "dc", "current": 0.0}),
        ("D4", "Ls", {"type": "ac", "current": 0.0})
    ],
    "D2D3": [
        ("Ls", "D3", {"type": "ac", "current": 0.0}),
        ("D3", "RL", {"type": "ac", "current": 0.0}),
        ("RL", "D2", {"type": "dc", "current": 0.0}),
        ("D2", "Cs", {"type": "dc", "current": 0.0}),
        ("Cs", "Ls", {"type": "ac", "current": 0.0})
    ]
}

coupled_edge = [
    ("Lp", "Ls", {
        "type": "coupler",  # 耦合系数
        "coupling_coefficient": 0.11,
        "mutual_inductance": 2.0e-5
    })
]


