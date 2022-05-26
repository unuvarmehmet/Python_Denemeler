dict_example = {
    'recipe1': {'menemen':['domates', 'biber', 'yumurta']},
    'recipe2': {'dolma':['yaprak', 'salça', 'pirinç']},
    'recipe3': {'kuru fasulye':{'kuru fasulye', 'Tuz', 'su', 'salça'}}            
}
sesli_harf = ['a', 'e', 'i', 'ö', 'ü', 'ı', 'u', 'o']
yeni = []

for i in dict_example.values():
    for k in i.values():
        for j in k:
            x = -1
            while x < len(j)-1:
                x += 1
                if j[x] in sesli_harf:
                    yeni.append(j[x])
                else:
                    continue
print(yeni)
print(len(yeni))


