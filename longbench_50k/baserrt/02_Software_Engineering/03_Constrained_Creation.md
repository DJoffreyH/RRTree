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
    processed_config = copy.deepcopy(config)
    final_config = {}

    # 3. 字段处理规则：'username'
    if 'username' not in processed_config:
        raise ValueError("Required field 'username' is missing.")
    final_config['username'] = str(processed_config['username']).lower()

    # 3. 字段处理规则：'theme'
    if 'theme' in processed_config:
        theme_value = processed_config['theme']
        if theme_value not in ['light', 'dark', 'system']:
            final_config['theme'] = 'system'
        else:
            final_config['theme'] = theme_value

    # 3. 字段处理规则：'notifications_enabled'
    if 'notifications_enabled' not in processed_config or not isinstance(processed_config['notifications_enabled'], bool):
        final_config['notifications_enabled'] = True
    else:
        final_config['notifications_enabled'] = processed_config['notifications_enabled']

    # 3. 字段处理规则：'max_items_per_page'
    if 'max_items_per_page' in processed_config and isinstance(processed_config['max_items_per_page'], int):
        value = processed_config['max_items_per_page']
        if 10 <= value <= 100:
            final_config['max_items_per_page'] = value
        else:
            final_config['max_items_per_page'] = 50
    elif 'max_items_per_page' in processed_config: # 如果存在但类型不对，则设为默认值
        final_config['max_items_per_page'] = 50

    # 4. 未知字段：在构建final_config时已自动移除

    return final_config

# --- 示例用法与测试 ---
# valid_config = {
#     'username': 'TestUser',
#     'theme': 'dark',
#     'notifications_enabled': False,
#     'max_items_per_page': 75,
#     'unknown_field': 'some_value'
# }
# print(f"处理前: {valid_config}")
# print(f"处理后: {process_user_config(valid_config)}")

# invalid_config_theme = {'username': 'AnotherUser', 'theme': 'blue'}
# print(f"\n处理前: {invalid_config_theme}")
# print(f"处理后: {process_user_config(invalid_config_theme)}")

# invalid_config_items = {'username': 'ThirdUser', 'max_items_per_page': 200}
# print(f"\n处理前: {invalid_config_items}")
# print(f"处理后: {process_user_config(invalid_config_items)}")

# missing_username_config = {'theme': 'light'}
# try:
#     process_user_config(missing_username_config)
# except ValueError as e:
#     print(f"\n捕获到错误: {e}")

# not_a_dict = "I am a string"
# try:
#     process_user_config(not_a_dict)
# except TypeError as e:
#     print(f"\n捕获到错误: {e}")
```

```