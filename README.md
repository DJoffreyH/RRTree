# RR-Tree: A Cognitive Architecture for Reasoning as a Program

<p align="center">
  <a href="CONTRIBUTING.md" target="_blank"><img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg" alt="Contributions Welcome"></a>
</p>

> **Compiling Consciousness: The RR-Tree and the Syntax of Machine Reasoning**

---

This repository contains the research and (eventual) implementation of the **Recursive Reasoning Tree (RR-Tree)**, a novel cognitive architecture for autonomous AI agents that treats reasoning as a formal, self-modifying program.

## 🎯 Abstract

The pursuit of autonomous agents has been constrained by the limitations of linear (Chain-of-Thought) and unstructured exploratory (Tree-of-Thought) reasoning frameworks. This paper argues for a new paradigm: treating reasoning as a formal, self-modifying program. We introduce a cognitive architecture built upon three core ideas:

1.  **🧠 The Recursive Reasoning Tree (RR-Tree)**: A stateful S-expression tree that represents thought as a computable data structure, moving beyond unstructured text.

2.  **🧭 The Thought-Quality-Resonance (TQR) Model**: A multi-dimensional evaluation function that assesses the logical alignment, novelty, and complexity of each reasoning step, replacing simple heuristics with rigorous, quantitative guidance. (中文暂定名: **神韵共振模型**)

3.  **🛠️ Explicit Transformation Operators**: A set of primitives for meta-reasoning (`CHOOSE`, `EXPAND`, `REWRITE`, `DEEP_DIVE`) that allow an agent to systematically and audibly manipulate its own cognitive process.

Together, these components create a framework that enhances robustness, provides radical explainability, and enables the recursive decomposition of complex problems, laying the foundation for a new class of auditable and dynamic AI agents.

## 🏛️ Core Architecture

The RR-Tree framework operates in a continuous "Evaluate-Transform" loop, which is analogous to the "Recognize-Act" cycle in classical cognitive architectures.

```
+------------------------------------+
|         Current State              |
|        (RR-Tree Instance)          |
+-----------------|------------------+
                  | (Represents the agent's current understanding)
                  v
+------------------------------------+
|         EVALUATE                   |
| (Using the TQR Model)              |
|   - α: Alignment                   |
|   - β: Quality & Insight           |
|   - C: Complexity                  |
+-----------------|------------------+
                  | (Generates a quantifiable score for each potential thought)
                  v
+------------------------------------+
|         TRANSFORM                  |
| (Executing a chosen operator)      |
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

## 🚀 Getting Started (Conceptual)

While the reference implementation is under development, the theoretical workflow is as follows:


## 💻 Usage (Pseudo-code)

Here is a Python-esque pseudo-code snippet illustrating how the RR-Tree framework might be used in practice:

```python
from rrtree import RRTree, TQRModel, Agent

# 1. Define the initial problem as a structured S-expression
initial_axioms = """
(root
  (goal "Determine optimal survival strategy for Civ-A detecting Civ-B.")
  (axioms
    (axiom (id "ax1") (name "Survival Imperative") ...)
    (axiom (id "ax2") (name "Zero-Sum Resource Game") ...)
    (axiom (id "ax3") (name "Chain of Suspicion") ...)
    (axiom (id "ax4") (name "Technological Explosion") ...)))
"""

# 2. Initialize the Agent with the RR-Tree and TQR model
reasoning_agent = Agent(cognitive_architecture=RRTree, evaluation_model=TQRModel)

# 3. Load the problem and let the agent reason until convergence
final_tree, transformation_log = reasoning_agent.reason_until_convergence(initial_axioms)

# 4. Inspect the results
print("✅ Reasoning converged!")
print("\n--- Final Conclusion ---")
print(final_tree.get_node("dark-forest-strike-proven").content)

print("\n--- Auditable Reasoning Log ---")
for transformation in transformation_log:
    print(transformation)
```

## 🎓 How to Cite

If you find this work useful in your research, please consider citing the original paper:

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

## 🤝 Contributing

Contributions to this project are welcome! This is a nascent field of research, and we are excited to collaborate with others.

Please feel free to open an issue to discuss a new feature or bug, or submit a pull request with your proposed changes.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
