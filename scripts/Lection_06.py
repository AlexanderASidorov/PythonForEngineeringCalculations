

# 1. Построение графиков в Python (продолжение)
# 
#



import matplotlib.pyplot as plt
import random








# Давайте изучим круговую диаграмму на примере визуализации текущего 
# распределения жителей на земле по струнам.
# Из Википедии, самые населенные страны мира:

countries = {'India': 1425775850, 'China': 1412600000, 'US': 336231646,
             'Indonesia': 278696200, 'Pakistan': 229488994, 'Nigeria': 216746934,
             'Brazil': 217440083, 'Bangladesh': 168220000, 'Russia': 147190000,
             'Mexico': 128271248, 'Total': 8045311447}

# Посчитаем количество людей живущих за пределами первой десятки стран
# по численности населения
countries['Rest'] = 2*countries['Total'] - sum(countries.values())
# удалим общее число людей на планете
countries.pop('Total')




# выведем данные на круговую диаграмму
plt.pie(list(countries.values()), labels=list(countries.keys()))

# что бы иметь какой-то контроль над цветами, напишем фунцкцию, которая будет
# генерировать нам палитру

def get_random_colors (n):
    # с помощью генератора случайных чисел сгенерим цвета для каждого 
    # из столбцов
    colors = []
    for _ in range (n):
        r= round(random.random(),3)
        g = round(random.random(),3)
        b = round(random.random(),3)
        a = round(random.random(),3)
        colors.append([r, g, b, a])
    return colors


    

plt.pie(list(countries.values()), 
        labels=list(countries.keys()),
        colors=get_random_colors(len(list(countries.values())))
        )


# Что бы иметь больше контроля над параметрами диаграммы, давайте создадим
# для нее отдельный объект

fig01=plt.figure()
# после этого мы можем настроить размер диаграммы (нирина и восота 
# в дюймах)
fig01.set_size_inches(9.0, 4.7)
# ее разрешение
fig01.set_dpi(900)
# отобразим процент от населения всего мира
plt.pie(list(countries.values()), 
        labels=list(countries.keys()),
        colors=get_random_colors(len(list(countries.values()))),
        autopct='%1.2f%%', pctdistance=0.9,
        radius = 1
        )
# Т.к. отображение процента на диаграмме в нашем случае не очень 
# удобно, мы можем убрать его в легенду.
# Для этого создадим отдельный словарь, где будет отображаться процент
# каждой страны в населении земли.
# создаем пустой словарь
countries_fraction = {}
# после чего будем добавлять в него ключи из словаря counties, а
# а значения будем расчитывать
for key, value in countries.items():
    key_new = key
    value_new = round(100*(value/(sum(countries.values()))), 2)
    countries_fraction[key_new] = value_new
 
#%%    
# Создадим объект fig02 и настроем его размер и разрешение    
fig02 = plt.figure()
fig02.set_size_inches(8.0, 5.0)
fig02.set_dpi(900)

# в этот раз цветовую гамму настроим не собственной функцией, а  возьмем
# один из готовых стилей.
# Список фозможных стилей смотрите здесь:
# https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
#plt.style.use('grayscale')
plt.style.use('seaborn-v0_8-bright')
#plt.style.use('seaborn-v0_8-dark-palette')


plt.pie(list(countries.values()), 
        labels=list(countries.keys()),
        radius = 1
        )

labels_percentage = [ str(key) + ' (' + str(value)+'%)' for key, value in countries_fraction.items()]

plt.legend(labels=labels_percentage,
          title="Population",
          loc='upper left', bbox_to_anchor=(1.0, 0.9))
# в конце можем сохранить рисунок в файл:
fig02.savefig('Population.png')


#%%
# Иногда появляется необходимость вывести два графика, которые будут 
# иметь одну общую ось.
# Давайте выведем график изменения населения России и Китая за
# последние 30 лет
# Очевидно, что эти графики будут иметь общую ось x, но из-за разности
# порядка населенности двух стран выводить их на одном графике не
# не очень целесообразно.

China = {'1990': 1135185000, '1995': 1204855000 , '2000': 1262645000, 
         '2005': 1303720000 , '2010': 1337705000, '2015': 1379860000, 
         '2020': 1411100000}

Russia = {'1990': 147665081, '1995': 148459937 , '2000': 146890128, 
         '2005': 143474219	 , '2010': 142856536, '2015': 146267288, 
         '2020': 146748590}
 
for item in China:
    China[item] = round(float(China[item]/1000000), 0)

for item in Russia:
    Russia[item] = round(float(Russia[item]/1000000), 0)


fig03, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
fig03.set_size_inches(7.0, 7.0)
fig03.set_dpi(900)

# строим зависимость для Китая
#ax[0].ticklabel_format(style='plain')
ax[0].plot(list(China.keys()), list(China.values()))
ax[0].set_ylabel('Population, milions of people')
ax[0].grid(True)
ax[0].set_title('Population in China')


ax[1].plot(list(Russia.keys()), list(Russia.values()))
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Population, milions of people')
ax[1].grid(True)
ax[1].set_title('Population in Russia')



























