import random
import string

def generate_password():
    # Pick 3–5 letters (first uppercase, rest lowercase)
    first_letter = random.choice(string.ascii_uppercase)
    other_letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(2, 4)))
    
    # Symbol restricted to only @ or _
    symbol = random.choice(["@", "_"])
    
    # Pick 2–4 digits
    digits = ''.join(random.choice(string.digits) for _ in range(random.randint(2, 4)))
    
    # Combine all parts
    password = first_letter + other_letters + symbol + digits
    return password

# Example usage
for _ in range(1):
    print(generate_password())
