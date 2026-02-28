# श्री राम नाग जी, यह शिव एआई के डिजिटल हाथ हैं।
# यह माउस को हिलाने, फाइल पकड़ने और कीबोर्ड टाइप करने का काम करता है।

import pyautogui
import time

class VisualHandAgent:
    def __init__(self):
        # स्क्रीन की चौड़ाई और लंबाई सेट करना
        self.width, self.height = pyautogui.size()

    def move_and_click(self, x, y):
        """माउस को किसी खास जगह ले जाकर क्लिक करना"""
        pyautogui.moveTo(x, y, duration=0.5)
        pyautogui.click()
        return "मालिक, मैंने वहां क्लिक कर दिया है।"

    def drag_and_drop(self, start_x, start_y, end_x, end_y):
        """किसी फाइल को पकड़कर (Drag) दूसरी जगह छोड़ना (Drop)"""
        pyautogui.moveTo(start_x, start_y)
        pyautogui.dragTo(end_x, end_y, duration=1.0, button='left')
        return "मालिक, फाइल को एक जगह से दूसरी जगह रख दिया गया है।"

    def type_command(self, text):
        """कीबोर्ड से कुछ भी टाइप करना"""
        pyautogui.write(text, interval=0.1)
        pyautogui.press('enter')
        return f"मालिक, मैंने '{text}' टाइप कर दिया है।"

hand_agent = VisualHandAgent()
