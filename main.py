from fastapi import FastAPI, Header, HTTPException
import jwt

app = FastAPI()
SECRET_KEY = "segredo-sprint1"

@app.get("/admin-data")
def read_admin_data(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Token ausente (Unauthorized)")
    
    try:
        # Extrai o token do formato "Bearer <token>"
        token = authorization.split(" ")[1]
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        
        if payload.get("role") != "ADMIN":
            raise HTTPException(status_code=403, detail="Acesso negado (Forbidden)")
            
        return {"message": "Acesso liberado. Dados do Admin."}
    
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")