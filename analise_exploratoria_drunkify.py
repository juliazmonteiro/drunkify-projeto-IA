# =======================================================
# Projeto: Drunkify - Análise Exploratória de Dados
# Integrante: Júlia Zanin Monteiro - RA: 10400678 - 10400678@mackenzista.com.br
# Síntese: Script para EDA, visualização e preparação de dados para ML.
# =======================================================

import pandas as pd

csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSUnhb0Gzj-AiGcrsgMBF8R0wWelqvFdM-a85AoYn2iF_f7A7POTbuI9adKCrx7HQJ09cUTpj3dR07K/pub?output=csv"  # substitua pelo link CSV que você copiou
df = pd.read_csv(csv_url)
df.head()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")

df.head()
df.info()

# humores
plt.figure(figsize=(7,4))
sns.countplot(data=df, x='humor')
plt.title("Distribuição de Humores")
plt.xticks(rotation=30)
plt.show()

# estilos musicais
plt.figure(figsize=(7,4))
sns.countplot(data=df, x='estilo_musical')
plt.title("Distribuição de Estilos Musicais")
plt.xticks(rotation=30)
plt.show()

# humor x bebida
pd.crosstab(df['humor'], df['bebida_favorita']).head()

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score

le_humor = LabelEncoder()
df['humor_encoded'] = le_humor.fit_transform(df['humor'].astype(str))

le_musica = LabelEncoder()
df['estilo_musical_encoded'] = le_musica.fit_transform(df['estilo_musical'].astype(str))

le_bebida = LabelEncoder()
df['bebida_encoded'] = le_bebida.fit_transform(df['bebida_favorita'].astype(str))

X = df[['humor_encoded', 'estilo_musical_encoded']]
y = df['bebida_encoded']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print("Acurácia:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, zero_division=0))

os.makedirs('/content/drunkify_artifacts', exist_ok=True)

joblib.dump(clf, '/content/drunkify_artifacts/dt_bebida_model.joblib')
joblib.dump(le_humor, '/content/drunkify_artifacts/le_humor.joblib')
joblib.dump(le_musica, '/content/drunkify_artifacts/le_musica.joblib')
joblib.dump(le_bebida, '/content/drunkify_artifacts/le_bebida.joblib')

plt.figure(figsize=(7,4))
sns.countplot(data=df, x='humor')
plt.title("Distribuição de Humores")
plt.tight_layout()
plt.savefig('/content/drunkify_artifacts/dist_humor.png')
plt.close()

print("Artefatos salvos em /content/drunkify_artifacts")
