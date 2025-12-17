from playwright.sync_api import sync_playwright, expect

link = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"

with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    page = browser.new_page()

    page.goto(link)

    # Пытаемся проверить, что несуществующий локатор виден на странице:
    # unknown = page.locator('#unknown')
    # expect(unknown).to_be_visible()
    """
        AssertionError: Locator expected to be visible
        Actual value: None                                                                                                                                                                                      
        Error: element(s) not found                                                                                                                                                                             
        Call log:                                                                                                                                                                                               
            - Expect "to_be_visible" with timeout 5000ms                                                                                                                                                          
            - waiting for locator("#unknown")  
        """

    # Пытаемся ввести текст в кнопку Login:
    # login_button = page.get_by_test_id('login-page-login-button')
    # login_button.fill('unknown')
    """
        playwright._impl._errors.TimeoutError: Locator.fill: Timeout 30000ms exceeded.
        attempting fill action
        -   waiting for element to be visible, enabled and editable
        -   element is not enabled
    """


    # Пытаемся изменить текст заголовка
    page.evaluate(
        """
        const title = document.getElementById('authentication-ui-course-title-text')
        title.textContent = 'New text'
        """
    )
    """
        playwright._impl._errors.Error: Page.evaluate: TypeError: Cannot set properties of null (setting 'textContent')
            at eval (eval at evaluate (:234:30), <anonymous>:2:23)
            at eval (<anonymous>)
            at UtilityScript.evaluate (<anonymous>:234:30)
            at UtilityScript.<anonymous> (<anonymous>:1:44)

        Тайтл не успел загрузиться. В page.goto() добавить wait_until="networkidle" -> page.goto(link, wait_until="networkidle")
    """

    page.wait_for_timeout(3000)