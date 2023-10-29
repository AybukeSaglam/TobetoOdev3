krediler = ["Hızlı kredi", "Maaşını alanlara özel","Emekliğe kredi"]

#kredi => alias değer/takma değer
for kredi in krediler:
    print(kredi)  #kredilerdeki bütün elemanları gezer.


for i in range(10):
    print(i)  #10'a kadar dönecek değerleri gösterir

for i in range(len(krediler)):
    print(krediler[i])

for i in range(0,11,2): #2'dan 10'a kadar 2'şer arttır. 11 dahil omaz!
    print(i)

for kredi in krediler:
    print("<option>" + kredi + "<option>") #açılır kutuda gösterir



