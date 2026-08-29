from playwright.sync_api import sync_playwright


with sync_playwright() as p:

    # ---------- BROWSER SETUP ----------
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # ---------- OPEN WEBSITE ----------
    page.goto("https://demo.automationtesting.in/Register.html")

    # ---------- PERSONAL INFORMATION ----------
    page.fill(
        'input[placeholder="First Name"]',
        "Saliha"
    )

    page.fill(
        'input[placeholder="Last Name"]',
        "Mohsin"
    )

    page.fill(
        'textarea[ng-model="Adress"]',
        "House # 123, Street 5, Phase 7, DHA, Lahore, Pakistan"
    )

    page.fill(
        'input[type="Email"]',
        "raisalihamohsin@gmail.com"
    )

    page.fill(
        'input[type="tel"]',
        "03*********"
    )

    # ---------- GENDER ----------
    female = page.locator('input[value="FeMale"]')
    female.click()

    # ---------- HOBBIES ----------
    page.check('input[value="Cricket"]')
    page.check('input[value="Hockey"]')

    # ---------- LANGUAGES ----------
    
    language = page.locator("#msdd")
    language.click()

    page.get_by_text("English", exact=True).click()
    page.get_by_text("Urdu", exact=True).click()
    page.get_by_text("Hindi", exact=True).click()

    # Language dropdown se bahar click
    page.get_by_text("Date Of Birth", exact=True).click()

    # ---------- COUNTRY ----------
    country = page.locator("span.select2-selection.select2-selection--single")
    country.click()

    page.get_by_role("treeitem", name="India").click()
    # ---------- SKILLS ----------
    skills = page.locator("#Skills")

    skills.select_option("Python")


    # ---------- DATE OF BIRTH ----------
    year = page.locator("#yearbox")
    year.select_option("2005")

    month = page.locator('select[placeholder="Month"]')
    month.select_option("May")

    day = page.locator("#daybox")
    day.select_option("9")

    # ---------- SCREENSHOT ----------
    page.screenshot(path="form_filled_final.png")

    # ---------- SUCCESS MESSAGE ----------
    print("✅ Form filled successfully!")
    print("📸 Screenshot saved as: form_filled_final.png")

    # Keep browser open for 5 seconds
    page.wait_for_timeout(5000)

    # ---------- CLOSE BROWSER ----------
    browser.close()