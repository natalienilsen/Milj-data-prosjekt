import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import warnings
warnings.filterwarnings('ignore')

def load_city_data(city_name):
    """Load data for a specific city
    
    Args:
        city_name (str): Name of the city to load data for
        
    Returns:
        pd.DataFrame or None: DataFrame with city pollution data, or None if file not found
    """
    try:
        filepath = f"data/clean/byer/{city_name.lower()}_clean.csv"
        df = pd.read_csv(filepath)
        df['city'] = city_name
        
        # Convert datetime if it exists
        if 'datetime' in df.columns:
            df['datetime'] = pd.to_datetime(df['datetime'])
            df = df.sort_values('datetime')
        return df
    except FileNotFoundError:
        print(f"Could not find data file for {city_name}")
        return None

def analyze_single_city(df, city_name):
    """Analyze trends and patterns for a single city
    
    Args:
        df (pd.DataFrame): DataFrame containing city pollution data
        city_name (str): Name of the city being analyzed
        
    Returns:
        list: List of available pollutants in the dataset
    """
    
    # Basic statistics
    print(f"Number of measurements: {len(df)}")
    
    if 'datetime' in df.columns:
        time_span = df['datetime'].max() - df['datetime'].min()
        print(f"Time span: {time_span.days} days")
    
    # Pollution components analysis
    pollutants = ['pm2_5', 'pm10', 'no2', 'o3', 'so2', 'co', 'nh3']
    available_pollutants = [p for p in pollutants if p in df.columns and df[p].notna().any()]
    
    if available_pollutants:
        print(f"\nAvailable pollutants: {', '.join(available_pollutants)}")
        
        # Perform machine learning analysis
        ml_results = perform_ml_analysis(df, city_name, available_pollutants)
        
        # Create prediction plot if ML analysis was successful
        if ml_results:
            create_prediction_plot(ml_results, city_name)
    
    return available_pollutants

def perform_ml_analysis(df, city_name, pollutants):
    """Perform machine learning analysis with chronological train/test split
    
    Args:
        df (pd.DataFrame): DataFrame containing city pollution data with datetime column
        city_name (str): Name of the city being analyzed
        pollutants (list): List of available pollutant column names
        
    Returns:
        dict or None: Dictionary containing model results and data for plotting, or None if analysis fails
            - model: Trained LinearRegression model
            - target: Target pollutant name
            - features: List of feature column names used
            - train_data: Training data DataFrame
            - test_data: Test data DataFrame
            - y_train: Training target values
            - y_test: Test target values
            - y_train_pred: Training predictions
            - y_test_pred: Test predictions
            - test_r2: R² score on test set
            - test_rmse: RMSE on test set
    """
    
    if len(pollutants) < 2:
        return None
    
    if 'datetime' not in df.columns:
        print("No datetime column found for time series analysis")
        return None
    
    # Use PM2.5 as target if available, otherwise first pollutant
    if 'pm2_5' in pollutants:
        target = 'pm2_5'
        features = [p for p in pollutants if p != 'pm2_5' and p in df.columns]
    else:
        target = pollutants[0]
        features = [p for p in pollutants[1:] if p in df.columns]
    
    if not features:
        return None
    
    # Prepare data with datetime
    ml_data = df[['datetime'] + features + [target]].dropna().sort_values('datetime')
    
    if len(ml_data) < 20:
        print(f"Insufficient data for ML analysis ({len(ml_data)} samples)")
        return None
    
    # Time-based split: first 80% for training, last 20% for testing
    split_idx = int(len(ml_data) * 0.8)
    
    train_data = ml_data.iloc[:split_idx]
    test_data = ml_data.iloc[split_idx:]
    
    X_train = train_data[features]
    y_train = train_data[target]
    X_test = test_data[features]
    y_test = test_data[target]
    
    # Train Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Predictions
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    
    # Calculate metrics
    train_r2 = r2_score(y_train, y_train_pred)
    test_r2 = r2_score(y_test, y_test_pred)
    train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
    test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
    
    print(f"\nLinear Regression Analysis for {target.upper()}:")
    print("-" * 50)
    print(f"Features used: {', '.join(features)}")
    print(f"Training period: {train_data['datetime'].min()} to {train_data['datetime'].max()}")
    print(f"Test period: {test_data['datetime'].min()} to {test_data['datetime'].max()}")
    print(f"Training samples: {len(X_train)}")
    print(f"Test samples: {len(X_test)}")
    print(f"Test R²: {test_r2:.3f}")
    print(f"Test RMSE: {test_rmse:.3f}")
    
    # Return data for plotting
    return {
        'model': model,
        'target': target,
        'features': features,
        'train_data': train_data,
        'test_data': test_data,
        'y_train': y_train,
        'y_test': y_test,
        'y_train_pred': y_train_pred,
        'y_test_pred': y_test_pred,
        'test_r2': test_r2,
                 'test_rmse': test_rmse
     }

