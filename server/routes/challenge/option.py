from fastapi import APIRouter
from server.routes.challenge.env import URL_PREFIX
from functions.getPass import BestActionIaGetPass
from pydantic import BaseModel
from typing import Optional
router=APIRouter(prefix=URL_PREFIX)

class Commands(BaseModel):
    dontSaveTrained:Optional[bool]=None

@router.post('/option/{challenge_name}')
async def getAndSave(challenge_name:str,options:Optional[Commands]=None):
    motor=BestActionIaGetPass(challenge_name)
    if options and options.dontSaveTrained:
       ret=motor.getActionAndSaveNotTreined()
    else:
       ret=motor.getActionAndSavePass()
    return {'option':{'id':ret.option.id,'text':ret.option.text},
            'passe':{'id':ret.passe.id} if ret.passe else None}

