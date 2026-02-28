# श्री राम नाग जी, यह सुरक्षा एजेंट अब एक्टिव मॉनिटरिंग और अलर्टिंग मोड में है।
import datetime

class CyberSecurityAgent:
    def __init__(self):
        self.owner = "Shri Ram nag"
        self.security_logs = "database/learning_data/security_alerts.txt"

    def monitor_activity(self, user_input, source_ip="Local"):
        """सिस्टम के साथ होने वाली हर छेड़छाड़ पर नज़र रखना"""
        
        # संदिग्ध कमांड्स या हैकिंग के प्रयास की पहचान
        hacking_patterns = ["sql injection", "sudo rm", "brute force", "nmap", "exploit"]
        is_suspicious = any(pattern in user_input.lower() for pattern in hacking_patterns)

        if is_suspicious:
            alert_message = f"🚨 अलर्ट! मालिक, कोई सिस्टम के साथ छेड़छाड़ की कोशिश कर रहा है। समय: {datetime.datetime.now()}"
            self._log_and_notify(alert_message, user_input)
            return alert_message
        
        return None

    def _log_and_notify(self, message, original_input):
        """खतरे को फाइल में सेव करना और मालिक को सूचित करने के लिए तैयार करना"""
        with open(self.security_logs, "a", encoding="utf-8") as f:
            f.write(f"{message} | इनपुट: {original_input}\n")
        print(f"सुरक्षा कवच सक्रिय: {message}")

security_port = CyberSecurityAgent()
