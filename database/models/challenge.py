from peewee import *
from database.connection import databaseIa
from datetime import datetime
from typing import TYPE_CHECKING,cast,Optional
import random
if TYPE_CHECKING:
    from database.models.challengeoption import ChallengeOptionModel
if TYPE_CHECKING:
    from database.models.challengeoptionpass import ChallengeOptionPassModel

class ChallengeModel(Model):
    name=TextField(unique=True,primary_key=True)
    options: list["ChallengeOptionModel"]
    passes: list['ChallengeOptionPassModel']
    sampleSize=IntegerField()
    description=TextField(null=True)
    created_at=DateTimeField(default=datetime.now)
    class Meta:
        database=databaseIa
    def hasEnoughSample(self):
        ops=list(self.options)
        if len(ops)==0:
            return False
        sampleSize=cast(int,self.sampleSize)
        for op in ops:
            passes_len=len(list(op.passes))
            if passes_len<sampleSize:
                return False
        return True
    def getRandomOption(self)->Optional['ChallengeOptionModel']:
        ops=list(self.options)
        if not ops:
            return None
        sample=cast(int,self.sampleSize)
        not_ready = [op for op in ops if len(list(op.passes)) < sample]    
        if not_ready:
            return random.choice(not_ready)
        return random.choice(ops)