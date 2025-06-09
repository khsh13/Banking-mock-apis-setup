def is_suspicious(amount, location, time):
    if amount > 100000 or location not in ["IN", "US", "UK"]:
        return True
    return False
