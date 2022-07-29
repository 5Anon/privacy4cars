# Import necessary packages
import pandas as pd
import numpy as np
import pymssql
import FiveAnonPrivacyMetrics

import warnings
warnings.filterwarnings("ignore")

## Load the Historical and Anonymized Datasets
# Note: Make sure your IP Address is Added to the Azure Database
conn = pymssql.connect(server='privacyforcars.database.windows.net',
    user='PfCCAdmin',
    password='PrivacyForConnectedCars101#',
    database='HistoricalDatabase')
data = pd.read_sql('SELECT * FROM dbo.HistoricalDataBase;', con = conn)
AnonData = pd.read_sql('SELECT * FROM dbo.AnonymizerDataset;', con = conn)

## Predefine the Identities, Quasi-Identifiers, and Sensitive Attributes
# Get the vehicle ID's separately
db_identities = ['car_id']
db_vehicle_id_values = data[db_identities]
db_vehicle_id_values = db_vehicle_id_values.drop_duplicates()

# # Identifying Driving Behavior Quasi-Identifiers
db_quasi_identifiers = ["Longitude","Latitude", "GPS_Speed"]
db_quasi_identifier_values = data.groupby(db_quasi_identifiers).size().reset_index().rename(columns={0:'count'})
db_quasi_identifier_values

# # Identifying Driving Behavior Sensitive Attributes
db_sensitive_attributes = ["Speed_GPS_mph"]
db_sensitive_attribute_values = data[db_sensitive_attributes]
db_sensitive_attribute_values

data = data.dropna(subset=db_quasi_identifiers+db_sensitive_attributes)


## Run the Five Anon Privacy Metrics
# Load the Dataset to the Privacy Metrics
anonymizedDataMetrics = FiveAnonPrivacyMetrics.PrivacyMetrics(data)

# Load the Identities, Quasi-Identifiers, and Sentitive Attributes
anonymizedDataMetrics.loadIdentities(db_identities)
anonymizedDataMetrics.loadQuasiIdentifiers(db_quasi_identifiers)
anonymizedDataMetrics.loadSensitiveAttributes(db_sensitive_attributes)

# Run the Privacy Metrics on the Dataset
anonymizedDataMetrics.runPrivacyMetrics()

# Run Privacy Metrics Comparison Against Another Dataset
anonymizedDataMetrics.comparePrivacyMetrics(AnonData)

conn.close()
