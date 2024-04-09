# House Price Prediction

## Summary
The factors that influence actual Sale Price of a house are analysed using Linear Regression, and Regularized using Ridge and Lasso Regression, after which the significant predictor variables and their influence are identified.

## Business Understanding
A US-based housing company named Surprise Housing has decided to enter the Australian market. The company uses data analytics to purchase houses at a price below their actual values and flip them on at a higher price. For the same purpose, the company has collected a data set from the sale of houses in Australia. The company is looking at prospective properties to buy to enter the market. In this project a regression model is built using regularisation in order to predict the actual value of the prospective properties and decide whether to invest in them or not. In addition, the significant variables in predicting the price of a house are identified using Recursive Feature Elimination and how well those variables describe the price of a house is explained.

## Conclusions
- Model built using Lasso Regression regularization gives best results while predicting Sales Price of a house.
- Ten most important features that influence the Sale Price of a house are: 
1.	OverallQual
2.	BsmtFinSF1
3.	OverallCond
4.	2ndFlrSF
5.	MasVnrArea
6.	Neighborhood_Crawfor
7.	TotalBsmtSF
8.	WoodDeckSF
9.	Fireplaces
10.	LotConfig_CulDSac

- Out of these variables, OverallQual, BsmtFinSF1, OverallCond, 2ndFlrSF, TotalBsmtSF, WoodDeckSF, Fireplaces, LotConfig_CulDSac are positively influencing the Sale Price. That's an increase in these variables will also cause an increase in Sale Price of the house.
- However, MasVnrArea, Neighborhood_Crawfor are negatively influencing the Sale Price. That's a decrease in these variables will cause an increase in Sale Price of the house.





