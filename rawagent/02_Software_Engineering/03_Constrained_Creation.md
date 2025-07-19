```python
import copy

def process_user_config(config: dict) -> dict:
    """
    Validates and cleans a user configuration dictionary based on a set of strict rules.

    Args:
        config: The input user configuration dictionary.

    Returns:
        A new, validated and cleaned dictionary.

    Raises:
        TypeError: If the input is not a dictionary.
        ValueError: If the required 'username' field is missing.
    """
    # 1. 输入验证：检查config是否为字典
    if not isinstance(config, dict):
        raise TypeError("Input 'config' must be a dictionary.")

    # 5. 返回值约束：创建一个新的字典副本，不修改原始输入
    # 我们通过只从原始字典中选择性地向新字典添加键值对来实现这一点
    final_config = {}

    # 3. 字段处理规则：'username'
    if 'username' not in config:
        raise ValueError("Required field 'username' is missing.")
    final_config['username'] = str(config['username']).lower()

    # 3. 字段处理规则：'theme'
    if 'theme' in config:
        theme_value = config['theme']
        if theme_value not in ['light', 'dark', 'system']:
            final_config['theme'] = 'system'
        else:
            final_config['theme'] = theme_value

    # 3. 字段处理规则：'notifications_enabled'
    if 'notifications_enabled' not in config or not isinstance(config['notifications_enabled'], bool):
        final_config['notifications_enabled'] = True
    else:
        final_config['notifications_enabled'] = config['notifications_enabled']

    # 3. 字段处理规则：'max_items_per_page'
    if 'max_items_per_page' in config and isinstance(config['max_items_per_page'], int):
        value = config['max_items_per_page']
        if 10 <= value <= 100:
            final_config['max_items_per_page'] = value
        else:
            final_config['max_items_per_page'] = 50
    elif 'max_items_per_page' in config: # 如果存在但类型不对，则设为默认值
        final_config['max_items_per_page'] = 50

    # 4. 未知字段：在构建final_config时已通过白名单的方式自动移除

    return final_config

```
