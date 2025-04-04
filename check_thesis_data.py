# -*- coding: utf-8 -*-
"""check_thesis_data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1klOYa8u5zeNay5YeFTjlZIaZgcY-7tEx
"""

import numpy as np
import pandas as pd
import lightgbm as lgm
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
import gc

import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

"""## Read accepted file



"""

import pandas as pd

# Initiate an empty list to store sliced dataframes (chunks)
myList = []

# Specify the chunksize
chunksize = 10000
pd.set_option('display.float', '{:.2f}'.format)
pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 50)

# Read the CSV file in chunks
for chunk in pd.read_csv('/content/drive/MyDrive/file_sieu_nang/file_new_chinh.csv', chunksize=chunksize):
    myList.append(chunk)

# Concatenate the chunks together
data = pd.concat(myList, axis=0)

# Display the DataFrame to verify
print(data.head())

data_cleaned = data.dropna(axis=1)
null_counts = data_cleaned.isnull().sum()
null_counts

selected_columns = [
    'loan_amnt', 'term', 'int_rate', 'installment', 'grade', 'emp_length',
    'home_ownership', 'annual_inc', 'loan_status', 'dti', 'open_acc',
    'pub_rec', 'revol_bal','revol_util','total_acc','mort_acc','pub_rec_bankruptcies','application_type','purpose'
]
data1 = data_cleaned[selected_columns]

#chuyển đổi non-numerical value
data1 = pd.get_dummies(data1, columns=['term', 'grade', 'emp_length', 'home_ownership','application_type','purpose'])

data1.head()

data1 = data1.applymap(lambda x: 0 if x is True else (1 if x is False else x))

plt.figure(figsize=(8, 6))
sns.countplot(x='loan_status', data=data1)
plt.title('Phân phối biến mục tiêu (loan_status)')
plt.show()

# Convert all columns to numeric, forcing non-numeric values to NaN
data1 = data1.apply(pd.to_numeric, errors='coerce')

data1.head()

correlation_matrix = data1.corr()
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(correlation_matrix['loan_status'].sort_values(ascending=False))

numeric_data1 = data1.select_dtypes(include=['number'])
plt.figure(figsize=(12, 8))
sns.heatmap(numeric_data1.corr(), annot=True, cmap='viridis')

corr_matrix = numeric_data1.corr()

# Plot heatmap of the correlation matrix (optional)
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='viridis')
plt.show()

# Define a threshold for highly correlated features
threshold = 0.8

# Create a list of highly correlated feature pairs
high_corr_pairs = [(corr_matrix.columns[i], corr_matrix.columns[j], corr_matrix.iloc[i, j])
                   for i in range(len(corr_matrix.columns))
                   for j in range(i+1, len(corr_matrix.columns))
                   if abs(corr_matrix.iloc[i, j]) > threshold]

# Display the highly correlated feature pairs
print("\nHighly correlated feature pairs (threshold = 0.8):")
for pair in high_corr_pairs:
    print(f"{pair[0]} and {pair[1]}: {pair[2]:.2f}")

import pandas as pd
import hvplot.pandas

# Example DataFrame, replace with your actual DataFrame loading code


# Creating histograms
installment_plot = data_cleaned.hvplot.hist(
    y='installment', by='loan_status', subplots=False,
    width=350, height=400, bins=50, alpha=0.4,
    title="Installment by Loan Status",
    xlabel='Installment', ylabel='Counts', legend='top'
)

loan_amnt_plot = data_cleaned.hvplot.hist(
    y='loan_amnt', by='loan_status', subplots=False,
    width=350, height=400, bins=30, alpha=0.4,
    title="Loan Amount by Loan Status",
    xlabel='Loan Amount', ylabel='Counts', legend='top'
)

# Displaying the plots
installment_plot + loan_amnt_plot

pd.set_option('display.max_columns', None)

accepted_file['loan_status'].unique()

"""pick some of the most relevant features


"""

accepted_file['loan_status'].value_counts()

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer

# Preprocess the data
# Ensure all categorical variables are strings
for column in accepted_file.select_dtypes(include=['object']).columns:
    accepted_file[column] = accepted_file[column].astype(str)

# Separate numerical and categorical columns
num_cols = accepted_file.select_dtypes(include=['float64', 'int64']).columns
cat_cols = accepted_file.select_dtypes(include=['object']).columns

# Impute missing values for numerical columns
num_imputer = SimpleImputer(strategy='mean')
accepted_file[num_cols] = num_imputer.fit_transform(accepted_file[num_cols])

# Impute missing values for categorical columns
cat_imputer = SimpleImputer(strategy='most_frequent')
accepted_file[cat_cols] = cat_imputer.fit_transform(accepted_file[cat_cols])


# Encoding categorical variables
label_encoders = {}
for column in accepted_file.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    accepted_file[column] = le.fit_transform(accepted_file[column])
    label_encoders[column] = le

# Define features and target
X = accepted_file.drop('loan_status', axis=1)  # Adjust 'Loan_Status' to your target variable
y = accepted_file['loan_status']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a Random Forest model
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Extract feature importances
importances = rf.feature_importances_
feature_names = X.columns

# Create a DataFrame for visualization
feature_importances = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
feature_importances = feature_importances.sort_values(by='Importance', ascending=False)

# Select the most relevant features
top_features = feature_importances.head(10)['Feature']

# Compute the correlation matrix for top features
corr_matrix = df[top_features].corr()

# Plot the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix of Top Features')
plt.show()

plt.figure(figsize=(12, 8))
sns.heatmap(accepted_file.corr(), annot=True, cmap='viridis')

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

sns.heatmap(accepted_file.corr() ,cmap='cubehelix_r')

"""## Read rejected file






"""

import pandas as pd

# Initiate an empty list to store sliced dataframes (chunks)
myList = []

# Specify the chunksize
chunksize = 10000

# Read the CSV file in chunks
for chunk in pd.read_csv('/content/drive/MyDrive/file_sieu_nang/rejected_2007_to_2018Q4.csv', chunksize=chunksize):
    myList.append(chunk)

# Concatenate the chunks together
rejected_file = pd.concat(myList, axis=0)

# Display the DataFrame to verify
print(rejected_file.head())

df = pd.read_parquet('train_data_0.pq')
df.dtypes.value_counts()
np.iinfo(np.int16)

df.head()