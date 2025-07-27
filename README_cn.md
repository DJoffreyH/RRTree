# RR-Tree: 一种将推理视为程序的认知架构

<p align="center">
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg" alt="Contributions Welcome"></a>
  <a href="https://github.com/DJoffreyH/RRTree/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
</p>

> **编译意识：RR-Tree与机器推理的语法**

---

### **摘要**

自主Agent的发展一直受到线性（思维链 Chain-of-Thought）和非结构化探索性（思维树 Tree-of-Thought）推理框架的限制。本仓库介绍一种名为**递归推理树 (Recursive Reasoning Tree, RR-Tree)** 的新颖认知架构，它将推理视为一种形式化的、自修改的程序。通过将思想表示为可计算的S-表达式树，并使用显式的元推理操作符对其进行操作，本框架为实现更鲁棒、可审计和动态自适应的AI Agent提供了一条路径。

---

### **📊 性能 (理论目标)**

RR-Tree架构旨在对需要复杂、多步骤推理以及对模糊性或有缺陷前提具有鲁棒性的基准测试中，展现出卓越的性能。下表概述了其与现有范式相比的理论目标性能。

| 基准测试 | 指标 | 主流LLM (基线) | RR-Tree (目标) | 改进原理 |
| :--- | :--- | :--- | :--- | :--- |
| **ARC-AGI** | 准确率 | ~35-50% | **> 75%** | 将新颖问题分解为逻辑原语，而非依赖模式匹配。 |
| **ARC-AGI-2** | 准确率 | (尚未评测) | **> 60%** | TQR模型优先选择优雅/简洁的解决方案，与ARC的核心原则一致。 |
| **HLE** | 准确率 (鲁棒性) | ~70-85% | **> 95%** | PAP机制能显式处理歧义、缺失数据和逻辑冲突。 |
| **MMLU-Bench** | 准确率 (知识) | ~80-90% | **> 99.5%** | `Law-Alpha-Veto`协议防止模型产生幻觉，强制进行可验证的推理或诚实地承认无知。 |
| **SWE-Bench** | 通过率 (代码生成) | **97.03%** | `Law-Alpha-Veto`协议防止模型产生幻觉，强制进行可验证的推理或诚实地承认无知。 |

*注意: 基线分数是截至2025年初技术水平的近似值。RR-Tree的目标是理论值，有待实现后验证。*

---

### **🏛️ 核心原则**

RR-Tree架构建立在三个核心理念之上：

1.  **思想作为可计算结构:** 我们通过将整个推理过程表示为一个有状态的**递归推理树 (RR-Tree)**（一种Lisp风格的S-表达式），从而超越了非结构化文本的限制。这使得认知过程成为一个可以被系统性分析和操作的形式化数据结构。

2.  **量化指导优于启发式:** 我们用**思维洞见共鸣 (TQR) 模型**取代了简单的启发式方法。这是一个多维评估函数，它根据每个推理步骤的逻辑一致性、解释力、以及结构优雅性对其进行评分。

3.  **元推理作为显式操作:** 我们定义了一组最小的**变换操作符**（如 `CHOOSE`, `EXPAND`, `REWRITE`, `DEEP_DIVE` 等），允许一个Agent有意识地、可审计地操纵其自身的认知过程，使推理成为一种显式的程序执行行为。

---

### **⚙️ 架构概览**

本框架在一个持续的 **评估-变换** 循环中运作，这类似于经典认知架构中的“识别-行动”循环，但它被应用于内部的思维过程。

```
+------------------------------------+
|         当前状态                   |
|        (RR-Tree 实例)              |
+-----------------|------------------+
                  | (代表Agent当前的理解)
                  v
+------------------------------------+
|         评估 (TQR 模型)            |
|   - α: 解释力                      |
|   - β: 证据支持                    |
|   - γ: 结构优雅性                  |
|   - C: 复杂度                      |
+-----------------|------------------+
                  | (为每个潜在思想生成可量化的分数)
                  v
+------------------------------------+
|         变换 (操作符)              |
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

这个循环会持续进行，直到树收敛到一个由TQR分数决定的、逻辑上健全且无法轻易改进的解。

---

### **🚀 概念性用法**

虽然参考实现尚在开发中，但其理论工作流程可通过以下伪代码来展示：

```python
from rrtree import RRTree, TQRModel, Agent

# 1. 将初始问题定义为结构化的S-表达式
initial_problem = """ 
(root
  (goal "确定文明A在探测到文明B后的最优生存策略。")
  (axioms
    (axiom (id "ax1") (name "生存是文明的第一需要"))
    (axiom (id "ax2") (name "资源零和博弈"))
    (axiom (id "ax3") (name "猜疑链"))
    (axiom (id "ax4") (name "技术爆炸"))))
"""

# 2. 使用RR-Tree架构和TQR模型初始化Agent
reasoning_agent = Agent(cognitive_architecture=RRTree, evaluation_model=TQRModel)

# 3. 加载问题并让Agent推理直至收敛
final_tree, transformation_log = reasoning_agent.reason_until_convergence(initial_problem)

# 4. 审视结果
print("✅ 推理已收敛！")
print("\n--- 最终结论 ---")
print(final_tree.get_node("dark-forest-strike-proven").content)

print("\n--- 可审计的推理日志 ---")
for transformation in transformation_log:
    print(transformation)
```

---

### **🎓 如何引用**

如果您认为这项工作对您的研究有帮助，请考虑引用我们的原始论文：

```bibtex
@misc{huang2025compiling,
    title   = {Compiling Consciousness: The RR-Tree and the Syntax of Machine Reasoning},
    author  = {YC Huang},
    year    = {2025},
    howpublished = {https://github.com/DJoffreyH/RRTree},
    archivePrefix = {arXiv},
    primaryClass = {cs.AI}
}
```

---

### **🤝 贡献**

我们欢迎对本项目的任何贡献。这是一个新兴的研究领域，我们非常期待与各界同仁合作。请随时通过创建Issue来讨论新功能或报告错误，或通过Pull Request来提交您的修改建议。

### **📜 许可证**

本项目采用MIT许可证。详情请参阅 [LICENSE](LICENSE) 文件。
