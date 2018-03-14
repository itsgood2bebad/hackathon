import pandas as pd
dt= pd.read_csv("Category.csv")
print(dt)
print(dt.continent.memory_usage(deep=True))
print(dt.country.memory_usage(deep=True))
#dt.continent.sort_values()
#dt.country.sort_values()
print(dt.continent.unique())
dt.continent=dt.continent.astype('category')
dt.continent.memory_usage(deep=True)
dt.country= dt.country.astype('category')
dt.country.memory_usage(deep=True)
dt.country.cat.categories
dico = {'ID':[100, 101, 102, 103], 'quality':['good', 'very good', 'good', 'excellent']}
dico = pd.DataFrame(dico)
print(dico)
print(dico.dtypes)
dico['quality_cat']=dico.quality.astype('category')

print(dico.sort_values(by='quality_cat'))
dico['quality_cat']=dico.quality.astype('category', categories=['good', 'very good', 'excellent'], ordered=True)
dico.quality_cat

dico.loc[dico.quality_cat > 'good']