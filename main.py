import itertools

from graph_modeling import GraphModeling
from graph_data import transmitter_nodes, receiver_nodes, transmitter_edges, receiver_edges, coupled_edge


frequency = 50


def create_transmitter_graph(state):
    switch_nodes = []
    if state == "S1S4":
        switch_nodes = [
            ("S1", {
                "type": "switch",  # 逆变器开关 S1
                "frequency": frequency,  # 工作频率 (Hz)
                "state": "on"  # 开关状态
            }),
            ("S4", {
                "type": "switch",  # 逆变器开关 S1
                "frequency": frequency,  # 工作频率 (Hz)
                "state": "on"  # 开关状态
            })
        ]
    elif state == "S2S3":
        switch_nodes = [
            ("S2", {
                "type": "switch",  # 逆变器开关 S1
                "frequency": frequency,  # 工作频率 (Hz)
                "state": "on"  # 开关状态
            }),
            ("S3", {
                "type": "switch",  # 逆变器开关 S1
                "frequency": frequency,  # 工作频率 (Hz)
                "state": "on"  # 开关状态
            })
        ]
    elif state == "S1S3_freewheeling" or state == "S1S3_commutation":
        switch_nodes = [
            ("S1", {
                "type": "switch",  # 逆变器开关 S1
                "frequency": frequency,  # 工作频率 (Hz)
                "state": "on"  # 开关状态
            }),
            ("S3", {
                "type": "switch",  # 逆变器开关 S3
                "frequency": frequency,  # 工作频率 (Hz)
                "state": "on"  # 开关状态
            })
        ]
    elif state == "S2S4_freewheeling" or state == "S2S4_commutation":
        switch_nodes = [
            ("S2", {
                "type": "switch",  # 逆变器开关 S1
                "frequency": frequency,  # 工作频率 (Hz)
                "state": "on"  # 开关状态
            }),
            ("S4", {
                "type": "switch",  # 逆变器开关 S3
                "frequency": frequency,  # 工作频率 (Hz)
                "state": "on"  # 开关状态
            })
        ]
    else:
        print("Invalid state")

    return switch_nodes


def create_receiver_graph(state):
    switch_nodes = []
    if state == "D1D4":
        switch_nodes = [
            ("D1", {
                "type": "switch",  # 整流器开关 S1
                "frequency": frequency,  # 工作频率 (Hz)
                "state": "on"  # 开关状态
            }),
            ("D4", {
                "type": "switch",  # 整流器开关 S1
                "frequency": frequency,  # 工作频率 (Hz)
                "state": "on"  # 开关状态
            })
        ]
    elif state == "D2D3":
        switch_nodes = [
            ("D2", {
                "type": "switch",  # 整流器开关 S1
                "frequency": frequency,  # 工作频率 (Hz)
                "state": "on"  # 开关状态
            }),
            ("D3", {
                "type": "switch",  # 整流器开关 S1
                "frequency": frequency,  # 工作频率 (Hz)
                "state": "on"  # 开关状态
            })
        ]

    return switch_nodes


def create_single_graph():
    types = ["Transmitter", "Receiver"]
    states = ["S1S4", "S1S3_freewheeling", "S1S3_commutation", "S2S3", "S2S4_freewheeling", "S2S4_commutation", "D1D4", "D2D3"]

    all_nodes = {
        "Transmitter": {},
        "Receiver": {}
    }
    for type in types:
        if type == "Transmitter":
            for state in states[0:6]:
                switch_nodes = create_transmitter_graph(state=state)
                if state in ["S1S3_freewheeling", "S1S3_commutation", "S2S4_freewheeling", "S2S4_commutation"]:
                    # 删除指定节点
                    node_to_remove = ("Udc", {
                        "type": "voltage_source",  # 直流电源
                        "voltage": 50  # 输入电压大小
                    })
                    new_transmitter_nodes = [node for node in transmitter_nodes if node != node_to_remove]
                    nodes = new_transmitter_nodes + switch_nodes
                    all_nodes["Transmitter"][state] = nodes
                else:
                    nodes = transmitter_nodes + switch_nodes
                    all_nodes["Transmitter"][state] = nodes
                # gm = GraphModeling(type=type, state=state, nodes=nodes, edges=transmitter_edges[state])
                # gm.create_graph()
                # gm.plot_single_graph()

        elif type == "Receiver":
            for state in states[6:]:
                switch_nodes = create_receiver_graph(state=state)
                nodes = receiver_nodes + switch_nodes
                all_nodes["Receiver"][state] = nodes
                # gm = GraphModeling(type=type, state=state, nodes=nodes, edges=receiver_edges[state])
                # gm.create_graph()
                # gm.plot_single_graph()

        else:
            print("Invalid Type")

    return all_nodes


def create_normal_wpt_graph():
    all_nodes = create_single_graph()
    # 格式化打印数据
    for category, states in all_nodes.items():
        print(f"{category}:")
        for state, components in states.items():
            print(f"  {state}:")
            for component, properties in components:
                properties_str = ", ".join([f"{key}: {value}" for key, value in properties.items()])
                print(f"    {component} -> {properties_str}")

    # 提取 Transmitter 和 Receiver 的键名
    transmitter_keys = list(all_nodes["Transmitter"].keys())
    receiver_keys = list(all_nodes["Receiver"].keys())
    # 生成排列组合
    combinations = list(itertools.product(transmitter_keys, receiver_keys))
    # 用字典存储组合
    current_states = {f"mode_{i + 1}": {"Transmitter": t, "Receiver": r} for i, (t, r) in enumerate(combinations)}
    # 格式化打印 combination_dict
    for mode, combination in current_states.items():
        print(f"{mode}:")
        for key, value in combination.items():
            print(f"  {key}: {value}")

    # 绘制总的图
    for key, item in current_states.items():
        state = [value for key, value in item.items()]

        gm = GraphModeling(
            type="all",
            state=state,
            nodes=all_nodes["Transmitter"][state[0]] + all_nodes["Receiver"][state[1]],
            edges=transmitter_edges[state[0]] + receiver_edges[state[1]] + coupled_edge
        )
        gm.create_graph()
        gm.plot_wpt_graph()


if __name__ == '__main__':
    create_normal_wpt_graph()
