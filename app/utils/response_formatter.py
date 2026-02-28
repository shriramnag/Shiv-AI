# श्री राम नाग जी, यह फाइल सुनिश्चित करती है कि एआई हकलाए नहीं।
# यह नंबरों और डॉट्स को शब्दों में बदल देती है।

def clean_shiv_response(text):
    # नंबरों को हिंदी शब्दों में बदलना (उदाहरण के लिए)
    replacements = {
        "1": " एक ", "2": " दो ", "3": " तीन ", "4": " चार ", "5": " पाँच ",
        ".": " डॉट ", ",": " कोमा ", "ip": " आई पी "
    }
    
    cleaned_text = str(text).lower()
    for key, val in replacements.items():
        cleaned_text = cleaned_text.replace(key, val)
        
    return cleaned_text.strip()
