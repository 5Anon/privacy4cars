# 5-Anon 
5 -Anon is an end-to-end software development kit for data privacy. It consists of 3 libraries. These 3 libraries work together to provide a comprehensive data anonymization capabilities.
- Parameterization processor - This library is to be used with server components along with raw data storage. Its purpose is to identify the best anonymization technique to be scripted to achieve required probability of disclosure. Scripts created by this processor are utilized by Anonymization processor library.
- Anonymization processor - This library executes on the edge and applies the scripts created by the first library on the raw data that is generated on the edge device. APIs in this library are dependent upon the user’s preferences,  Output of this library is the anonymized data. Once anonymized data is uploaded to the server for storage.
- Privacy Analyzer - This library provides methods that can performs privacy analysis on a dataset and provide the probability of attribute, information and membership disclosures.

# API
## Privacy Metrics API
### k_Anonymity
	k_Anonimity method helps in determining the probability of information disclosure. k-Anonymity is referred to as the power of "hiding in the crowd". A dataset is k-anonymous if quasi-identifers for each person in the dataset are identical to at least k-1 other people also in the dataset. k-Anonymity address the risk of re-identification of anonymized data through linkage to other datasets.
	
	```tuple<kvalue, equivalence_classes> k_Anonymity(data)

	Input: data input to this api is the dataset
	Output: a tuple containing k-anonymity value and the equivalence classes satifying that anonymity
	```

# Usecase: Data Privacy for connected vehicles
Automobile manufacturers are re-inventing themselves and becoming more like software driven companies. Connected vehicles, as these new generations of vehicles are called, collect data by design about the car, driver, ride, and its surroundings. According to AAA, an average connected vehicle could generate 380 TB to 5100 TB of data in just one year while driving 17,600 minutes on average. 

Connected vehicles collect data by design about the vehicle, driver, driving dynamics, and its surroundings. Data collection is not clearly mentioned to the users upon vehicle purchase. To make matters worse, vehicle manufacturers do not easily allow customers the flexibility and control over data collection measures. So, what options do drivers have to protect their privacy? What can vehicle manufacturers do to raise confidence in vehicle owners about the data custody that they have?

This repository contains the library and application that car manufacturers can use to integrate kep privacy compliance options into their cars. Car manufacturers will have the capability to update the anonymization lambdas at anypoint of time.


![Library Usage in privacy compliance for connected cars](./images/Libraryusage.PNG?raw=true)
