import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from joblib import dump


df = pd.read_csv('./data/churn.csv')
Y = df["churn"]

df = (df
      .astype({"gender": "category", "country": "category", "products_number": "category",
               "credit_card": bool, "active_member": bool, "churn": "category"})
      .drop(["customer_id"], axis=1)
)

df_ = df.drop("churn", axis=1)
numerical = list(filter(lambda x: df_[x].dtype in [np.int64, np.float64], df_.columns))
categorical = list(filter(lambda x: x not in numerical, df_.columns))

column_transformer = make_column_transformer(
    (StandardScaler(), numerical),
    (OneHotEncoder(drop="first"), categorical)
)

column_transformer.fit(df_)
X = column_transformer.transform(df_)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2,
                                                    random_state=42)

clf = RandomForestClassifier(n_estimators=10,
                             max_depth=2,
                             random_state=0)

clf.fit(X_train, y_train)

dump(clf, 'model/churn.joblib')
dump(column_transformer, 'model/transformer.joblib')
