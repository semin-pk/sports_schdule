from fastapi import APIRouter
from routes.schdule import sports_schdule_route

schdule_routers = APIRouter(tags=["Schdule"])

schdule_routers.routes.append(sports_schdule_route)