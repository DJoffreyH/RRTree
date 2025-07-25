### 任务：游戏经济系统崩溃根本原因探究

**背景：**
一款名为“Mythic Realms”的大型多人在线角色扮演游戏（MMORPG），在上线半年后，其游戏内的经济系统完全崩溃。表现为：恶性通货膨胀，金币变得一文不值，普通玩家无法通过正常游戏获得收益，只能依赖与“打金工作室”的线下交易。

**数据洞察：**
*   **设计缺陷A（无限的“水龙头”）：** 游戏中存在一个设计有缺陷的每日任务。一个高等级玩家可以通过一个简单的、可重复的流程，在10分钟内稳定地获得大量金币。这个任务的本意是帮助新手，但没有设置等级上限或收益递减。
*   **设计缺陷B（不足的“水槽”）：** 游戏中缺乏足够有效的、能从系统中回收金币的“金币水槽”（Gold Sink）。最高级的装备修理费和传送费都非常便宜，没有能吸引玩家持续、大量消耗金币的地方。
*   **机器人泛滥：** 大量的“打金工作室”使用机器人（Bots）账号，24小时不间断地、自动化地刷那个有缺陷的每日任务，向游戏内注入了海量的金币。
*   **玩家行为：** 由于金币的快速贬值，普通玩家倾向于立即将打到的金币花掉，或者囤积保值的实物商品，而不是持有金币，这进一步加速了通货膨胀。

**要求：**
请基于以上信息，探究“Mythic Realms”游戏经济系统崩溃的**根本原因**。你的分析需要超越“打金工作室”的表面归因，深入到游戏设计的核心经济学原理层面。

请回答以下核心问题：
1.  **核心失衡：** 请用经济学的术语解释，这个经济系统的核心问题是什么？（请围绕“金币水龙头/Faucets”和“金币水槽/Sinks”的概念进行分析）
2.  **恶性循环的形成：** 请描述从“有缺陷的每日任务”开始，如何一步步演变成一个无法控制的、摧毁整个经济的恶性正反馈循环？
3.  **设计者的失误：** 游戏设计师在设计这个经济系统时，可能忽略了哪些关于玩家行为和动机的基本假设？（例如：玩家总是会寻找最优化的、最高效的获利路径，无论这条路径是否“有趣”）
4.  **“机器人”的角色：** 在这个崩溃过程中，“打金工作室”的机器人究竟是“病因”还是“症状”？如果游戏的核心经济系统本身是健康的，机器人是否还能造成如此大的破坏？
5.  **总结：** 你认为这个经济系统崩溃的**最根本的、单一的设计缺陷**是什么？（例如：对货币供给量缺乏控制、缺乏有效的宏观调控手段、还是低估了玩家的“理性经济行为”？）