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


# region Select-Filter
# df = pd.read_csv(
#     filepath_or_buffer="data/imdb.csv",
#     encoding="utf-8"
# )
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


#rating 8.0 dan büyük olan filmlerin
#select-> Title Rating Year
#20-50 arasıdnaki filmler gelsin
#sort edelim
# print(
#     df[df["Rating"]>8.0]
#     [["Title","Rating","Year"]][20:50].sort_values(by="Rating",ascending=True)
#     )

# #Year 2014- 2019 arasında olan
# #Title,Rating,Year

# print(
#     df[(df["Year"]>=2014)&(df["Year"]<=2019)][["Title","Year"]]
# )

# # metascore 80 den büyük olanlar ve ratingi 8.0 dan büyük olanlar
# # Title, Rating ,Year,

# print(
#     df[(df["Metascore"]>=80)&(df["Rating"]>=8.0)][["Title","Rating","Metascore"]].sort_values(by="Metascore",ascending=True)
# ) 

# endregion

#region NBA Group-by Select Filter
# df = pd.read_csv(filepath_or_buffer="data/nba.csv",encoding="utf-8")

# print(
#     df[(df["Age"]>=25)&(df["Salary"]>=10000000)][["Name","Age"]].sort_values(by="Age",ascending=True)

# )

# #en yüksek maaşlı oyuncu
# print(
#     df[(df["Salary"])==(df["Salary"].max())][["Name","Age"]]
# )

# #group by
# print(
#     df.groupby(by="Position")["Salary"].sum()
# )
# print(
#     df.groupby(by="Team")["Salary"].sum().sort_values(ascending=True)
# )

# #kaç tane takım varsa onun sayısını döner
# print(
#     df["Team"].nunique()
# )
# print(
#     df.groupby(by="Team")["Team"].count()
# )
# result = df.groupby(by="Team")
# print(result.value_counts().to_string)# benzersiz satırların kaç kez tekrarlandığını ekrana yazar

# #yaşları 25-35 arasında olan adı takımı bilgilerini listele
# print(
#     df[(df["Age"]<=35)&(df["Age"]>=25)][["Name","Team"]]
# )
# print(
#     df[(df["Age"].between(25,35))][["Name","Team","Age"]].sort_values(by="Age" ,ascending=True)
# )
# result = df[(df["Age"].between(25,35))][["Name","Team","Age"]].sort_values(by="Age" ,ascending=True)
# print(result.groupby(by="Team").size())
# print(result.groupby(by="Team")["Age"].mean()) #yaş ortalaması hesaplar

# #custom funtion
# def str_find(name):
#     if isinstance(name, str):  # Eğer name bir string ise
#         return "and" in name
#     return False  # Eğer name string değilse False döner

# print(df["Name"].apply(str_find))
# print(df["Name"].apply(lambda x: str_find(x)))
# endregion


# region Youtube
df = pd.read_csv(filepath_or_buffer="data/youtube.csv",encoding="utf-8")

# print(df.shape)
# print(df.columns)


#Bu kod, bir Pandas DataFrame'deki verileri "Grade" sütununa göre gruplar, 
#her grubun "Views" sütunundaki toplamını hesaplar, bu toplamları artan sırada sıralar
#ve en düşük 10 sonucu ekrana yazdırır.
print(
    df.groupby(by="Grade")[["Views"]].sum().sort_values(by="Views",ascending=True).head(10)
    )
# endregion

