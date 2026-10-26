import jwt
import datetime

SECRET_KEY = "segredo-sprint1"

def gerar_token(role: str):
    payload = {
        "user": f"teste_{role.lower()}",
        "role": role,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

if __name__ == "__main__":
    print("Token ADMIN:", gerar_token("ADMIN"))
    print("Token OPERATOR:", gerar_token("OPERATOR"))
