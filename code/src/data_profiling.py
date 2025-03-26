import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df:any
def load_data(file_path):
    """Load data from a CSV file."""
    data = pd.read_csv(file_path)
    df=data
    return data

def generate_summary(data):
    """Generate statistical summary of the data."""
    summary = data.describe(include='all')
    return summary

def visualize_data_distribution(data, column):
    """Visualize the distribution of a specific column in the data."""
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], kde=True)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

def profile_data(file_path):
    """Load data and generate profiling report."""
    data = load_data(file_path)
    summary = generate_summary(data)
    return summary, data


        
def validate_transaction_amount(row):
    if row['Currency']!='USD':
        return abs(row['Transaction_Amount']-row['Reported_Amount'])<=0.01*row['Transaction_Amount']
    return row['Transaction_Amount']==row['Reported_Amount']
    
def validate_account_balance(row):
        if 'OD' in row and row['OD']=='Y':
            return True
        return row['Account_Balance']>=0
    
def validate_currency(row):
        validate_currencies=['USD','EUR','GBP']
        return row['Currency'] in validate_currencies
    
def validate_country(row):
        valid_countries=['US','DE','UK']
        return row['Country'] in valid_countries
    
def validate_transaction_date(row):
        return pd.to_datetime(row['Transaction_Date'])<=pd.Timestamp.today()
    
def validate_risk_score(row):
        return row['Risk_Score']<=10
    

    
def visualize_all_columns(data):
    """Visualize distributions for all numeric columns in the data."""
    numeric_columns = data.select_dtypes(include=['number']).columns
    # for column in numeric_columns:
    #     visualize_data_distribution(data, column)
    data['Transaction_Amount_Valid']=data.apply(validate_transaction_amount,axis=1)
    data['Account_Balance_Valid']=data.apply(validate_account_balance,axis=1)
    data['Currency_Valid']=data.apply(validate_currency,axis=1)
    data['Country_Valid']=data.apply(validate_country,axis=1)
    data['Transaction_Date_Valid']=data.apply(validate_transaction_date,axis=1)
    data['Risk_Score_Valid']=data.apply(validate_risk_score,axis=1)
    data['OD Flag']=~data.apply(validate_account_balance,axis=1)
# st.write('Validate Results')
# st.dataframe(df)