def create_prediction_plot(ml_results, city_name):
    """Create a plot showing actual vs predicted values with time series
    
    Args:
        ml_results (dict): Dictionary containing ML analysis results from perform_ml_analysis()
        city_name (str): Name of the city being analyzed
        
    Returns:
        None: Displays matplotlib plots
    """
    
    train_data = ml_results['train_data']
    test_data = ml_results['test_data']
    target = ml_results['target']
    y_test = ml_results['y_test']
    y_test_pred = ml_results['y_test_pred']
    test_r2 = ml_results['test_r2']
    test_rmse = ml_results['test_rmse']
    
    plt.figure(figsize=(12, 8))
    
    # Plot actual training data
    plt.subplot(2, 1, 1)
    plt.plot(train_data['datetime'], train_data[target], 'b-', label='Training Data', alpha=0.7)
    plt.plot(test_data['datetime'], y_test, 'g-', label='Actual Test Data', linewidth=2)
    plt.plot(test_data['datetime'], y_test_pred, 'r--', label='Predicted Test Data', linewidth=2)
    plt.title(f'{city_name} - {target.upper()} Prediction (R² = {test_r2:.3f}, RMSE = {test_rmse:.2f})')
    plt.ylabel(f'{target.upper()} (μg/m³)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Plot predicted vs actual scatter plot
    plt.subplot(2, 1, 2)
    plt.scatter(y_test, y_test_pred, alpha=0.6, color='blue')
    
    # Add perfect prediction line
    min_val = min(min(y_test), min(y_test_pred))
    max_val = max(max(y_test), max(y_test_pred))
    plt.plot([min_val, max_val], [min_val, max_val], 'r--', label='Perfect Prediction')
    
    plt.xlabel(f'Actual {target.upper()} (μg/m³)')
    plt.ylabel(f'Predicted {target.upper()} (μg/m³)')
    plt.title(f'Predicted vs Actual - {city_name}')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def visualize_city_trends(df, city_name, pollutants):
    """Create comprehensive visualizations for a city
    
    Args:
        df (pd.DataFrame): DataFrame containing city pollution data
        city_name (str): Name of the city being analyzed
        pollutants (list): List of available pollutant column names
        
    Returns:
        None: Displays matplotlib plots with time series trends for up to 4 pollutants
    """
    
    if not pollutants:
        print(f"No pollutant data available for {city_name}")
        return
    
    # Set up the plot style
    plt.style.use('default')
    sns.set_palette("husl")
    
    # Create figure with subplots
    n_plots = min(len(pollutants), 4)  # Max 4 pollutants per city
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle(f'Luftkvalitet Trender - {city_name}', fontsize=16, fontweight='bold')
    
    axes = axes.flatten()
    
    for i, pollutant in enumerate(pollutants[:4]):
        ax = axes[i]
        
        # Get data for this pollutant
        data = df[pollutant].dropna()
        
        if len(data) == 0:
            ax.text(0.5, 0.5, f'Ingen data for {pollutant}', 
                   ha='center', va='center', transform=ax.transAxes)
            ax.set_title(f'{pollutant.upper()}')
            continue
        
        if 'datetime' in df.columns and len(data) > 1:
            # Time series plot
            valid_data = df[df[pollutant].notna()]
            ax.plot(valid_data['datetime'], valid_data[pollutant], 
                   marker='o', linewidth=2, markersize=4, alpha=0.7)
            ax.set_xlabel('Tid')
            ax.set_ylabel(f'{pollutant.upper()} (μg/m³)')
            ax.tick_params(axis='x', rotation=45)
            
            # Add trend line if enough data
            if len(valid_data) > 2:
                x_numeric = np.arange(len(valid_data))
                z = np.polyfit(x_numeric, valid_data[pollutant], 1)
                p = np.poly1d(z)
                ax.plot(valid_data['datetime'], p(x_numeric), 
                       "--", alpha=0.8, color='red', linewidth=2)
        else:
            # Bar plot if no datetime
            ax.bar(range(len(data)), data, alpha=0.7)
            ax.set_xlabel('Måling nummer')
            ax.set_ylabel(f'{pollutant.upper()} (μg/m³)')
        
        ax.set_title(f'{pollutant.upper()}')
        ax.grid(True, alpha=0.3)
    
    # Hide unused subplots
    for i in range(n_plots, 4):
        axes[i].set_visible(False)
    
    plt.tight_layout()
    plt.show()


def compare_cities(city_data):
    """Compare pollution levels across the three cities
    
    Args:
        city_data (dict): Dictionary with city names as keys and DataFrames as values
        
    Returns:
        None: Displays matplotlib plots and prints summary table comparing cities
    """
    
    
    # Combine all city data
    all_data = []
    for city, df in city_data.items():
        if df is not None:
            df_copy = df.copy()
            df_copy['city'] = city
            all_data.append(df_copy)
    
    if not all_data:
        print("Ingen data tilgjengelig for sammenligning")
        return
    
    combined_df = pd.concat(all_data, ignore_index=True)
    
    # Find common pollutants
    pollutants = ['pm2_5', 'pm10', 'no2', 'o3', 'so2', 'co']
    available_pollutants = []
    
    for pollutant in pollutants:
        if pollutant in combined_df.columns:
            # Check if at least 2 cities have data for this pollutant
            cities_with_data = combined_df.groupby('city')[pollutant].count()
            if (cities_with_data > 0).sum() >= 2:
                available_pollutants.append(pollutant)
    
    if not available_pollutants:
        print("Ingen felles forurensningsdata funnet for sammenligning")
        return
    
    
    # Create comparison plots
    n_pollutants = len(available_pollutants)
    n_cols = min(3, n_pollutants)
    n_rows = (n_pollutants + n_cols - 1) // n_cols
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5*n_rows))
    fig.suptitle('Sammenligning av Luftkvalitet - Utvekslingsbyer', fontsize=16, fontweight='bold')
    
    if n_pollutants == 1:
        axes = [axes]
    elif n_rows == 1:
        axes = axes if n_cols > 1 else [axes]
    else:
        axes = axes.flatten()
    
    for i, pollutant in enumerate(available_pollutants):
        ax = axes[i] if n_pollutants > 1 else axes[0]
        
        # Create boxplot for comparison
        plot_data = []
        plot_cities = []
        
        for city in combined_df['city'].unique():
            city_values = combined_df[combined_df['city'] == city][pollutant].dropna()
            if len(city_values) > 0:
                plot_data.extend(city_values.tolist())
                plot_cities.extend([city] * len(city_values))
        
        if plot_data:
            plot_df = pd.DataFrame({'City': plot_cities, 'Value': plot_data})
            sns.boxplot(data=plot_df, x='City', y='Value', ax=ax)
            ax.set_title(f'{pollutant.upper()}')
            ax.set_ylabel('μg/m³')
            ax.grid(True, alpha=0.3)
            
            # Add mean values as text
            for j, city in enumerate(plot_df['City'].unique()):
                city_mean = plot_df[plot_df['City'] == city]['Value'].mean()
                ax.text(j, ax.get_ylim()[1] * 0.9, f'μ={city_mean:.1f}', 
                       ha='center', va='center', fontweight='bold')
    
    # Hide unused subplots
    if n_pollutants > 1:
        for i in range(n_pollutants, len(axes)):
            axes[i].set_visible(False)
    
    plt.tight_layout()
    plt.show()
    
    # Summary table
    print(f"\nSammendrag (gjennomsnittsverdier i μg/m³):")
    print("-" * 60)
    summary_table = []
    
    for city in combined_df['city'].unique():
        city_data = combined_df[combined_df['city'] == city]
        row = {'City': city}
        for pollutant in available_pollutants:
            values = city_data[pollutant].dropna()
            if len(values) > 0:
                row[pollutant.upper()] = f"{values.mean():.1f}"
            else:
                row[pollutant.upper()] = "N/A"
        summary_table.append(row)
    
    summary_df = pd.DataFrame(summary_table)
    print(summary_df.to_string(index=False))

def main():
    """Main function to run the analysis
    
    Args:
        None
        
    Returns:
        None: Executes complete analysis pipeline for Milano, Grenoble, and København
    """
    
    # Define the three exchange cities
    cities = ['Milano', 'Grenoble', 'København']
    city_data = {}
    
    # Load data for each city
    for city in cities:
        city_data[city] = load_city_data(city)
    
    # Analyze each city separately
    for city in cities:
        if city_data[city] is not None:
            pollutants = analyze_single_city(city_data[city], city)
            visualize_city_trends(city_data[city], city, pollutants)
        else:
            print(f"\nIngen data tilgjengelig for {city}")
    
    # Compare all cities
    compare_cities(city_data)


if __name__ == "__main__":
    main()

