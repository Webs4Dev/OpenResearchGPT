from datetime import datetime

def log(message: str):

    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] OpenResearchGPT: {message}")