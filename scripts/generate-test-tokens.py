import jwt
import datetime

SECRET_KEY = "segredo-sprint1"

roles = ["OPERATOR", "ENGINEER", "MANAGER", "ADMIN"]

def gerar_tokens():
    print("=== TOKENS DE TESTE GERADOS (SPRINT 1 & 2) ===")
    for role in roles:
        payload = {
            "user": f"usuario_{role.lower()}",
            "role": role,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        print(f"\n[Perfil {role}]:")
        print(f"Bearer {token}")

if __name__ == "__main__":
    gerar_tokens()
