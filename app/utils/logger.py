import logging

def log_shiv_action(action):
    # टर्बो स्पीड पर लॉगिंग
    logging.basicConfig(filename='shiv_ai_history.log', level=logging.INFO)
    logging.info(f"कार्य: {action}")
