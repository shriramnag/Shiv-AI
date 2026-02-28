# श्री राम नाग जी, यह शिव एआई का यूनिवर्सल वेब नेविगेटर बॉट है।
# यह किसी भी वेबसाइट पर जाकर लॉगिन, सर्च और ईमेल लिखने में सक्षम है।

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class WebNavigatorBot:
    def __init__(self):
        self.driver = None

    def start_browser(self):
        if not self.driver:
            # यह ब्राउज़र को कंट्रोल करने वाला ड्राइवर शुरू करता है
            self.driver = webdriver.Chrome()

    def navigate_and_action(self, target_url, task, details=None):
        self.start_browser()
        print(f"मालिक, मैं {target_url} पर जा रहा हूँ...")
        self.driver.get(target_url)
        time.sleep(2) # पेज लोड होने का इंतज़ार

        # १. गूगल सर्च करना
        if "search" in task or "खोजो" in task:
            search_box = self.driver.find_element(By.NAME, "q")
            search_box.send_keys(details)
            search_box.send_keys(Keys.RETURN)
            return f"मालिक, मैंने गूगल पर {details} खोज लिया है।"

        # २. ईमेल लिखना (Gmail/Outlook)
        elif "email" in task or "ईमेल" in task:
            # यहाँ ईमेल प्लेटफॉर्म पर जाकर लिखने का लॉजिक लगेगा
            return f"मालिक, मैं ईमेल लिखने की प्रक्रिया शुरू कर रहा हूँ।"

        # ३. कहीं भी लॉगिन करना
        elif "login" in task or "लॉगिन" in task:
            return f"मालिक, मैं {target_url} पर लॉगिन करने की कोशिश कर रहा हूँ।"

        return "मालिक, वेबसाइट खुल गई है। आगे क्या आदेश है?"

web_nav_bot = WebNavigatorBot()
          
