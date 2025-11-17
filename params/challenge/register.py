from pydantic import BaseModel
from typing import Optional
class ChallengeRegisterParamsOptions(BaseModel):
    text:str

class ChallengeRegisterParams(BaseModel):
     challengeName:str
     challengeSample:int
     challengeDescription:Optional[str]
     options:list[ChallengeRegisterParamsOptions]