from fastapi import Query
from pydantic import BaseModel, Field


class LimitOffset(BaseModel):
    limit: int = Field(
        Query(default=50, ge=1, le=100, description="Number of items to return")
    )
    offset: int = Field(Query(default=0, ge=0, description="Offset from the beginning"))


class CompanySearchQuery(LimitOffset):
    name: str | None = Field(
        Query(default=None, description="Company name [fuzzy search]")
    )
    website: str | None = Field(
        Query(default=None, description="Company website [exact match]")
    )
    country: str | None = Field(
        Query(
            default=None, description="Country where the company is based [exact match]"
        )
    )


class ContactSearchQuery(LimitOffset):
    job_title: str | None = Field(
        Query(default=None, description="Job title [exact match]")
    )
    job_level: str | None = Field(
        Query(default=None, description="Job level [exact match]")
    )
    job_function: str | None = Field(
        Query(default=None, description="Job function [exact match]")
    )


class CompanyResponse(BaseModel):
    id: int = Field(..., description="Company unique ID")
    name: str = Field(..., description="Company name")
    website: str | None = Field(default=None, description="Company website")
    country: str | None = Field(
        default=None, description="Country where the company is based"
    )

    class Config:
        orm_mode = True


class ContactResponse(BaseModel):
    id: int = Field(..., description="Contact unique ID")
    company: CompanyResponse | None = Field(default=None, description="Company details")
    name: str = Field(..., description="Contact person name")
    job_title: str = Field(..., description="Job title")
    job_level: str | None = Field(default=None, description="Job level")
    job_function: str | None = Field(default=None, description="Job function")

    class Config:
        orm_mode = True


class HTTP404Response(BaseModel):
    detail: str = Field(..., description="Human friendly error message")
