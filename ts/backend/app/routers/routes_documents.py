from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db, get_current_user
from app.database import models, schemas

from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from datetime import datetime



from app.database.models import Document
from app.utils.hashing import generate_sha256
from app.core.s3 import upload_file_to_s3
from app.core.security import get_current_user

router = APIRouter()

@router.post("/", response_model=schemas.DocumentOut)
def create_doc(payload: schemas.DocumentCreate, current=Depends(get_current_user), db: Session = Depends(get_db)):
    doc = models.Document(
        owner_id=current["id"],
        doc_type=payload.doc_type,
        doc_number=payload.doc_number,
        file_url=payload.file_url,
        hash=payload.hash,
        issued_at=payload.issued_at,
        org_name=current["org_name"]
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc

@router.get("/")
def list_docs(current=Depends(get_current_user), db: Session = Depends(get_db)):
    if current["role"] == "auditor":
        return db.query(models.Document).all()
    return db.query(models.Document).filter(models.Document.org_name == current["org_name"]).all()




router = APIRouter(prefix="/documents", tags=["Documents"])

@router.post("/upload")
async def upload_document(
    doc_type: str,
    doc_number: str,
    issued_at: datetime,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    file_bytes = await file.read()

    # 1️⃣ Hash
    file_hash = generate_sha256(file_bytes)

    # 2️⃣ Upload to S3
    file_url = upload_file_to_s3(file_bytes, file.filename)

    # 3️⃣ Save metadata
    document = Document(
        owner_id=current_user.id,
        doc_type=doc_type,
        doc_number=doc_number,
        file_url=file_url,
        hash=file_hash,
        issued_at=issued_at
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return {
        "message": "Document uploaded successfully",
        "document_id": document.id,
        "hash": file_hash
    }
