
#extraiga la info
from marketing.extract_data import read_local
#la transforme

from marketing.transform_data import transform_data
X, y = transform_data(df)
#cree el modelo
from marketin.create_model import create_model
#

model = LGBMClassifier(boosting_type='rf', bagging_freq=1, bagging_fraction=.3)
#el modelo aprende (Fitea la data)
model.fit(X, Y)

#guarde el resultado