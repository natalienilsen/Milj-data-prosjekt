import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Laste og forberede data
def prepare_data_for_regression(filepath):

    # Forbereder dataen
    df = pd.read_csv(filepath)

    # Visualiserer manglende data
    visualize_missing_data(df)

    # Enkel håndtering av manglende verdier
    df.fillna(df.mean(numeric_only=True), inplace=True)

    # Konverterer kategori-variabler til numeriske variabler ved bruk av one-hot encoding
    df_encoded = pd.get_dummies(df, columns=['category', 'main_pollutant'])

    # Skiller ut features X (uavhenig variabel) og målvariabelen y (avhengig variabel)
    X = df_encoded.drop(['AQI', 'By'], axis=1) 
    y = df_encoded['AQI']

    return X, y, df

# 2. Trener og evaluerer modellen
def train_regression_model(X, y):

    # Separer dataene i treining- og test-sett
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Lager og trener modellen
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions:
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    # Performance metrics:
    metrics = {
        'train_r2': r2_score(y_train, y_pred_train),
        'test_r2': r2_score(y_test, y_pred_test),
        'train_rmse': np.sqrt(mean_squared_error(y_train, y_pred_train)),
        'train_rmse': np.sqrt(mean_squared_error(y_test, y_pred_test))
    }

    return model, metrics, (X_train, X_test, y_train, y_test, y_pred_test)

# 3. Visualiserer resultatene
def visualize_predictions(results):

    X_train, X_test, y_train, y_test, y_pred_test = results 
    
    # Faktisk vs. Prediktiv plot
    plt.figure(figsize(10, 6))
    sns.scatterplot(x=y_test, y=y_pred_test, alpha=0.5)
    plt.scatter(y_test, y_pred_test, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.xlabel('Faktisk AQI')
    plt.ylabel('Prediktiv AQI ')
    plt.title('Faktisk vs Prediktiv AQI verdier')
    plt.tight_layout()
    plt.show()

    # Gjenværende plot
    residual = y_test - y_pred_test
    plt.figure(figsize(10, 6))
    plt.scatterplot(x=y_pred_test, y=residual, alpha=0.5)
    plt.xlabel('Forutsett AQI')
    plt.ylabel('Gjenværende')
    plt.title('Gjenværende plot')
    plt.axhline(y=0, color='r', linestyle='--')
    plt.tight_layout()
    plt.show()

# Visualiserer manglende data
def visualize_missing_data(df):

    plt.figure(figsize=(10, 6))
    sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
    plt.title("Manglende verdier i datasettet")
    plt.show()

    plt.figure(figsize=(10, 6))
    df.isnull().sum().plot(kind='bar', color='orange')
    plt.title ("Antall manglende verdier per kolonne")
    plt.ylabel("Antall")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Visualiserer trender
def visualize_trends(df):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='Dato', y='AQI')
    plt.title("Luftkvalitet (AQI) over tid")
    plt.xlabel("Dato")
    plt.ylabel("AQI")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Hovedprogrammet: 
def main():

    sns.set_style("whitegrid")
    sns.set_palette("coolwarm")

    file_path = '/Users/mariaforland/Documents/NTNU/4.\ Semester/5.\ Semester/6.\ Semester/Milj-data-prosjekt/data/clean/luftkvalitet_byer_clean.csv'

    # Forberede data
    X, y, df = prepare_data_for_regression(file_path)

    # Visualisere trender i dataene
    visualize_trends(df)

    # Trene modellen og få resultater
    model, metrics, results = train_regression_model(X, y)

    # Print modell performance metrics
    print("\nModel Performance Metrics:")
    print(f"Training R² Score: {metrics['train_r2']:.4f}")
    print(f"Testing R² Score: {metrics['test_r2']:.4f}")
    print(f"Training RMSE: {metrics['train_rmse']:.4f}")
    print(f"Testing RMSE: {metrics['test_rmse']:.4f}")

    # Vis koeffisientene til modellens variabler - jo større absoluttverdi koeffisienten har, jo viktigere er variablene
    feature_importance = pd.DataFrame({
        'Feature': X.columns,
        'Coefficient': model.coef_
    })
    print("\nFeature importance:")
    print(feature_importance.sort_values(by='Coefficient', key=abs, ascending=False))

    # Visualiserer resultatene
    visualize_predictions(results)

if __name__ =="__main__":
    main()

