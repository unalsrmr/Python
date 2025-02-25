# tuple3=(
#     'Sarıyer',
#     'Beşiktaş',
#     'Kadıköy',
#     'Üsküdar',
#     (1,2,3,4,5),
#     'Beykoz',
#     'Beylikdüzü',
#     ('a','b','c','d','e'),
# )
# tuple2=(
#     'Sarıyer',
#     'Beşiktaş',
#     'Kadıköy',  
#     'Üsküdar',
#     (1,2,3,4,5),
#     'Beykoz',
# )
# tuple1=tuple2+tuple3
# print(tuple1)
# print(tuple3[0])
# print(tuple3[1])
# print(tuple3[2])
# print(tuple3[3])
# print(tuple3[4][0])
# print(tuple3[5])
# print(tuple3[6])
# print(tuple3[7][0])
# print(tuple3[7][1])
# print(tuple3[7][2])
# print(tuple3[7][3])
# print(tuple3[7][4])


# x=2
# y=3
# toplam=x+y
# print(f"{x}+{y}={toplam}")

# # ...existing code...

# # Bir dictionary örneği
# my_dict = {
#     "isim": "Ahmet",
#     "yaş": 25,
#     "şehir": "İstanbul",
#     "meslek": "Mühendis"
# }

# # Dictionary içeriğini yazdırma
# print(my_dict)

# # Belirli bir anahtarın değerini yazdırma
# print(my_dict["isim"])
# print(my_dict["yaş"])

# # Yeni bir anahtar-değer çifti ekleme
# my_dict["hobi"] = "Yüzme"
# print(my_dict)

# # Bir anahtar-değer çiftini güncelleme
# my_dict["yaş"] = 26
# print(my_dict)

# # Bir anahtar-değer çiftini silme
# del my_dict["meslek"]
# print(my_dict)

# products = [
#     {"name": "Laptop","price": 1000},
#     {"name": "Mouse","price": 50},
#     {"name": "Keyboard","price": 150},
#     {"name": "Laptop","price": 10000},
#     {"name": "Monitor","price": 300}
# ]
# toplam=0
# for product in products:
#     toplam+=product.get("price")
# print(f"Toplam:{toplam}")
# for product in products:
#     if product.get("price")>100:
#         print(f"Name:{product.get('name')}")

# for product in products:
#     if product.get("name")=="Laptop" and product.get("price")>1000:
#         print(f"Name:{product.get('name')} ,Price:{product.get('price')}")

# from uuid import uuid4
# from pprint import pprint

# print(uuid4())
# print(type(uuid4()))

# categories={
#     "179e1430-c569-4302-96b1-f0f204412651":{
#         "name":"Elektronik",
#         "description":"Elektronik ürünler"
#     },
#     "dbb6abac-8a67-4182-87bf-dcfec5929516":{
#         "name":"Giyim",
#         "description":"Giyim ürünleri"
#     },
#     "f6b4f6c7-9a0b-4f4b-8e8b-8b4b6f1e4b4b":{
#         "name":"Kitap",
#         "description":"Kitaplar"
#     }
# }

# while True:
#     prcess = input("Type a process name: ")
#     match prcess:
#         case "create":
#             categories[str(uuid4())]={
#                 "name":input("Category name: "),
#                 "description":input("Category description: ")
#             }
#         case "list":
#             pprint(categories)
#         case "update":
#             categories.update({
#                 input("Category id: "):{
#                     "name":input("Category name: "),
#                     "description":input("Category description: ")
#                 }
#             })
#             pprint(categories)
#         case "delete":
#             id = input("Category id: ")
#             del categories[id]
#             pprint(categories)
#         case "e":
#             break
#         case _:
#             print("Invalid process name")
        
# from requests import get
# from pprint import pprint

# # Doğrudan URL'yi kullanarak isteği yapın
# response = get("https://jsonplaceholder.typicode.com/posts")
# data = response.json()
# pprint(data)

def sum(x,y)->int:
    return x+y
sum(2,32)
print(sum(2,3))

