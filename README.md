# Playwright QA Portfolio

Automated test suite in **Python + Playwright + pytest**, written by a QA engineer with a manual background (iGaming, FinTech/insurance). It covers UI flows, layout across resolutions and API checks, structured the way I'd structure a real project: Page Object Model, parametrized tests, markers, reports and CI.

Tests run against public sites built for practice, so nothing here comes from any employer's product:

- UI: [Sauce Demo](https://www.saucedemo.com) (online shop)
- API: [JSONPlaceholder](https://jsonplaceholder.typicode.com) (fake REST API)

## What is covered

| Area | File | Examples |
|---|---|---|
| Login | `tests/test_login.py` | valid login, wrong password, unknown/locked user, empty fields, access to a protected page without login, logout |
| Cart and checkout | `tests/test_cart_checkout.py` | cart badge, products in cart, full purchase, totals = items + tax, form validation, sorting |
| Responsiveness | `tests/test_responsive.py` | login and inventory pages at 375, 768, 1366 and 1920 px: key elements visible, no horizontal scroll |
| API | `tests/test_api.py` | GET/POST/PUT/DELETE, status codes, filtering, JSON structure, 404 handling |

## Structure

```
pages/          Page Objects (login, inventory, cart, checkout)
tests/          test modules grouped by area
conftest.py     shared fixtures (logged-in user, API client, base URLs)
pytest.ini      markers, screenshots and traces on failure
.github/        GitHub Actions workflow
```

## Design choices

- **Page Object Model**: selectors live in `pages/`, tests read like scenarios.
- **Fixtures** for login and the API client, so tests stay short and independent.
- **Parametrization** for validation cases instead of copy-pasted tests.
- **Markers** (`smoke`, `ui`, `api`, `responsive`) to run only a part of the suite.
- **Failure evidence**: screenshot and Playwright trace saved for every failed UI test.
- **Resilient locators** based on `data-test` attributes and roles, with web-first assertions (auto-waiting, no fixed sleeps).

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium

pytest                           # everything
pytest -m smoke                  # quick check of key flows
pytest -m api                    # API only
pytest --headed --slowmo 300     # watch the browser
pytest --browser firefox         # another browser (playwright install firefox)
pytest --html=report.html --self-contained-html
```

To inspect a failed run: `playwright show-trace test-results/<test-folder>/trace.zip`.

## CI

GitHub Actions runs the whole suite on every push and uploads the HTML report and traces as an artifact.

## Roadmap

- [ ] Visual regression checks for the responsive tests
- [ ] AI-agent assisted exploratory runs (Python) feeding new test ideas
- [ ] Parallel execution with `pytest-xdist`
