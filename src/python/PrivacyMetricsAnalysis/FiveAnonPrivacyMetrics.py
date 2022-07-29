import pandas as pd
import numpy as np

class PrivacyMetrics():

  def __init__(self,data):
    # Get the vehicle ID's separately
    self.data = data
  
  def loadIdentities(self,db_identities):
    self.identities = db_identities
    db_vehicle_id_values = self.data[self.identities]
    db_vehicle_id_values = db_vehicle_id_values.drop_duplicates()
    
  
  def loadQuasiIdentifiers(self, db_quasi_identifiers):
    # # Identifying Driving Behavior Quasi-Identifiers
    self.quasi_identifiers = db_quasi_identifiers
    db_quasi_identifier_values = self.data.groupby(self.quasi_identifiers).size().reset_index().rename(columns={0:'count'})
    db_quasi_identifier_values
    self.data = self.data.dropna(subset=self.quasi_identifiers)

  def loadSensitiveAttributes(self, db_sensitive_attributes):
    # # Identifying Driving Behavior Sensitive Attributes
    self.sensitive_attributes = db_sensitive_attributes
    db_sensitive_attribute_values = self.data[self.sensitive_attributes]
    db_sensitive_attribute_values
    self.data = self.data.dropna(subset=self.sensitive_attributes)

  # k-Anonymity function
  def k_Anonymity(self, data):
    # Get quasi_identifiers data only
    qi_data = data[self.quasi_identifiers]

    # Get list of EC (equivalence classes) and associated counts for each EC
    equivalece_classes = data.groupby(self.quasi_identifiers).size().reset_index().rename(columns={0:'count'})

    # Get lowest EC class count = k
    k = min(equivalece_classes['count'])
    return k, equivalece_classes
  
  # entropy l-diversity and distinct l-diversity function
  def Distinct_L_Diversity(self, data):
    # Get list of EC and associated counts for each EC
    equivalece_classes = data.groupby(self.quasi_identifiers).size().reset_index().rename(columns={0:'count'})
    equivalece_classes['DistinctL'] = np.nan
    
    # Iterate through each EC
    for index, eqv_class_id in equivalece_classes.iterrows():
      # take the quasi_identifier data seperately
      eqv_class = eqv_class_id[self.quasi_identifiers]
      temp = data[self.quasi_identifiers].copy() == eqv_class 
      relevant_data = data[((temp).all(axis=1))]
      
      # extract out the sensitive and find the counts of each unique set of sensitive attributes
      sensitive_values_from_ec = relevant_data[self.sensitive_attributes]
      l_distinct = sensitive_values_from_ec.groupby(self.sensitive_attributes).size().reset_index().rename(columns={0:'count'})

      # Get the lowest senstive attribute count = l
      equivalece_classes.loc[index,'DistinctL'] = min(l_distinct['count'])
    return equivalece_classes
  
  def runPrivacyMetrics(self):
    print("Running Privacy Metrics! ...\n")

    anonData = self.data.copy()
    k_anon_before,quasi_ident = self.k_Anonymity(anonData)
    print("\n\nDataset has a K-Anonymity of ",k_anon_before,"\n")

    anonData2 = anonData.copy()
    equiv_class = self.Distinct_L_Diversity(anonData2)
    print("Dataset has a Distinct L-Diversity",
          min(equiv_class["DistinctL"]) ,
          "for the following Sensitive Attributes: \n"+
          str(self.sensitive_attributes),"\n\n")

  def comparePrivacyMetrics(self, newData):
    print("\n\nComparing Privacy Metrics! ...\n")

    anonData = self.data.copy()
    k_anon,quasi_ident = self.k_Anonymity(anonData)
    print("Original dataset has a K-Anonymity of ",k_anon)

    newAnonData = newData.copy()
    newK_anon,newQuasi_ident = self.k_Anonymity(newAnonData)
    print("New dataset has a K-Anonymity of ",newK_anon,'\n\n')

    anonData2 = anonData.copy()
    equiv_class = self.Distinct_L_Diversity(anonData2)
    print("Original dataset has a Distinct L-Diversity",
          min(equiv_class["DistinctL"]),
          "for the following Sensitive Attributes: \n"+
          str(self.sensitive_attributes))
    
    newAnonData2 = newAnonData.copy()
    newEquiv_class = self.Distinct_L_Diversity(newAnonData2)
    print("New dataset has a Distinct L-Diversity",
          min(newEquiv_class["DistinctL"]),
          "for the following Sensitive Attributes: \n"+
          str(self.sensitive_attributes),"\n\n")