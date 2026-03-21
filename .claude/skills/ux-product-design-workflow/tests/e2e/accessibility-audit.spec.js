import { test, expect } from "@chromatic-com/playwright";

test.describe("Accessibility Audit", () => {
  test("Example page loads and has title", async ({ page }) => {
    await page.goto("https://example.com/");
    await expect(page).toHaveTitle(/Example Domain/);
  });

  test("Page has main heading", async ({ page }) => {
    await page.goto("https://example.com/");
    const heading = page.locator("h1");
    await expect(heading).toBeVisible();
  });
});
