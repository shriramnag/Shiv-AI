# ****************************************************************************
# प्रोजेक्ट: शिव एआई (SHIV AI) | मालिक: श्री राम नाग (Shri Ram nag)
# कार्य: shiv_memory.db फाइल को पहली बार बनाना
# ****************************************************************************

import sqlite3
import os

# १. सही रास्ता (Path) तय करना
db_folder = "database/learning_data"
db_path = os.path.join(db_folder, "shiv_memory.db")

# २. यदि फोल्डर नहीं है तो उसे बनाना
if not os.path.exists(db_folder):
    os.makedirs(db_folder)
    print(f"📁 फोल्डर बनाया गया: {db_folder}")

try:
    # ३. डेटाबेस से जुड़ना (यह फाइल को अपने आप बना देता है)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # ४. याददाश्त के लिए टेबल बनाना
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            information TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # ५. पहली याद सेव करना (मालिक का नाम)
    cursor.execute(
        "INSERT INTO memory (category, information) VALUES (?, ?)",
        ("Owner", "Shri Ram nag")
    )

    conn.commit()
    conn.close()
    print(f"✅ बधाई हो श्री राम नाग जी! 'shiv_memory.db' सफलता पूर्वक बन गई है।")
    print(f"📍 लोकेशन: {db_path}")

except Exception as e:
    print(f"🚨 एरर: {str(e)}")
  
