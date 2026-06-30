from fastapi import FastAPI

app = FastAPI()
students = [
    {"id" : 1 , "name": "An"},
    {"id" : 2 , "name" : "Binh"},
    {"id" : 3, "name" : "Cuong"}
]

@app.get("/students/{id}")
def get_student(id :int):
    current_find = []
    for people in students:
        if people["id"] == id:
            current_find.append(people)
            return current_find 
    
    return {"message" : "Không tìm thấy"}
    
      
# ở đây đề bài muốn lấy dict của học sinh ở ví trí [0] , nhưng mà như thế này rất dễ bị sai lệch dữ liệu
# ta sẽ dùng cách vòng lặp rồi in ra data 

# trong bài còn thiếu đường path đúng và ép kiểu dữ liệu id , 
# khi ta đã có truy bằng id thì sẽ trả ra đúng dữ liệu của học sinh đó