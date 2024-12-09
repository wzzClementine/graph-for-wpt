
import networkx as nx
import matplotlib.pyplot as plt


class GraphModeling:
    def __init__(self, type, state, nodes, edges):
        self.type = type  # transmitter or receiver
        self.state = state  # switch state
        self.nodes = nodes  # circuit elements
        self.edges = edges

        self.circuit_graph = nx.DiGraph()

    def create_graph(self):
        for node, features in self.nodes:
            self.circuit_graph.add_node(node, **features)
        self.circuit_graph.add_edges_from(self.edges)
        # for node, data in self.circuit_graph.nodes(data=True):
        #     print(f"{node}: {data}")

    def plot_single_graph(self):
        # 定义布局
        pos = nx.spring_layout(self.circuit_graph, center=(0, 0), k=1.5, iterations=50, seed=11)

        # 调整边界使图居中显示
        x_values = [pos[node][0] for node in pos]
        y_values = [pos[node][1] for node in pos]
        x_margin, y_margin = 0.2, 0.2  # 设置边界留白
        plt.xlim(min(x_values) - x_margin, max(x_values) + x_margin)
        plt.ylim(min(y_values) - y_margin, max(y_values) + y_margin)

        # 绘制节点和边
        nx.draw(self.circuit_graph, pos, with_labels=False, node_size=800, node_color="lightblue")

        # 绘制节点标签，设置偏移以防重叠
        for node, (x, y) in pos.items():
            plt.text(
                x, y,
                f"{node}",
                fontsize=8,
                ha='center',
                va='center',  # 居中
                bbox=dict(facecolor='white', alpha=0.8, edgecolor='none')  # 设置背景框
            )

        plt.title(f"WPT System Circuit Graph ({self.type} with {self.state} ON)")
        plt.show()

    def plot_wpt_graph(self):
        layout = nx.spring_layout(self.circuit_graph, seed=145)
        # 绘制图
        fig, ax = plt.subplots(figsize=(15, 10))
        nx.draw(
            self.circuit_graph,
            layout,
            with_labels=False,
            node_size=2000,
            node_color="lightblue",
            arrowsize=20,
            ax=ax  # 使用 ax 指定子图
        )

        # 绘制节点标签
        # node_labels = {node: f"{node}\n{data.get('type', '')}" for node, data in self.circuit_graph.nodes(data=True)}
        nx.draw_networkx_labels(self.circuit_graph, layout,  font_size=15)

        # 绘制边标签（显示带属性的边）
        edge_labels = nx.get_edge_attributes(self.circuit_graph, 'type')
        nx.draw_networkx_edge_labels(self.circuit_graph, layout, edge_labels=edge_labels, font_size=18)

        # 设置标题并调整位置
        fig.suptitle(f"WPT System Circuit Graph ({self.state[0]} & {self.state[1]} ON)", fontsize=25, y=0.95)  # 使用 fig.suptitle 设置标题

        # 自动调整布局
        fig.tight_layout(rect=[0, 0, 1, 0.95])  # 确保标题不被裁剪
        plt.show()




