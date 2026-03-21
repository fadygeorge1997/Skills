const { request } = require('playwright');

async function getShadcnAuthApi() {
  const context = await request.newContext();

  try {
    const response = await context.get('https://ui.shadcn.com/r/styles/new-york/login-01.json');

    if (response.ok()) {
      const registryItem = await response.json();
      console.log("تجلت أسرار المكون:", registryItem.name);
      console.log(registryItem.files.map(f => f.path));
    } else {
      console.error(`❌ فشل. الحالة: ${response.status()}`);
    }
  } catch (error) {
    console.error("💥 خطأ:", error);
  } finally {
    await context.dispose();
  }
}

getShadcnAuthApi();
