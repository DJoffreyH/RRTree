# RR-Tree: A Cognitive Architecture for Reasoning as a Program

<p align="center">
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg" alt="Contributions Welcome"></a>
  <a href="https://github.com/DJoffreyH/RRTree/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
</p>

> **Compiling Consciousness: The RR-Tree and the Syntax of Machine Reasoning**

---

### **Abstract**

The pursuit of autonomous agents has been constrained by the limitations of linear (Chain-of-Thought) and unstructured exploratory (Tree-of-Thought) reasoning frameworks. This repository introduces the **Recursive Reasoning Tree (RR-Tree)**, a novel cognitive architecture that treats reasoning as a formal, self-modifying program. By representing thought as a computable S-expression tree and manipulating it with explicit meta-reasoning operators, this framework provides a path toward more robust, auditable, and dynamically adaptive AI agents.

---

### **🏛️ Core Principles**

The RR-Tree architecture is founded on three core ideas:

1.  **Thought as a Computable Structure:** We move beyond unstructured text by representing the entire reasoning process as a stateful **Recursive Reasoning Tree (RR-Tree)**, a Lisp-style S-expression. This makes cognition a formal data structure that can be systematically analyzed and manipulated.

2.  **Quantitative Guidance over Heuristics:** We replace simple heuristics with the **Thought-Quality-Resonance (TQR) Model**, a multi-dimensional evaluation function that scores each reasoning step based on its logical coherence, explanatory power, and structural elegance. *(中文暂定名: 思维洞见共鸣模型)*

3.  **Meta-Reasoning as Explicit Operations:** We define a minimal set of **Transformation Operators** (`CHOOSE`, `EXPAND`, `REWRITE`, `DEEP_DIVE`, etc.) that allow an agent to consciously and audibly manipulate its own cognitive process, making reasoning an explicit act of program execution.

---

### **⚙️ Architecture Overview**

The framework operates in a continuous **Evaluate-Transform** loop, analogous to the "Recognize-Act" cycle in classical cognitive architectures, but applied to an internal thought process.

```
+------------------------------------+
|         Current State              |
|        (RR-Tree Instance)          |
+-----------------|------------------+
                  | (Represents the agent's current understanding)
                  v
+------------------------------------+
|         EVALUATE (TQR Model)       |
|   - α: Explanatory Power           |
|   - β: Evidential Support          |
|   - γ: Structural Elegance         |
|   - C: Complexity                  |
+-----------------|------------------+
                  | (Generates a quantifiable score for each potential thought)
                  v
+------------------------------------+
|         TRANSFORM (Operators)      |
|   - CHOOSE, EXPAND, REWRITE,       |
|     MERGE, DEEP_DIVE, EVAL         |
+-----------------|------------------+
                  | (Applies a formal modification to the tree)
                  v
+------------------------------------+
|           New State                |
|      (Evolved RR-Tree)             |
+------------------------------------+
```

This loop continues until the tree converges on a solution that is logically sound and cannot be easily improved, as determined by the TQR scores.

---

### **🚀 Conceptual Usage**

While a reference implementation is under development, the theoretical workflow is illustrated in the following pseudo-code:

```python
from rrtree import RRTree, TQRModel, Agent

# 1. Define the initial problem as a structured S-expression
initial_problem = """
(root
  (goal "Determine optimal survival strategy for Civ-A detecting Civ-B.")
  (axioms
    (axiom (id "ax1") (name "Survival Imperative"))
    (axiom (id "ax2") (name "Zero-Sum Resource Game"))
    (axiom (id "ax3") (name "Chain of Suspicion"))
    (axiom (id "ax4") (name "Technological Explosion"))))
"""

# 2. Initialize the Agent with the RR-Tree architecture and TQR model
reasoning_agent = Agent(cognitive_architecture=RRTree, evaluation_model=TQRModel)

# 3. Load the problem and let the agent reason until convergence
final_tree, transformation_log = reasoning_agent.reason_until_convergence(initial_problem)

# 4. Inspect the results
print("✅ Reasoning converged!")
print("\n--- Final Conclusion ---")
print(final_tree.get_node("dark-forest-strike-proven").content)

print("\n--- Auditable Reasoning Log ---")
for transformation in transformation_log:
    print(transformation)
```

---

### **🎓 How to Cite**

If you find this work useful in your research, please consider citing the original paper:

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

### **🤝 Contributing**

Contributions to this project are welcome. This is a nascent field of research, and we are excited to collaborate with others. Please feel free to open an issue to discuss a new feature or bug, or submit a pull request with your proposed changes.

### **📜 License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.