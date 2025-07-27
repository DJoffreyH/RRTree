### **电商平台用户地址管理API端点整合报告**

**致：** 后端开发团队
**发件人：** AI分析引擎
**日期：** 2025年7月20日
**主题：** 用户地址管理相关API端点信息整合

根据对 `Users_API.md`, `Orders_API.md`, 和 `Shipping_API.md` 三份文档的分析，以下是关于“用户地址”管理的完整API端点列表，及其在服务间的交互关系：

---

**1. 核心CRUD服务：用户服务 (Users Service)**

用户地址的生命周期管理，完全由用户服务负责。

*   **`GET /api/v2/users/{userId}/addresses`**
    *   **功能描述：** 返回指定用户ID下保存的所有地址信息。
*   **`POST /api/v2/users/{userId}/addresses`**
    *   **功能描述：** 为指定用户创建一个新的收货地址。
    *   **关键请求参数：** `street`, `city`, `state`, `zipCode`, `country`, `isDefault` (optional)。
*   **`PUT /api/v2/users/{userId}/addresses/{addressId}`**
    *   **功能描述：** 更新指定用户的特定地址信息。
*   **`DELETE /api/v2/users/{userId}/addresses/{addressId}`**
    *   **功能描述：** 删除一个特定的地址。

---

**2. 工具性验证服务：配送服务 (Shipping Service)**

配送服务提供了一个独立的、用于验证地址有效性的工具性API。

*   **`POST /api/v1/shipping/addresses/validate`**
    *   **功能描述：** 验证一个地址是否有效、是否存在于可配送范围内。此API不与特定用户关联，供其他服务调用。
    *   **关键请求参数：** `street`, `city`, `zipCode`。

---

**3. 服务间交互：订单服务 (Orders Service)**

订单服务在创建订单时，会作为客户端，调用上述两个服务。

*   **交互流程:** 当收到一个创建订单的请求（`POST /api/v1/orders`）时，订单服务会：
    1.  从请求中获取 `shippingAddressId`。
    2.  调用**用户服务**的 `GET .../{addressId}` 接口，获取地址详情。
    3.  调用**配送服务**的 `validate` 接口，确认该地址是否可达。
    4.  只有当两个调用都成功后，订单才能被创建。

**总结：**

此架构体现了良好的微服务设计原则：**用户服务**作为地址数据的“权威来源”（Source of Truth），负责其核心管理；**配送服务**则提供了一个解耦的、可重用的验证功能；而**订单服务**则作为协调者，编排这些服务以完成更复杂的业务流程。
