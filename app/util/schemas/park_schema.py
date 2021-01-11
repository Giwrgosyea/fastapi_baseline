from pydantic import BaseModel, Field


class Park_schema(BaseModel):
    park_name: str = Field(...)
    asset_id: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "park_name": "Xanthi",
                "asset_id": "564236523",
            }
        }
