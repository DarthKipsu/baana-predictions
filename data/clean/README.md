### Clean data

Labels file contains counts for cyclist from 1.1.2013 until yesterday. Each day on their seperate row. Actuals file is a temporary file containing the same info collected daily from [InfraControl barometer](http://www1.infracontrol.com/cykla/barometer/barometer_fi.asp?system=helsinki&mode=day).

Data file contains similarly weather data for each day from 1.1.2013 until yesterday. The data in each column is:

- column 0: the amount of rain
- column 1: medium temperature
- column 2: depth of snow (-1 if no snow)
- column 3: minimum temperature
- column 4: maximum temperature

Predictions file lists the predicted cyclist counts since 13Th February 2016. Predictions up until 28Th February 2016 use the older classifier version 2b and since then version 3.
