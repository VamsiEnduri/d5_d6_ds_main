print("1. adding student")
print("2. view students")
print("3. update student")
print("4. delete student")
print("5. exist")
import json

f_name="students.json"

def read_data():
    try:
        with open(f_name,"r") as f: # 1
            return  json.load(f)
    except:
        with open(f_name,"w") as f:
            json.dump([],f)        
            
       

def save_data(data):
    with open(f_name,"w") as f:
        json.dump(data,f)


def add_student():
    name=input("enter name here :-- ")
    age=int(input("enter age here"))

    new_student={"name":name,"age":age}
    allStuds=read_data()
    allStuds.append(new_student)
    save_data(allStuds)
    print("student addedd successfully....")

def view_students():
    allStuds=read_data()
    for i in range(0,len(allStuds)):
        print(f"{i+1} - {allStuds[i]["name"]}- {allStuds[i]["age"]}")

def delete_student():
    allStuds=read_data()
    view_students()

    op=int(input("enter student id to remove from allStuds :-- "))
    allStuds.pop(op-1)
    print("these are students after deleting a student")
    save_data(allStuds)
    view_students()

def update_student():
    allStuds=read_data()
    view_students()

    op=int(input("enter student id to update from allStuds :-- "))
    name=input("enter name here :-- ")
    age=int(input("enter age here"))

    allStuds[op-1]={"name":name,"age":age}
    save_data(allStuds)
    print("student got updated...")

while True:
    o=int(input("choose operation :--"))
    if o==1:
        add_student()
    elif o == 2: 
        view_students()  
    elif o == 3:
        update_student()    
    elif o == 4:
        delete_student() 



# import json

# # file="a.json"
# # with open(file,"r") as f:
# #     data=json.load(f)
# #     print(type(data))

# file="data.json"

# with open(file,"r") as f:
#     data=json.load(f)
#     print(data)