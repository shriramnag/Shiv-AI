from datetime import datetime

def get_current_time_text():
    # समय को शब्दों में बदलने के लिए ताकि एआई हकलाए नहीं
    now = datetime.now()
    # उदाहरण: 2026 को "दो हजार छब्बीस" की तरह भेजने का लॉजिक यहाँ रहेगा
    return now.strftime("%Y-%m-%d %H:%M:%S")
  
