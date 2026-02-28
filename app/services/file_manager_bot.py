# श्री राम नाग जी, यह शिव एआई का फाइल मैनेजर बॉट है।
# यह स्क्रीनशॉट और कोड फाइलों को अपलोड करने और पढ़ने का काम करता है।

import os
import shutil

class FileManagerBot:
    def __init__(self):
        self.upload_dir = "app/uploads"
        if not os.path.exists(self.upload_dir):
            os.makedirs(self.upload_dir)

    def handle_upload(self, file_path, target_folder="services"):
        """फाइल को अपलोड फोल्डर से प्रोजेक्ट फोल्डर में ले जाना"""
        try:
            filename = os.path.basename(file_path)
            destination = f"app/{target_folder}/{filename}"
            shutil.copy(file_path, destination)
            return f"मालिक, फाइल '{filename}' सफलतापूर्वक अपलोड और सेव कर दी गई है।"
        except Exception as e:
            return f"क्षमा करें मालिक, अपलोड में समस्या आई: {str(e)}"

    def read_document(self, file_path):
        """अपलोड की गई फाइल के अंदर का डेटा पढ़ना"""
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()

file_manager_bot = FileManagerBot()

