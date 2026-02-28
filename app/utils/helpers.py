def clean_output_for_shiv(text):
    # यह फंक्शन सभी नंबरों को हिंदी शब्दों में बदल देगा
    # उदाहरण: 10 -> दस, 2026 -> दो हजार छब्बीस
    replacements = {
        "1": "एक", "2": "दो", "3": "तीन", "4": "चार", "5": "पांच",
        "6": "छह", "7": "सात", "8": "आठ", "9": "नौ", "0": "शून्य", ".": ","
    }
    for num, word in replacements.items():
        text = text.replace(num, word)
    return text
  
