from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory='app/templates')
router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@router.post("/join_chat", response_class=HTMLResponse)
async def join_chat(request: Request, username: str = Form(...), room_id: int = Form(...)):
    # Простая генерация user_id
    user_id = hash(username) % 10000
    return templates.TemplateResponse("index.html",
                                      {"request": request,
                                       "room_id": room_id,
                                       "username": username,
                                       "user_id": user_id}
                                      )

# Этот эндпоинт выполняет несколько задач:

# Получает username и room_id из формы (с помощью Form(...)).

# Генерирует случайный идентификатор пользователя в диапазоне от 100 до 100000

# Возвращает HTML-страницу index.html с переданными в шаблон параметрами:

# room_id – ID комнаты, куда заходит пользователь.

# username – имя пользователя.

# user_id – сгенерированный идентификатор пользователя.