from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, ForeignKey, Numeric
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database.connection import Base
from pydantic import BaseModel

import enum

class RoleEnum(str, enum.Enum):
    bank = "bank"
    corporate = "corporate"
    auditor = "auditor"
    admin = "admin"

class DocTypeEnum(str, enum.Enum):
    LOC = "LOC"
    INVOICE = "INVOICE"
    BILL_OF_LADING = "BILL_OF_LADING"
    PO = "PO"
    COO = "COO"
    INSURANCE_CERT = "INSURANCE_CERT"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)
    org_name = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    documents = relationship("Document", back_populates="owner")

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    doc_type = Column(Enum(DocTypeEnum))
    doc_number = Column(String)
    file_url = Column(String)
    hash = Column(String)
    issued_at = Column(DateTime)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    org_name = Column(String, nullable=False)
    owner = relationship("User", back_populates="documents")

