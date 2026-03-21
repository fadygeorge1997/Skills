const { request } = require('playwright');

async function fetchCommunityComponent(component = 'multiple-selector') {
  const api = await request.newContext();

  try {
    const response = await api.get(`https://shadcn-community.com/r/styles/default/${component}.json`);

    if (response.ok()) {
      const data = await response.json();
      console.log("--- استحضار مكون المجتمع (Community Component) ---");
      console.log(`الاسم: ${data.name}`);
      console.log(`المؤلف/المصدر: ${data.type}`);

      if (data.dependencies) {
        console.log(`الارتباطات الخارجية: ${data.dependencies.join(', ')}`);
      }
    } else {
      console.error("❌ فشل الاتصال بالشبكة المجتمعية. الحالة:", response.status());
    }
  } catch (error) {
    console.error("💥 خطأ:", error);
  } finally {
    await api.dispose();
  }
}

const component = process.argv[2] || 'multiple-selector';
fetchCommunityComponent(component);
