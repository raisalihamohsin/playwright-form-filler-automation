from playwright.sync_api import sync_playwright

def fill_form():
    with sync_playwright() as p:
        # Browser kholo (slow_mo thoda kam kiya hai taake fast ho)
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        
        print(">>> Opening registration form...")
        page.goto("https://demo.automationtesting.in/Register.html")
        
        # ---------- PERSONAL INFO (Sirf yahan fill use kiya hai) ----------
        print(">>> Filling personal information...")
        page.fill('input[placeholder="First Name"]', 'Saliha')
        page.fill('input[placeholder="Last Name"]', 'Mohsin')
        page.fill('textarea[ng-model="Adress"]', 'House # 123, Street 5, Phase 7, DHA, Lahore, Pakistan')
        page.fill('input[type="email"]', 'raisalihamohsin@gmail.com')
        page.fill('input[type="tel"]', '033********')
        
        # ---------- GENDER (Direct Click - Safe hai) ----------
        print(">>> Selecting Gender...")
        page.click('input[value="FeMale"]')
        
        # ---------- HOBBIES (Direct Click - Safe hai) ----------
        print(">>> Selecting Hobbies...")
        page.check('input[value="Cricket"]')
        page.check('input[value="Hockey"]')
        
        # ---------- LANGUAGES (100% JavaScript - UI ko bypass) ----------
        print(">>> Selecting Languages via JavaScript...")
        page.evaluate('''() => {
            // Language dropdown ko khulo
            const dd = document.querySelector('#msdd');
            if (dd) dd.click();
            
            // Saare options mein se English, Urdu, Hindi ko click karo
            setTimeout(() => {
                const items = document.querySelectorAll('.ui-corner-all, li a, .ui-menu-item');
                items.forEach(el => {
                    const txt = el.textContent.trim();
                    if (txt === 'English' || txt === 'Urdu' || txt === 'Hindi') {
                        el.click();
                    }
                });
            }, 300);
        }''')
        page.wait_for_timeout(1000)  # Languages select hone ka wait
        
        # ---------- SKILLS (Direct JavaScript) ----------
        print(">>> Selecting Skills...")
        page.select_option('#Skills', 'Programming')
        
        # ---------- COUNTRY (Direct JavaScript - UI bypass) ----------
        print(">>> Selecting Country via JavaScript...")
        page.evaluate('''() => {
            // Country dropdown ko khulo
            const countryDropdown = document.querySelector('.select2-selection--single');
            if (countryDropdown) countryDropdown.click();
            
            setTimeout(() => {
                const searchField = document.querySelector('.select2-search__field');
                if (searchField) {
                    searchField.value = 'Pakistan';
                    // Event trigger karo taake result show ho
                    const event = new Event('input', { bubbles: true });
                    searchField.dispatchEvent(event);
                }
                
                // Enter press karne ke liye keyboard event
                setTimeout(() => {
                    const options = document.querySelectorAll('.select2-results__option');
                    options.forEach(el => {
                        if (el.textContent.trim() === 'Pakistan') {
                            el.click();
                        }
                    });
                }, 500);
            }, 500);
        }''')
        page.wait_for_timeout(2000)  # Country settle hone ka wait
        
        # ---------- DATE OF BIRTH (Direct JavaScript - Super Safe) ----------
        print(">>> Selecting Date of Birth via JavaScript...")
        page.evaluate('''() => {
            // Direct values set karo
            const yearEl = document.querySelector('#yearbox');
            const monthEl = document.querySelector('#monthbox');
            const dayEl = document.querySelector('#daybox');
            
            if (yearEl) yearEl.value = '2006';
            if (monthEl) monthEl.value = '5';   // May
            if (dayEl) dayEl.value = '9';
            
            // UI ko update karne ke liye change event trigger karo
            ['#yearbox', '#monthbox', '#daybox'].forEach(id => {
                const el = document.querySelector(id);
                if (el) {
                    const event = new Event('change', { bubbles: true });
                    el.dispatchEvent(event);
                }
            });
        }''')
        page.wait_for_timeout(2000)
        
        # ---------- SCREENSHOT ----------
        page.screenshot(path='form_filled_final.png')
        print(">>> Screenshot saved: form_filled_final.png")
        page.wait_for_timeout(2000)
        browser.close()
        

if __name__ == "__main__":
    fill_form()