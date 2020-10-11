# CO2-emission-analysis
In this repository, the data of various car companies is analyzed for finding out the factors affecting CO2 emission, top company in terms of CO2 emission and many more key points
The entire process is divided into three main steps:- 1)Dataset Description 2)Data Visualization and 3)prediction of car condition using a suitable model

1) Dataset Description
*This dataset is taken from kaggle.com.
*This dataset is about the CO2 emissions(in g/km) of various Car companies in Canada
*This Dataset contains 7386 rows alongwith 12 columns which are Make,Vehicle class,Engine sze(in L),cylinders,fuel type,transmission,Fuel consumption citywise(in g/100km),Fuel consumption Highway(in g/100km),Fuel consumption Comb(in g/100km),Co2 emission(in g/km),fuel consumption Comb(in mpg) and Model.
* This dataset has no null values.
*It has 6 attributes of cateogorical value and 6 attributes of numerical value.
*Now we proceed towards analysis of this dataset using data visualization.

2) Data Visualization
*for Data Visualisation,Tableau which is popular Business Intelligence tool has been used.
*here i have tried to identify the relationships between various attributes of dataset and predicted some results.
*There are various types of plots used to analyze the data such as Bubble Plots,Waterfall Plots,Bar Plots,Pie Charts etc.
*In order to verify the results predicted by data visualization,A machine learning model has been applied.

3)prediction of car condition
*In this portion a machine learning model has been applied to determine weights and bias values from the given data so that results for unknown values can be determined.
*For applying of model ,first dependent and independent variables are identified which in this dataset are as follows-:

Independent Variables->Engine sze(in L),cylinders,Fuel consumption citywise(in g/100km),Fuel consumption Highway(in g/100km),Fuel consumption Comb(in g/100km)

Dependent variable->,Co2 emission(in g/km)

*for this purpose i have applied Multiple Linear Regression Model which involves following steps-:
