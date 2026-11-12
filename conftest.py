"""Shared fixtures for the test suite."""
import pytest
from playwright.sync_api import Playwright, APIRequestContext

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

# Public demo shop made for test practice: https://www.saucedemo.com
BASE_URL = "https://www.saucedemo.com"
API_URL = "https://jsonplaceholder.typicode.com"
PASSWORD = "secret_sauce"


@pytest.fixture(scope="session", autouse=True)
def _use_data_test_attribute(playwright: Playwright) -> None:
    # The demo shop marks elements with data-test, not Playwright's default data-testid.
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.fixture(scope="session")
def base_url() -> str:
    # Overrides the pytest-playwright option so page.goto("/") works.
    return BASE_URL


@pytest.fixture
def login_page(page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def inventory_page(page) -> InventoryPage:
    return InventoryPage(page)


@pytest.fixture
def cart_page(page) -> CartPage:
    return CartPage(page)


@pytest.fixture
def checkout_page(page) -> CheckoutPage:
    return CheckoutPage(page)


@pytest.fixture
def logged_in(login_page, inventory_page) -> InventoryPage:
    """Open the shop and log in as the standard user."""
    login_page.open()
    login_page.login("standard_user", PASSWORD)
    inventory_page.expect_loaded()
    return inventory_page


@pytest.fixture(scope="session")
def api(playwright: Playwright) -> APIRequestContext:
    context = playwright.request.new_context(base_url=API_URL)
    yield context
    context.dispose()
