import jwt
import sys

if len(sys.argv) != 3:
    print("Usage: python verify_jwt.py <token> <secret>")
    sys.exit(1)

token = sys.argv[1]
secret = sys.argv[2]

try:
    result = jwt.decode(token, secret, algorithms=['HS256'])
    print("Valid signature! Decoded payload:", result)
except jwt.exceptions.InvalidSignatureError:
    print("Invalid signature!")
except Exception as e:
    print(f"Error: {e}")

# This script is used to verify whether the JWT we constructed meets the requirements
# use：python3 verify_jwt.py "JWT" "secret"
