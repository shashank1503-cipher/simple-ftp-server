from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from os import getcwd, chdir
from utils import generate_random_name
import uvicorn
app = FastAPI()
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    chdir(getcwd() + "/files")
    get_random_name = generate_random_name(file.filename)
    file.filename = get_random_name
    with open(file.filename, 'wb') as image:
        content = await file.read()
        image.write(content)
        image.close()
    return {"filename": file.filename,"url":"http://127.0.0.1:5500/file/"+file.filename}

@app.get("/file/{name_file}")
def get_file(name_file: str):
    try:
        return FileResponse(path=getcwd() + "\\files\\" + name_file)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    


@app.get("/")
def home():
    routes = {
            "Upload File": "/upload",
            "Get File": "/file/{name_file}"
        }
    
    return routes

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=5500)

"""
Run this command to start the server:
uvicorn main:app --reload --port 5500
"""