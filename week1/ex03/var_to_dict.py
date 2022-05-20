d=[('Hendrix' , '1942'),('Allman' , '1946'),('King' , '1925'), ('Clapton' , '1945'), ('Johnson' , '1911'), ('Berry' , '1926'), ('Vaughan' , '1954'), ('Cooder' , '1947'), ('Page' , '1944'), ('Richards' , '1943'), ('Hammett' , '1962'), ('Cobain' , '1967'), ('Garcia' , '1942'), ('Beck' , '1944'), ('Santana' , '1947'), ('Ramone' , '1948'), ('White' , '1975'), ('Frusciante', '1970'), ('Thompson' , '1949'), ('Burton' , '1939')]
diz=dict()
for el in d:
    tmp = diz.get(el[1], [])
    tmp.append(el[0])
    diz[el[1]] = tmp
for x, y in diz.items():
    print(x, end=" : ")
    for el in y:
        print(el, end =" ")
    print()