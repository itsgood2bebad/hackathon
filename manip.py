import pandas as pd
import matplotlib
manip = pd.read_table("Manip str ds Pandas.txt",sep ="\t")
#print(manip)
 manip.choice_description = manip.choice_description.str.replace('[\[\]]','')
 a=manip.item_name.str.match('Chicken',case=False)
manip.item_price=manip.item_price.str.replace('$','')
#manip.item_price.astype(float)
manip.item_price.convert_objects(convert_numeric=True).mean()
print (manip1)
a= pd.crosstab(manip1.genre,manip1.content_rating)
print(a)
manip1.loc[(manip1.genre== 'Drama') & (manip1.duration>=200)]
manip1.title.sort_values(ascending =False)
#manip1.groupby(['title','duration']).
a = manip1.genre.value_counts()
b = round(manip1.genre.value_counts(normalize = True) * 100,2)
c = pd.concat([a,b],axis=1)
print(c)