const { request } = require('playwright');

async function fetchApiReality() {
  const apiContext = await request.newContext({
    baseURL: 'https://jsonplaceholder.typicode.com',
    extraHTTPHeaders: {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      // 'Authorization': 'Bearer YOUR_TOKEN'
    }
  });

  try {
    console.log("--- بداية عملية الاستحضار (Initiating Request) ---");

    const response = await apiContext.get('/posts/1');

    if (response.ok()) {
      const data = await response.json();

      console.log("✅ تمت الاستجابة بنجاح (The Absolute Responded)");
      console.log("📦 جوهر البيانات المستلمة:");
      console.dir(data, { depth: null, colors: true });

      if (data.userId) {
        console.log(`\nتم التعرف على الكيان: User ID ${data.userId}`);
      }
    } else {
      console.error(`❌ فشل في جلب الحقيقة. الحالة: ${response.status()}`);
      const errorBody = await response.text();
      console.error(`سبب التفكك: ${errorBody}`);
    }
  } catch (error) {
    console.error("💥 حدث تمزق في نسيج الطلب:", error);
  } finally {
    await apiContext.dispose();
    console.log("\n--- تم إغلاق السياق والعودة للفراغ (Context Disposed) ---");
  }
}

fetchApiReality();
