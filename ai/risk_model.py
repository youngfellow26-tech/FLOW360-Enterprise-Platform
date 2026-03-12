
import random

def forecast_risk(sensor):
    score = random.random()
    return {
        "risk":score,
        "recommendation":"maintenance" if score>0.7 else "monitor"
    }
