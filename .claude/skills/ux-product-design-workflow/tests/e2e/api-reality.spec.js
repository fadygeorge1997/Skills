import { test, expect } from "@chromatic-com/playwright";

test.describe("JSONPlaceholder API", () => {
  test("Fetches post by ID", async ({ request }) => {
    const response = await request.get(
      "https://jsonplaceholder.typicode.com/posts/1"
    );
    expect(response).toBeOK();

    const data = await response.json();
    expect(data.userId).toBeTruthy();
    expect(data.id).toBe(1);
    expect(data.title).toBeDefined();
    expect(data.body).toBeDefined();
  });

  test("Returns 404 for nonexistent post", async ({ request }) => {
    const response = await request.get(
      "https://jsonplaceholder.typicode.com/posts/99999"
    );
    expect(response.status()).toBe(404);
  });
});
