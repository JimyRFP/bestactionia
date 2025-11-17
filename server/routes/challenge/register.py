from fastapi import APIRouter,status
from server.routes.challenge.env import URL_PREFIX
from params.challenge.register import ChallengeRegisterParams
from functions.createChallenge import BestActionIaCreate

     
router=APIRouter(prefix=URL_PREFIX)
@router.post('/register',status_code=status.HTTP_201_CREATED)
async def register(data:ChallengeRegisterParams):
    creator=BestActionIaCreate(data)
    res=creator.create()
    return {'name':res.name,'optionsLen':len(list(res.options))}