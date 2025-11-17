from fastapi import APIRouter,HTTPException,status
from server.routes.challenge.env import URL_PREFIX
from pydantic import BaseModel
from database.models.challengeoptionpass import ChallengeOptionPassModel
router=APIRouter(prefix=URL_PREFIX)

class RewardParams(BaseModel):
    passId:str
    reward:int


@router.post('/setReward')
async def set(data:RewardParams):
    if(data.reward<1):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='reward must be greater then 0')
    passe=ChallengeOptionPassModel.get_or_none(ChallengeOptionPassModel.id==data.passId)
    if(not passe):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='unknwon passe')
    ChallengeOptionPassModel.setReward(passe,data.reward)
    return {}
