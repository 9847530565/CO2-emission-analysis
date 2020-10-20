# CO2-emission-analysis
## packages used-Numpy,Pandas,Sklearn,tkinter,seaborn
## tool for data visualization- Tableau
## language- Python
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
I->Test Train data splitting
*the entire dataset is divided into two parts which are test data and train data.
*The data with the help of which model is created is called train data and the data by which accuracy of model is checked is called test data.
*generally the size of train data must be smaller than test data.so for that purpose, I have taken 20% of data as training data and 80% of data as testing data.
*Now the model is created using train data.

II->Model creation and accuracy 
*Since there are more than one independent variable and one dependent variable as well as dataset is smaller in size so Multiple Linear Regression Model is effecient itself.
*after generating the model and predicting the result using this model we get a value of 249.29248476641845g/km CO2 emissions with Rsquare value of 0.8808767275286365 on train data.
* then we applied the same on test data and we achieved resultant of 250.433816742409g/km CO2 emissions with Rsquare value of 0.8783545840264559.
*clearly the value of Rsquare for testing data is less than training data by a very small difference of 0.3 approx ,so the results are acceptable and model can be trusted.

#SVM Model
*In order to improve the accuracy SVR Model ie Support Vector Regressor model has been applied.
*This model works on the concept of margin,kernel,gamma and C.
*after applying SVR model accuracy on testing dATA increased to 91%.
