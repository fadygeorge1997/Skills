import { test, expect } from "@chromatic-com/playwright";

test.describe("shadcn/ui Registry API", () => {
  test("Accordion component loads from registry", async ({ request }) => {
    const response = await request.get(
      "https://ui.shadcn.com/r/styles/new-york/accordion.json"
    );
    expect(response).toBeOK();

    const data = await response.json();
    expect(data.name).toBe("accordion");
    expect(data.files).toBeDefined();
    expect(data.files.length).toBeGreaterThan(0);
  });

  test("Login block loads from registry", async ({ request }) => {
    const response = await request.get(
      "https://ui.shadcn.com/r/styles/new-york/login-01.json"
    );
    expect(response).toBeOK();

    const data = await response.json();
    expect(data.name).toBeDefined();
    expect(data.files).toBeDefined();
  });
});
