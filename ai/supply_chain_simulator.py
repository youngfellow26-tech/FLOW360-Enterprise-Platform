
import random

def simulate_disruption(event):
    return {
        "event":event,
        "diesel_price_change":random.randint(10,40),
        "explosives_delay_days":random.randint(2,12),
        "production_loss":random.randint(4,18)
    }
