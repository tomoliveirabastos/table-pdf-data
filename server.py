from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from extract_data_pdf_process import ExtractDataPdfProcess
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import File, UploadFile

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/razao-social")
def razao_social(request: Request):
    raza = request.query_params.get('nome')

    return {
        resultado: []
    }    

@app.post("/extrair_dados")
def extrair_dados(request: Request, file: UploadFile):
    path = "files/{}".format(file.filename)

    f = open(path, 'wb+')
    f.write(file.file.read())
    f.close()

    ExtractDataPdfProcess(path, int(request.query_params.get('column'))).run()

    return {
        "ok": "ok"
    }

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="index.html"
    )
