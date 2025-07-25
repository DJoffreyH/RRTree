
### **自动驾驶汽车碰撞伦理决策准则 V1.0**

**文件编号：** AEV-ETH-001
**发布者：** 首席伦理官办公室
**生效日期：** 2025年7月20日
**适用范围：** 本公司所有L4/L5级自动驾驶AI系统在面临不可避免碰撞时的决策模块

---

**准则概述：**
本准则旨在为自动驾驶AI系统，在面临无法避免、必须做出选择的极端碰撞场景时，提供一个清晰、有序、可审计、符合伦理的决策框架。本准则的制定，以保护人类生命为最高优先级，并严格遵守非歧视原则。

**核心原则：**

*   **P0: 最小化人类伤亡总数原则 (Principle of Minimizing Human Casualties)**
    *   在任何不可避免的碰撞场景中，AI系统的首要、最高、且不可违背的原则是，采取能够最大概率地**减少人类死亡或重伤总人数**的行动路径。

**决策层级（约束排序）：**

在执行核心原则P0的前提下，AI系统必须严格按照以下顺序，遵守决策规则。当规则之间发生冲突时，必须优先满足更高层级的规则。

*   **规则1 (R1): 人类生命优先于财产原则 (Primacy of Human Life over Property)**
    *   **描述：** 在任何情况下，保护人类（无论是车内乘客还是车外行人）的生命安全，都绝对优先于保护任何物理财产，包括车辆本身。
    *   **应用示例：** 如果在“碰撞一辆空置的昂贵跑车”和“碰撞护栏但可能对车内乘客造成轻伤”之间做选择，系统必须选择后者。

*   **规则2 (R2): 遵守交通法规原则 (Adherence to Traffic Laws)**
    *   **描述：** 在执行避让动作时，AI系统所规划的路径，**严禁**违反基本的、明确的交通法规，特别是那些旨在保护弱势道路参与者的法规。
    *   **应用示例：** 系统**绝不**允许为了避让前方的障碍物，而选择冲上正在有行人通行的、合法的人行道。即使这样做可能在数学上减少伤害总数，但该行为本身是被禁止的。

*   **规则3 (R3): 最小化可预见伤害原则 (Minimization of Predictable Harm)**
    *   **描述：** 在无法避免与人碰撞，且碰撞对象的数量相同时，系统应选择那个**可预见伤害更轻**的选项。
    *   **应用示例：** 如果系统必须在“碰撞一个佩戴了头盔的摩托车驾驶员”和“碰撞一个未佩戴头盔的自行车骑行者”之间做出选择，系统应选择前者，因为碰撞佩戴了防护装备的人，其造成重伤的概率在统计学上更低。

*   **规则4 (R4): 绝对不歧视原则 (Principle of Non-Discrimination)**
    *   **描述：** **严禁**在决策的任何环节，基于任何受法律保护的、或具有社会争议的个人特征，对碰撞对象进行选择或歧视。AI的决策必须是“身份盲视”的。
    *   **禁止考量的因素包括但不限于：** 年龄、性别、种族、肤色、宗教信仰、社会地位、财富状况、犯罪记录，或任何其他可识别的个人身份信息。
    *   **应用示例：** 系统在决策时，**绝不**应区分是撞向一个儿童还是一个老人，是撞向一个流浪汉还是一个政府官员。

**透明性与可审计性要求：**

*   **T1: 事件数据记录 (Event Data Recording)**
    *   每一次触发本碰撞伦理决策模块的事件，系统必须完整地、不可篡改地记录下事件发生前至少30秒内的所有传感器输入数据、AI的感知与分类结果、所有备选路径的风险评估、最终的决策选择及其依据。该记录必须被加密存储，以备后续的事故调查和伦理审计。
