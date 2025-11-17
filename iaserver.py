from fastapi import FastAPI
from server.routes.challenge import register,option,reward
app=FastAPI()
app.include_router(register.router)
app.include_router(option.router)
app.include_router(reward.router)


