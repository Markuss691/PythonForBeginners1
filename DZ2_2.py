mn1 = {'Анатолий Кузнецов','Спартак Мишулин','Кахи Кавсадзе','Павел Луспекаев'}
mn2 = {'Джим Керри','Джефф Дэниелс','Лорен Холли','Майк Старр'}
mn3 = {'Яна Троянова','Гоша Куценко','Александр Баширов'}

X = {'id': '1', 'name': 'Белое солнце пустыни', 'year': '1968', 'genre': 'Боевик', 'country': 'USSR', 'actors': mn1}
Y = {'id': '2', 'name': 'Тупой и ещё тупее', 'year': '1993', 'genre': 'Комедия', 'country': 'USA', 'actors': mn2}
Z = {'id': '3', 'name': 'Страна ОЗ', 'year': '2015', 'genre': 'Артхаус', 'country': 'Russia', 'actors': mn3}

Films = [X,Y,Z,]

Pk = input('Введите категорию для поиска фильма (name year genre country actors):')

Pv = input('Введите значение категории для поиска фильма:')

for f in Films:
    for key, value in f.items():
        if key == Pk and type(value) != set:
          if value == Pv:

              print(f['name'])
        if key == Pk and type(value) == set:

             if Pv in value:
                 print('Фильм ' + '"'+ f['name']+ '"')
                
           


