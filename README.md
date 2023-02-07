# Surfs_Up
Gathering and analysis of weather data for a future surf and scoop shop in Hawaii.

## Overview
Nothing quite like a scoop after hitting the waves! In this analysis we take a look into weather data for a client who seeks to open a surf shop in Hawaii. Using data obtained from mutiple weather stations, we have to take into consideration any biases from this data that may skew our results and work around those to obtain true results! Weather is important as conditions could have an effect on sales and the ideal icecream temperature must be taken into account for supply purposes.

The main goal for our Analysis here is to get temperature data for the months of June and December in Oahu. Once this is obtained, we can determine if the surf and ice cream shop business is sustainable year-round!

## Results
After preparing the data for analysis, we had to runa query in the sqlite database. We were able to filter a specific month and pull that months Temperature data. We then placed it into a list as well as a pandas dataframe. From there we were able to calculate our sumarry of results. The results for each month are as follows:

### June Results
<img width="131" alt="June_Temps" src="https://user-images.githubusercontent.com/18335464/217325459-4c133e27-9600-405d-a968-699d04db0b07.png">


### December Results 
<img width="159" alt="December_Temps" src="https://user-images.githubusercontent.com/18335464/217329312-0bf1f789-08f4-4cde-b8c2-e1da8005cdf3.png">


### Key Differences

* The Minimum temp for June is 64 while december is a staggering 56. This means december will likeley mean much less clients as conditions could be too cold to surf.

* The mean temp is 75 in june. This could impact how long icecream is able to remain outside. the mean temp for December is 71, meaning conditions could be a little more favorable for stock.

* The max temp for both months isn't too far at all (83 and 85). This means things could get hot in these months, this is important to note for supply!

## Summary
We can see differences in these months for Hawaii. This impacts how certain decisions are made going forward. December will be a less favorable month as it has a very cold minimum temperature meaning less surfers. The mean temperatures give us an idea of the average temp for keeping our supply fresh and melt free! The max heat is high in both months and this should be taken into cosideration as heatwaves can strike at any time in Hawaii!

Additional queries that could be run include other data for the month of July and December. For June we can check the Measurement table for prcipitation data to see if rainy weather trends could have an impact on how many guests visit. For December we can filter the data to return the only the last two weeks, to see if Christmas time trends could influence our results for the month!
