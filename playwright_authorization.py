from playwright.sync_api import sync_playwright, expect # Импорт Playwright для синхронного режима и проверки

link = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(link)

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    password_input = page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill("password")

    login_button = page.get_by_test_id('login-page-login-button')
    login_button.click()

    wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text('Wrong email or password')

    page.wait_for_timeout(5000)



"""
Необходимо написать скрипт, который откроет страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login
Заполнит поле "Email" значением user.name@gmail.com
Заполнит поле "Password" значением password
Нажмет на кнопку "Login"
Проверит наличие алерта с текстом "Wrong email or password"

Terminal command: python -m playwright_authorization


# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу авторизации
    page.goto(link)

    # Находим поле "Email" и заполняем его
    email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    email_input.fill("user.name@gmail.com")

    # Находим поле "Password" и заполняем его
    password_input = page.locator('//div[@data-testid="login-form-password-input"]//div//input')
    password_input.fill("password")

    # Находим кнопку "Login" и кликаем на нее
    login_button = page.locator('//button[@data-testid="login-page-login-button"]')
    login_button.click()

    # Проверяем, что появилось сообщение об ошибке
    wrong_email_or_password_alert = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
    expect(wrong_email_or_password_alert).to_be_visible() # Проверяем видимость элемента
    expect(wrong_email_or_password_alert).to_have_text('Wrong email or password') # Проверяем текст

    # Пауза на 5 секунд, чтобы увидеть результат
    page.wait_for_timeout(5000)
"""