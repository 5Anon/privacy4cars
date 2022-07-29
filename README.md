# 5-Anon 
5 -Anon is an end-to-end software development kit for data privacy. It consists of 3 libraries. These 3 libraries work together to provide a comprehensive data anonymization capabilities.
- **Parameterization processor** - This library is to be used with server components along with raw data storage. Its purpose is to identify the best anonymization technique to be scripted to achieve required probability of disclosure. Scripts created by this processor are utilized by Anonymization processor library.
- **Anonymization processor** - This library executes on the edge and applies the scripts created by the first library on the raw data that is generated on the edge device. APIs in this library are dependent upon the user’s preferences,  Output of this library is the anonymized data. Once anonymized data is uploaded to the server for storage.
- **Privacy Analyzer** - This library provides methods that can performs privacy analysis on a dataset and provide the probability of attribute, information and membership disclosures.

# Anonymizer Processor API
### Anonymizer()
Anonymizer API anonymizes input dataset resulting in an anonymized dataset

```
anonymized_dataset Anonymizer(preferences, anonymization_parameters, raw_dataset)

Input:	preferences
		anonymization_parameters
		raw_dataset

Output: anonymized_dataset

Example:
	k_anon, l_diversity = runPrivacyMetrics(dataframeObj)

```

# Privacy Analyzer API
### runPrivacyMetrics()
runPrivacyMetrics helps in determining both K Anonimity and L-Diversity of the given dataset. 

```
tuple<kvalue, ldiversity> runPrivacyMetrics(data)

Input: data - input to this api is the dataset for which k-anonymity and l-diversity values 
			  are to be determined
Output: a tuple 
			k-anonymity value 
			l-diversity value
Example:
	(k_anon, l_diversity) = runPrivacyMetrics(dataframeObj)

```

### k_Anonymity()
k_Anonimity method helps in determining the probability of information disclosure. k-Anonymity is referred to as the power of "hiding in the crowd". A dataset is k-anonymous if quasi-identifers for each person in the dataset are identical to at least k-1 other people also in the dataset. k-Anonymity address the risk of re-identification of anonymized data through linkage to other datasets.
	
```
(kvalue, equivalence_classes) k_Anonymity(data)

Input: data - input to this api is the dataset
Output: a tuple 
			k-anonymity value 
			equivalence classes satifying the anonymity value
Example:
	(k_anon, eq) = k_Anonymity(dataframeObj)
```

### Distinct_L_Diversity()
Distinct_L_Diversity method determines entropy l-diversity and distinct l-diversity. l-Diversity is the probability of sensitive attribute disclosures.

```
(lvalue, equivalence_classes) Distinct_L_Diversity(data):
Input: data - input to this api is the dataset
Output: a tuple 
			lvalue - distinct l-diversity value
			equivalence classes satifying the l-diversity value
Example:
	(lvalue, eq) = Distinct_L_Diversity(dataframeObj)
```

# Usecase: Data Privacy for connected vehicles
Automobile manufacturers are re-inventing themselves and becoming more like software driven companies. Connected vehicles, as these new generations of vehicles are called, collect data by design about the car, driver, ride, and its surroundings. According to AAA, an average connected vehicle could generate 380 TB to 5100 TB of data in just one year while driving 17,600 minutes on average. 

Connected vehicles collect data by design about the vehicle, driver, driving dynamics, and its surroundings. Data collection is not clearly mentioned to the users upon vehicle purchase. To make matters worse, vehicle manufacturers do not easily allow customers the flexibility and control over data collection measures. So, what options do drivers have to protect their privacy? What can vehicle manufacturers do to raise confidence in vehicle owners about the data custody that they have?

This repository contains the library and application that car manufacturers can use to integrate kep privacy compliance options into their cars. Car manufacturers will have the capability to update the anonymization lambdas at anypoint of time.


![Library Usage in privacy compliance for connected cars](./images/Libraryusage.PNG?raw=true)

## Webservice API(s)

### Get Parameterization Vector API

**Request**
```	
	GET /api/pv

	Example:
	curl -i -H http://localhost:3999/api/pv
```

**Response**
```
	HTTP/1.1 200 OK
	Date: Thu, 28 Jul 2022 12:36:30 GMT
	Status: 200 OK
	Connection: close
	Content-Type: application/json
	Content-Length: 2

	[]
```

### Anonymized Data Upload API
**Request**
```	
	POST /api/upload

	Example:
		curl -i -H http://localhost:3999/api/upload -d "my data"

		curl -i -H http://localhost:3999/api/upload -d "anonymized dataframe"
```

**Response**
```
	HTTP/1.1 200 OK
	Date: Thu, 28 Jul 2022 12:36:30 GMT
	Status: 200 OK
	Connection: close

	------------------------------------
	HTTP/1.1 404 Not Found
	Date: Thu, 28 Jul 2022 12:36:30 GMT
	Status: 404 Not Found
	Connection: close
	Content-Type: text/html;charset=utf-8
	Content-Length: 35
	
	{"status":404,"reason":"Not found"}

```