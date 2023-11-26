from fastapi import FastAPI
import router
app=FastAPI()

@app.get("/mongo")
async def Home():
    return "Welcome Home"

app.include_router(router.router,prefix="/user",tags=["user"])