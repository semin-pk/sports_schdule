from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from routes import schdule_routers
from starlette.exceptions import HTTPException as StarletteHTTPException

# FastAPI
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(schdule_routers, prefix="/schedule")

@app.get("/")
async def index():
    return "Hello this is Let's Server"

@app.get("/hello")
async def hello():
    return "Hello"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
