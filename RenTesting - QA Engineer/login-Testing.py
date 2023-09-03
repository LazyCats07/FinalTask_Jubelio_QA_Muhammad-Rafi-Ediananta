from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Inisialisasi WebDriver (Anda perlu menyesuaikan path ke driver Anda)
driver = webdriver.Chrome(executable_path='D:\RAFI\1. EDUcate\9. Telkom University\3. KEGIATAN\Intern\Jubelio - QA software\FinalTask_Jubelio_QA_Muhammad Rafi Ediananta\chromedriver-win64')

# Skenario 1: Login ke halaman Jubelio
def login_to_jubelio(username, password):
    driver.get('https://app.jubelio.com/login')

    # Temukan elemen-elemen input dan tombol login
    username_input = driver.find_element_by_class('username')
    password_input = driver.find_element_by_id('password')
    login_button = driver.find_element_by_id('login-button')

    # Masukkan username dan password, lalu klik tombol login
    username_input.send_keys("qa.rakamin.jubelio@gmail.com")
    password_input.send_keys("Jubelio123!")
    login_button.click()

# Tutup browser setelah selesai
driver.quit()
