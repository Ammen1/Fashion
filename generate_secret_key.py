import secrets

# Generate a new SECRET_KEY
new_secret_key = secrets.token_hex(32)

# Print the new SECRET_KEY
print(new_secret_key)
