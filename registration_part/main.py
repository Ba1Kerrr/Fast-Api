from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

#importing func to insert values in database 
from database import insert_values,find_users

app = FastAPI()

# Mount the static files directory
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "templates"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory='templates')

@app.post('/registrate', response_class=HTMLResponse)
async def registrate(full_name: str = Form(...), username: str = Form(...), email: str = Form(...), password: str = Form(...), confirm_password: str = Form(...)):
    if password == confirm_password  : #and find_users() < 0
        insert_values(full_name,username,email,password) # add to database
        return f'''
        <h1>Registration Successful!</h1>
        '''
    elif find_users() > 0:
        return f'''
        <h1>Registration Failed!</h1>
        <p>Username already exists</p>
        '''
    elif password != confirm_password:
        script = '<script>alert("Registration Failed!");</script>'
        templates.TemplateResponse('regitration-form.html')
    else:
        script = '<script>alert("Registration Failed!");</script>'
        templates.TemplateResponse('regitration-form.html')

@app.get('/reg-form', response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse('regitration-form.html', {'request': request})

@app.get('/', response_class=HTMLResponse)
async def main2(request: Request):
    return RedirectResponse("/reg-form")