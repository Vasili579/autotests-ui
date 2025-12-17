from playwright.sync_api import sync_playwright, expect

link = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"

with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    page = browser.new_page()

    page.goto(link)

    """
    AssertionError: Locator expected to be visible
    Actual value: None                                                                                                                                                                                      
    Error: element(s) not found                                                                                                                                                                             
    Call log:                                                                                                                                                                                               
        - Expect "to_be_visible" with timeout 5000ms                                                                                                                                                          
        - waiting for locator("#unknown")  
    """
    # unknown = page.locator('#unknown')
    # expect(unknown).to_be_visible()

    """
    playwright._impl._errors.TimeoutError: Locator.fill: Timeout 30000ms exceeded.
    """
    # login_button = page.get_by_test_id('login-page-login-button')
    # login_button.fill('unknown')


    """
    playwright._impl._errors.Error: Page.evaluate: TypeError: Cannot set properties of null (setting 'textContent')
    
    Тайтл не успел загрузиться. В page.goto() добавить wait_until="networkidle" -> page.goto(link, wait_until="networkidle")
    """
    page.evaluate(
        """
        const title = document.getElementById('authentication-ui-course-title-text')
        title.textContent = 'New text'
        """
    )

    page.wait_for_timeout(3000)