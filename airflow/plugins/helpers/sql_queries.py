us_cities_demo_create = """CREATE TABLE us_cities_demographics (
city text,
state text,
median_age double precision,
male_population int,
female_population int,
total_population int,
vertagan_numbers int,
foreign_borns int,
avarage_household_size double precision,
state_code text,
race text,
population_count int
)
"""

us_accidents_create = """CREATE TABLE us_accident (
ID text PRIMARY KEY,
Source text,
TMC float,
Severity int,
Start_Time date,
End_Time date,
Start_Lat double precision,
Start_Lng double precision,
End_Lat double precision,
End_Lng double precision,
Distance double precision,
Description text,
Number float,
Street text,
Side text,
City text,
County text,
State text,
Zipcode text,
Country text,
Timezone text,
Airport_Code text,
Weather_Timestamp date,
Temperature float,
Wind_Chill float,
Humidity float4,
Pressure float4,
Visibility float4,
Wind_Direction text,
Wind_Speed float4,
Precipitation float4,
Weather_Condition text,
Amenity bool,
Bump bool,
Crossing bool,
Give_Way bool,
Junction bool,
No_Exit bool,
Railway bool,
Roundabout bool,
Station bool,
Stop bool,
Traffic_Calming bool,
Traffic_Signal bool,
Turning_Loop bool,
Sunrise_Sunset text,
Civil_Twilight text,
Nautical_Twilight text,
Astronomical_Twilight text
)
"""


us_cities_demo_copy = """COPY us_cities_demographics
FROM 'data/us-cities-demographics.csv' DELIMITER ';' csv
"""

us_accidents_copy = """COPY us_accident
FROM 'data/US_Accidents_Dec19.csv' DELIMITER ',' csv
"""


create_tables_queue = [us_accidents_create, us_cities_demo_create]
copy_tables_queue = [us_cities_demo_create, us_accidents_copy]




