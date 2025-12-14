from playwright.sync_api import sync_playwright, expect

link = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(link)

    login_email_input = page.get_by_test_id('login-form-email-input').locator('input')
    expect(login_email_input).to_be_visible()

    login_password_input = page.get_by_test_id('login-form-email-input').locator('input')
    expect(login_password_input).to_be_visible()

    login_button = page.get_by_test_id('login-page-login-button')
    expect(login_button).to_be_visible()

    registration_link = page.get_by_test_id('login-page-registration-link')
    registration_link.click()

    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    expect(registration_email_input).to_be_visible()

    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    expect(registration_password_input).to_be_visible()

    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_visible()

    page.wait_for_timeout(3000)




"""
Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login
Проверить наличие элементов: "Email", "Password", "Login"
Нажать на ссылку "Registration", после чего произойдет редирект на страницу Registration
Проверить наличие элементов: "Email", "Password", "Registration"
"""