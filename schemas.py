"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name.
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Example schemas (kept for reference):
class User(BaseModel):
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Flames-specific schema
class Calculationlog(BaseModel):
    """
    Collection name: "calculationlog"
    Stores each FLAMES calculation for analytics.
    """
    name_a: str = Field(..., description="First name")
    name_b: str = Field(..., description="Second name")
    count: int = Field(..., ge=0, description="Letter count used in FLAMES algorithm")
    result: str = Field(..., description="FLAMES outcome")
    source: Optional[str] = Field(None, description="Where the calc came from, e.g., web, mobile, bot")
    user_agent: Optional[str] = Field(None, description="Requester user agent string")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
