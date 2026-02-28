import logging

def log_activity(activity):
    logging.basicConfig(filename='shiv_ai_log.txt', level=logging.INFO)
    logging.info(f"एक्टिविटी: {activity}")
    print(f"लॉग: {activity}")
  
