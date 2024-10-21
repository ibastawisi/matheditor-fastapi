from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pix2text import Pix2Text, merge_line_texts

app = FastAPI()
p2t = Pix2Text()

origins = [
    "https://matheditor.me",
    "https://matheditor.vercel.app",
    # "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return HTMLResponse("""
    <!DOCTYPE html>
        <html>
        <head>
            <title>Math Editor Fastapi</title>
        </head>
        <body>
            <h1>Math Editor Fastapi</h1>
            <ul>
                <li><a href="/docs">/docs</a></li>
                <li><a href="/redoc">/redoc</a></li>
            </ul>
        </body>
    </html>
    """)

@app.post('/pix2text')
async def pix2text(file: UploadFile):
    outs = p2t.recognize(file.file, resized_shape=608,isolated_sep=('$$', '$$'))
    return {'generated_text': outs}
