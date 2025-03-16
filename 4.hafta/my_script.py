import pandas as pd
import numpy as np

# region Intro Pandas

# number = ["10","20","30"]
# dict  = {
#     "a":10,
#     "b":20,
#     "c":30,
#     "d":40
# }

# np_array = np.array(["10","20","30","40"])

# # pd_series = pd.Series(["10","20","30","40"])
# # print(pd_series)
# # print(type(pd_series))

# pd_series = pd.Series(dict)
# print(pd_series)
# print(type(pd_series))

# print(pd_series.shape)
# print(pd_series.dtype)
# print(pd_series.ndim)#katman sayısı
# print(pd_series.describe())#matematiksel yararlı şeyler döner
# print(pd_series.head())
# print(pd_series.head(2))
# print(pd_series.tail(2))
# print(pd_series>=20)#seri içindeki ifadeler 20den büyük mü diye bakar true false döner
# print(pd_series%2 ==0)#seri içindeki ifadeler 2 ye bölünüyor mu diye bakar

# dodge_2025 = pd.Series(data=[10,20],index=["TRX 1500","RAW 2500"])
# dodge_2024 = pd.Series(data=[5,15],index=["TRX 1500","RAW 2500"])

# toplam = dodge_2025 + dodge_2024
# print(toplam)

# df = pd.DataFrame(
#     data=np.random.rand(3,5),#3 satır 5 sutun
#     index= ["A","B","C"],
#     columns=["Coloum1","Coloum2","Coloum3","Coloum4","Coloum5"]
# )

# print(df)

# #1.sutunu yazar
# print(df["Coloum1"])
# print(type(df["Coloum2"]))

# #1.sutunu yazar çift parantez olursa dataframe döner
# print(df[["Coloum1"]])
# print(type(df[["Coloum2"]]))

# print(df.loc["B"]) #transpose yazar
# print(df.loc["C","Coloum3"]) #sadece coloum3 ü yazar
# print(df.loc[:,["Coloum1","Coloum2"]])#bütün indexleeri yazar
# print(df.loc[["A","C"],["Coloum1","Coloum2"]])#istediğimiz sutun ve indexler

# endregion

df = pd.read_csv(
    filepath_or_buffer="data/imdb.csv",
    encoding="utf-8"
)
# print(df.shape)
# print(df.head(2))
# print(df.describe())

# # Title ya göre ilk 20 satırı yazdır
# # Path 1
# print(df[["Title","Year"]].head(20))
# # Path 2
# print(df[["Title","Year"]][0:20])
# # Path 3
# print(df.loc[0:20, ["Title","Year"]])

print(
    df[df["Rating"]>8.0]
    [["Title","Rating","Year"]][20:].sort_values(by="Rating",ascending=True)
    )