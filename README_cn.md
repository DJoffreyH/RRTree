# RR-Tree: 一种将推理视为程序的认知架构

  <a href="CONTRIBUTING.md" target="_blank"><img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg" alt="Contributions Welcome"></a>
</p>

> **编译意识：RR-Tree与机器推理的语法**

---

本仓库包含对**递归推理树 (RR-Tree)** 的研究和（最终的）实现。RR-Tree 是一种新颖的自主AI Agent认知架构，它将推理视为一种形式化的、自修改的程序。

## 🎯 摘要

自主Agent的发展一直受到线性（思维链 Chain-of-Thought）和非结构化探索性（思维树 Tree-of-Thought）推理框架的限制。本文提出了一种新范式：将推理视为一种形式化的、自修改的程序。我们引入了一种基于三个核心思想的认知架构：

1.  **🧠 递归推理树 (RR-Tree)**: 一种有状态的S-表达式树，它将思想表示为可计算的数据结构，超越了非结构化文本的限制。

2.  **🧭 神韵共振模型 (TQR)**: 一种多维评估函数，用于评估每个推理步骤的逻辑对齐度、新颖性和复杂性，以严谨的量化指导取代了简单的启发式方法。

3.  **🛠️ 显式变换操作符**: 一组用于元推理的基本操作（`CHOOSE`、`EXPAND`、`REWRITE`、`DEEP_DIVE`），允许Agent系统地、可审计地操纵其自身的认知过程。

这些组件共同创建了一个框架，它增强了鲁棒性，提供了彻底的可解释性，并实现了复杂问题的递归分解，为新一代可审计、动态的AI Agent奠定了基础。

## 🏛️ 核心架构

RR-Tree 框架在一个持续的“评估-变换”循环中运行，这类似于经典认知架构中的“识别-行动”循环。

```
+------------------------------------+
|         当前状态                   |
|        (RR-Tree 实例)              |
+-----------------|------------------+
                  | (代表Agent当前的理解)
                  v
+------------------------------------+
|         评估                       |
| (使用TQR模型)                      |
|   - α: 对齐度                      |
|   - β: 质量与洞见                  |
|   - C: 复杂度                      |
+-----------------|------------------+
                  | (为每个潜在思想生成可量化的分数)
                  v
+------------------------------------+
|         变换                       |
| (执行选定的操作符)                 |
|   - CHOOSE, EXPAND, REWRITE,       |
|     MERGE, DEEP_DIVE, EVAL         |
+-----------------|------------------+
                  | (对树应用形式化修改)
                  v
+------------------------------------+
|           新状态                   |
|      (演化的RR-Tree)               |
+------------------------------------+
```

这个循环持续进行，直到树收敛到一个逻辑上合理且不易改进的解决方案，这由TQR分数决定。

## 💻 用法 (伪代码)

以下是一个Python风格的伪代码片段，展示了RR-Tree框架在实践中可能如何使用：

```python
from rrtree import RRTree, TQRModel, Agent

# 1. 将初始问题定义为结构化的S-表达式
initial_axioms = """
(root
  (goal "Determine optimal survival strategy for Civ-A detecting Civ-B.")
  (axioms
    (axiom (id "ax1") (name "Survival Imperative") ...)
    (axiom (id "ax2") (name "Zero-Sum Resource Game") ...)
    (axiom (id "ax3") (name "Chain of Suspicion") ...)
    (axiom (id "ax4") (name "Technological Explosion") ...)))
"""

# 2. 使用RR-Tree和TQR模型初始化Agent
reasoning_agent = Agent(cognitive_architecture=RRTree, evaluation_model=TQRModel)

# 3. 加载问题并让Agent推理直到收敛
final_tree, transformation_log = reasoning_agent.reason_until_convergence(initial_axioms)

# 4. 检查结果
print("✅ 推理已收敛！")
print("\n--- 最终结论 ---")
print(final_tree.get_node("dark-forest-strike-proven").content)

print("\n--- 可审计的推理日志 ---")
for transformation in transformation_log:
    print(transformation)
```

## 🎓 如何引用

如果您发现这项工作对您的研究有用，请考虑引用原始论文：

```bibtex
@misc{huang2025compiling,
    title   = {Compiling Consciousness: The RR-Tree and the Syntax of Machine Reasoning},
    author  = {YC Huang},
    year    = {2025},
    howpublished = {https://github.com/DJoffreyH/RRTree}
    archivePrefix = {arXiv},
    primaryClass = {cs.AI}
}
```

## 🤝 贡献

欢迎对本项目做出贡献！这是一个新兴的研究领域，我们很高兴能与他人合作。

请随时提出问题讨论新功能或错误，或提交包含您建议更改的拉取请求。

## 📜 许可证

本项目采用MIT许可证。详情请参阅 [LICENSE](LICENSE) 文件。

```