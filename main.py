from fastapi import FastAPI, UploadFile, Form, Response, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
from typing import Annotated
import sqlite3


con = sqlite3.connect('db.db', check_same_thread=False)
cur = con.cursor()

app = FastAPI()

SERCRET = "super-coding"
manager = LoginManager(SERCRET, '/login')


@manager.user_loader()
def query_user(data):
    WHERE_STATEMENTS = f'id="{data}"'
    if type(data) == dict:
        WHERE_STATEMENTS = f'''id="{data['id']}"'''

    con.row_factory = sqlite3.Row  # 컬럼명도 같이 가져오겠다.
    cur = con.cursor()
    user = cur.execute(f"""
                       SELECT * from users WHERE {WHERE_STATEMENTS}
                       """).fetchone()
    return user


@app.post('/login')
def login(id: Annotated[str, Form()],
          password: Annotated[str, Form()]):
    user = query_user(id)
    # user가 있는지 없는지를 판단
    if not user:
        raise InvalidCredentialsException  # 파이썬에서는 에러메세지   raise로 보냄
    elif password != user['password']:  # user의 패스워드 정보가 일치하지 않으면
        raise InvalidCredentialsException

    # access 토큰을 만들어서 토큰안에 정보를 가져옴
    access_token = manager.create_access_token(data={
        'sub': {
            'id': user['id'],
            'name': user['name'],
            'email': user['email'],
        }
    })

    return {'access_tokoen': access_token}

# signup html 받기 post 값으로 보내기


@app.post('/signup')
# id를 문자열로 폼데이터를 통해 보낼 것이다라는 선언
def signup(id: Annotated[str, Form()],
           password: Annotated[str, Form()],
           name: Annotated[str, Form()],
           email: Annotated[str, Form()]):
    # 받은 정보를 데이터에 입력 회워가입을 하면 무조건 넣음
    cur.execute(f"""
                INSERT INTO users(id,name,email,password)
                VALUES ('{id}','{name}','{email}','{password}')
                """)
    con.commit()


@app.post('/items')
async def create_item(image: UploadFile,
                      title: Annotated[str, Form()],
                      price: Annotated[int, Form()],
                      description: Annotated[str, Form()],
                      place: Annotated[str, Form()],
                      insertAt: Annotated[int, Form()],
                      user=Depends(manager)
                      ):

    image_bytes = await image.read()
    cur.execute(f"""
                INSERT INTO items(title,image,price,description,place,insertAt)
                VALUES ('{title}','{image_bytes.hex()}',{price},'{description}','{place}','{insertAt}')
                """)
    con.commit()
    return '200'


@app.get('/items')
async def get_items(user=Depends(manager)):  # depends 는 인증된 user만 내려줌
    # 컬럼명도 같이 가져옴
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    rows = cur.execute(f"""
                       SELECT * from items;
                       """).fetchall()

    return JSONResponse(jsonable_encoder(dict(row) for row in rows))
# array 형태라 for문을 이용하여 id값을 돌리면서 가져옴


# 이미지 응답 API
@app.get('/images/{item_id}')  # 이미지를 ID 값으로 가져오기
async def get_image(item_id):
    cur = con.cursor()
    image_bytes = cur.execute(f"""
                              SELECT image from items WHERE id={item_id}
                              """).fetchone()[0]  # fetchone은 0번째 index를 넣어준다.
    return Response(content=bytes.fromhex(image_bytes))  # 이미지 byte를 가져와서 이거를 해석을 한 뒤 컨텐츠로 response하겠다.


# app.mount는 루트 경로라 이 위에 서버 생성해줘야함
app.mount("/", StaticFiles(directory="frontend",
          html=True), name="frontend")
