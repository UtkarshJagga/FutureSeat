from pydantic import BaseModel


class CollegeBase(BaseModel):
    name: str
    branch: str
    cutoff_rank: int


class CollegeCreate(CollegeBase):
    pass


class CollegeOut(CollegeBase):
    id: int

    class Config:
        from_attributes = True