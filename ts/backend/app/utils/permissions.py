from fastapi import HTTPException
def allow_roles(*roles):
    def check(role):
        if role not in roles:
            raise HTTPException(403, "Forbidden")
    return check