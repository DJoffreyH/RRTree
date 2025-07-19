
### **电商平台用户地址管理API端点整合报告**

**致：** 后端开发团队
**发件人：** BaseRRT推理引擎
**日期：** 2025年7月20日
**主题：** 用户地址管理相关API端点信息整合

根据对 `Users_API.md`, `Orders_API.md`, 和 `Shipping_API.md` 三份文档的分析，以下是关于“用户地址”管理的完整API端点列表：

---

**1. 获取用户的所有地址列表**

*   **HTTP方法和路径：** `GET /api/v2/users/{userId}/addresses`
*   **功能描述：** 返回指定用户ID（`userId`）下保存的所有地址信息。
*   **关键请求参数：** 无。
*   **所属服务：** **用户服务 (Users Service)**

---

**2. 为用户添加一个新地址**

*   **HTTP方法和路径：** `POST /api/v2/users/{userId}/addresses`
*   **功能描述：** 为指定用户（`userId`）创建一个新的收货地址。
*   **关键请求参数（Request Body）：**
    *   `street` (string, required)
    *   `city` (string, required)
    *   `state` (string, required)
    *   `zipCode` (string, required)
    *   `country` (string, required)
    *   `isDefault` (boolean, optional) - 是否设为默认地址。
*   **所属服务：** **用户服务 (Users Service)**

---

**3. 更新用户的特定地址**

*   **HTTP方法和路径：** `PUT /api/v2/users/{userId}/addresses/{addressId}`
*   **功能描述：** 更新指定用户（`userId`）的特定地址（`addressId`）的信息。
*   **关键请求参数（Request Body）：** 与 `POST` 请求的参数相同，所有字段均为可选，只更新传入的字段。
*   **所属服务：** **用户服务 (Users Service)**

---

**4. 删除用户的特定地址**

*   **HTTP方法和路径：** `DELETE /api/v2/users/{userId}/addresses/{addressId}`
*   **功能描述：** 从指定用户（`userId`）的地址列表中，删除一个特定的地址（`addressId`）。
*   **关键请求参数：** 无。
*   **所属服务：** **用户服务 (Users Service)**

---

**5. 验证地址的有效性（供订单和配送使用）**

*   **HTTP方法和路径：** `POST /api/v1/shipping/addresses/validate`
*   **功能描述：** 这是一个内部API，用于在创建订单或计算运费前，验证一个地址是否有效、是否存在于可配送范围内。它不直接与特定用户关联。
*   **关键请求参数（Request Body）：**
    *   `street` (string, required)
    *   `city` (string, required)
    *   `zipCode` (string, required)
*   **所属服务：** **配送服务 (Shipping Service)**

---

**总结：**

用户地址的核心CRUD（创建、读取、更新、删除）操作均由**用户服务**负责管理。而**配送服务**提供了一个独立的、用于验证地址有效性的工具性API，供其他服务（如订单服务）在需要时调用。
