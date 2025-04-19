from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from app.query_data import get_answer,format_response

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def get_home():
    return FileResponse("static/index.html")


@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    question = body.get("question", "")
    answer = get_answer(question)
    #return JSONResponse({"answer": answer})
    print(f"{answer}")
    formatted_response = format_response(answer)
    return JSONResponse({"response": formatted_response})
