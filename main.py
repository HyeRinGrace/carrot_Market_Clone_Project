from fastapi import FastAPI,UploadFile,Form,Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles
from typing import Annotated
import sqlite3


con = sqlite3.connect('db.db',check_same_thread=False)
cur = con.cursor()


app = FastAPI()

@app.post('/items')
async def create_item(image:UploadFile, 
                title:Annotated[str,Form()],
                price:Annotated[int,Form()], 
                description:Annotated[str,Form()],
                place:Annotated[str,Form()],
                insertAt:Annotated[int,Form()]
            ):

    image_bytes = await image.read()
    cur.execute(f"""
                INSERT INTO items(title,image,price,description,place,insertAt)
                VALUES ('{title}','{image_bytes.hex()}',{price},'{description}','{place}','{insertAt}')
                """)
    con.commit()    
    return '200'


@app.get('/items')
async def get_items():
    # 컬럼명도 같이 가져옴
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    rows = cur.execute(f"""
                       SELECT * from items;
                       """).fetchall()
    
    return JSONResponse(jsonable_encoder(dict(row) for row in rows)) 
#array 형태라 for문을 이용하여 id값을 돌리면서 가져옴


#이미지 응답 API
@app.get('/images/{item_id}') #이미지를 ID 값으로 가져오기
async def get_image(item_id):
    cur = con.cursor()
    image_bytes = cur.execute(f"""
                              SELECT image from items WHERE id={item_id}
                              """).fetchone()[0]#fetchone은 0번째 index를 넣어준다.
    return Response(content=bytes.fromhex(image_bytes)) #이미지 byte를 가져와서 이거를 해석을 한 뒤 컨텐츠로 response하겠다.

# signup html 받기 post 값으로 보내기
@app.post('/signup')
# id를 문자열로 폼데이터를 통해 보낼 것이다라는 선언
def signup(id:Annotated[str,Form()], 
           password:Annotated[str,Form()],
           name:Annotated[str,Form()],
           email:Annotated[str,Form()]):
    # 받은 정보를 데이터에 입력
    cur.execute(f"""
                INSERT INTO users(id,name,email,password)
                VALUES ('{id}','{name}','{email}','{password}')
                """)
    con.commit()
    return '200'


# app.mount는 루트 경로라 이 위에 서버 생성해줘야함
app.mount("/", StaticFiles(directory="frontend",
          html=True), name="frontend")