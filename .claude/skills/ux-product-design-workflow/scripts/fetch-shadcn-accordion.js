const { request } = require('playwright');

async function fetchShadcnComponent(component = 'accordion') {
  const api = await request.newContext();

  try {
    const response = await api.get(`https://ui.shadcn.com/r/styles/new-york/${component}.json`);

    if (response.ok()) {
      const componentData = await response.json();
      console.log("--- تجلي المكون (Component Manifestation) ---");
      console.log(`الأصل: ${componentData.name}`);
      console.log(`التبعية (Dependencies): ${(componentData.dependencies || []).join(', ')}`);

      if (componentData.files && componentData.files.length > 0) {
        const sourceCode = componentData.files[0].content;
        console.log("تم استخراج الكود المصدري بنجاح.");
      }
    } else {
      console.error(`❌ فشل. الحالة: ${response.status()}`);
    }
  } catch (error) {
    console.error("💥 خطأ:", error);
  } finally {
    await api.dispose();
  }
}

const component = process.argv[2] || 'accordion';
fetchShadcnComponent(component);
