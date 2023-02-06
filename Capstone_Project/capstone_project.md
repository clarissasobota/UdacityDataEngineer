# **Capstone Project - Immigration Data**




## **Initial Data Analysis**


### **airport-codes_csv.csv**
| Column                | Description                                   | Used in Dim Table |
| --------------------  | --------------------------------------------- | :---------------: |
| ident (text)          | Airport identification code                   |        X          |
| type (text)           | Type of airport                               |        X          |
| name (text)           | Name of airport                               |        X          |
| elevation_ft (int)    | Airport elevation                             |                   |
| continent (text)      | Continent                                     |                   |
| iso_country (text)    | Country                                       |        X          |
| iso_region (text)     | Country and region                            |        X          |
| municipality (text)   | City                                          |        X          |
| gps_code (text)       | GPS Code                                      |                   |
| iata_code (text)      | Airport location identifier                   |                   |
| local_code (text)     | Airport code                                  |                   |
| coordinates (text)    | Coordinates                                   |                   |

&nbsp;


### **immigration_data_sample.csv**
| Column                   | Description                                | Used in Dim Table |
| -----------------------  | ------------------------------------------ | :---------------: |
| *null* (int)             | Unique record id                           |        X          |
| cicid (float)            | Immigrant identifier                       |        X          |
| i94yr (float)            | 4 digit year                               |        X          |
| i94mon (float)           | Numeric month                              |        X          |
| i94cit (float)           | Resident origin                            |        X          |
| i94res (text)            | Resident origin                            |        X          |
| i94port (float)          | Arrival port                               |        X          |
| arrdate (float)          | Arrival date in US                         |        X          |
| i94mode (float)          | Mode of travel                             |        X          |
| i94addr (text)           | Address state                              |        X          |
| depdate (float)          | Date departing from US                     |        X          |
| i94bir (float)           | Age of respondent                          |        X          |
| i94visa (float)          | Visa code (visa use)                       |        X          |
| count (float)            | Used for summarizing statistics            |                   |
| dtadfile (int)           | Data dded to files (not used)              |                   |
| visapost (text)          | State where visa was issued (not used)     |                   |
| occup (text)             | Occupation in US (not used)                |                   |
| entdepa (char)           | Arrival flag (not used)                    |                   |
| entdepd (char)           | Departure flag (not used)                  |                   |
| entdepu (text)           | Update flag (not used)                     |                   |
| matflag (char)           | Match flag                                 |                   |
| biryear (float)          | 4 digit year of birth                      |                   |
| dtaddto (int)            | Data admitted to US (not used)             |                   |
| gender (char)            | Sex of non-immigrant                       |        X          |
| isnum (int)              | INS Number                                 |                   |
| airline (text)           | Airline used to arrive in US               |        X          |
| admnum (int)             | Admission number                           |                   |
| fitno (text)             | Flight number                              |                   |
| visatype (text)          | Class of admission for temp state          |        X          |

&nbsp;


### **us-cities-demographics.csv**
| Column                   | Description                                | Used in Dim Table |
| -----------------------  | ------------------------------------------ | :---------------: |
| city (text)              | City in US                                 |        X          |
| state (text)             | State in US                                |        X          |
| median age (float)       | Median age of population                   |        X          |
| male population (int)    | Number of males in population              |        X          |
| female population (text) | Number of females in population            |        X          |
| total population (int)   | Total people in population                 |        X          |
| number of veterans (int) | Veterans in population                     |                   |
| foreign-born (int)       | Number of immigrants                       |        X          |
| avg household size (int) | Average size of household                  |        X          |
| state code (text)        | State abbreviation                         |        X          |
| race (text)              | Race                                       |                   |
| count (int)              | Count of number of race in population      |                   |

&nbsp;

### **GlobalLandTemperatureByCity.csv**
| Column                          | Description                         | Used in Dim Table |
| ---------------------------------  | -------------------------------- | :---------------: |
| dt (date)                          | Date temp taken                  |                   |
| avg temperature (float)            | Average temp                     |        X          |
| avg temperature uncertainty (float)| Accounts for margin of error     |        X          |
| city (text)                        | City                             |        X          |
| country (text)                     | Country                          |        X          |
| latitude (text)                    | Latitude                         |                   |
| longitude (text)                   | Longitude                        |                   |

&nbsp;

## **Data Model**

## *Dimension Tables*

### **airport_codes**
| Column                | Description                                   | 
| --------------------  | --------------------------------------------- | 
| ident (text)          | Airport identification code                   |
| type (text)           | Type of airport                               | 
| name (text)           | Name of airport                               |
| country (text)        | Country                                       |
| state (text)          | State                                         | 
| city (text)           | City                                          | 

&nbsp;

### **global_temps**
| Column                             | Description                      |
| ---------------------------------  | -------------------------------- |
| city (text)                        | City                             |
| country (text)                     | Country                          |
| month (int)                        | Month                            |
| avg temperature (float)            | Average temp                     |
| avg temperature uncertainty (float)| Accounts for margin of error     |


&nbsp;

### **us_cities_demographics**
| Column                   | Description                                |
| -----------------------  | ------------------------------------------ |
| city (text)              | City in US                                 |
| state (text)             | State in US                                |
| median_age (float)       | Median age of population                   |
| male_population (int)    | Number of males in population              |
| female_population (text) | Number of females in population            |
| total_population (int)   | Total people in population                 |
| foreign_born (int)       | Number of immigrants                       |
| avg_household_size (int) | Average size of household                  |
| state_code (text)        | State abbreviation                         |

&nbsp;

### **countries**
| Column                             | Description                      |
| ---------------------------------  | -------------------------------- |
| code (text)                        | Country code                     |
| country (text)                     | Country                          |

&nbsp;

### **ports**
| Column                             | Description                      |
| ---------------------------------  | -------------------------------- |
| code (text)                        | Port code                        |
| port (text)                        | Port                             |
| city (text)                        | City                             |
| state (text)                       | State                            |

&nbsp;

### **states**
| Column                             | Description                      |
| ---------------------------------  | -------------------------------- |
| code (text)                        | State code                       |
| state (text)                       | State                            |

&nbsp;

### **travel_modes**
| Column                             | Description                      |
| ---------------------------------  | -------------------------------- |
| code (text)                        | Travel code                      |
| mode (text)                        | Travel type                      |

&nbsp;

### **visa_use**
| Column                             | Description                      |
| ---------------------------------  | -------------------------------- |
| code (text)                        | Visa code                        |
| visa (text)                        | Visa type                        |

&nbsp;

## *Fact Table*

### **immigrant_data**
| Column                   | Description                                |
| -----------------------  | ------------------------------------------ |
| record_id (int)          | Unique record id                           |
| cicid (int)              | Immigrant identifier                       |
| year (int)               | 4 digit year                               |
| month (int)              | Numeric month                              |
| origin_res (text)        | Resident origin                            |
| port (int)               | Arrival port                               |
| arrdate (float)          | Arrival date in US                         |
| travel_mode (int)        | Mode of travel                             |
| us_state (text)          | Arrival state                              |
| us_city  (text)          | Arrival city                               |
| depdate (float)          | Date departing from US                     |
| age (int)                | Age of respondent                          |
| visa_use (int)           | Visa code (visa use)                       |
| gender (char)            | Sex of non-immigrant                       |
| airline (text)           | Airline used to arrive in US               |
| visa_type (text)         | Class of admission for temp state          |
| city_temp (float)        | Average temp for city in arrival month     |