from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.router_page import router as router_page
from app.api.router_socket import router as router_socket

app = FastAPI()

app.mount('/static', StaticFiles(directory='app/static'), 'static')
app.include_router(router_socket)
app.include_router(router_page)
# https://habr.com/ru/companies/amvera/articles/884816/
# https://github.com/Yakvenalex/EasyFastApiWebsocketChat