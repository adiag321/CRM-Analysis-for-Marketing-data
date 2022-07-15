# CRM Analysis for Marketing data

I’m a data analyst, and the Chief Marketing Officer has told me that previous marketing campaigns have not been as effective as they were expected to be. I need to analyze the data set to understand this problem and propose data-driven solutions.

## DATA DESCRIPTION

The dataset for this project is provided by Dr. Omar Romero-Hernandez. It is licensed as CC0: Public Domain, which states, “You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission”

1. ID: Customer’s unique identifier
2. Year_Birth: Customer’s birth year
3. Education: Customer’s education level
4. Marital_Status: Customer’s marital status
5. Income: Customer’s yearly household income
6. Kidhome: Number of children in customer’s household
7. Tennhome: Number of teenagers in customer’s household
8. Dt_Customer: Date of customer’s enrollment with the company
9. Recency: Number of days since customer’s last purchase
10. MntWines: Amount spent on wine in the last 2 years
11. MntFruits: Amount spent on fruits in the last 2 years
12. MntMeatProducts: Amount spent on meat in the last 2 years
13. MntFishProducts: Amount spent on fish in the last 2 years
14. MntSweetProducts: Amount spent on sweets in the last 2 years
15. MntGoldProds: Amount spent on gold in the last 2 years
16. NumDealsPurchase: Number of purchases made with a discount
17. NumWebPurchase: Number of purchases made through the company’s website
18. NumCatalogPurchase: Number of purchases made using a catalog
19. NumStorePurchase: Number of purchases made directly in stores
20. NumWebVisitsMonth: Number of visits to company’s website in the last month
21. AcceptedCmp3: 1 if customer accepted the offer in the 3rd campaign, 0 otherwise
22. AcceptedCmp4: 1 if customer accepted the offer in the 4th campaign, 0 otherwise
23. AcceptedCmp5: 1 if customer accepted the offer in the 5th campaign, 0 otherwise
24. AcceptedCmp1: 1 if customer accepted the offer in the 1st campaign, 0 otherwise
25. AcceptedCmp2: 2 if customer accepted the offer in the 1st campaign, 0 otherwise
26. Response: 1 if customer accepted the offer in the last campaign, 0 otherwise
27. Complain: 1 if a customer complained in the last 2 years, 0 otherwise
28. Country: Customer’s location


The dataset is collected from kaggle - https://www.kaggle.com/datasets/jackdaoud/marketing-data?taskId=2986

## METHODS

1. Data Cleaning:

- There is a space in front of the income’s column name

- There are dollar signs is the values of Income column

- The “Income” column has 23 missing values

- Income’s type is string

- Dt_Customer’s type is string

2. Exploratory Data Analysis (EDA)

- Are there any outliers? How will you wrangle/handle them?

- Are there any useful variables that you can engineer with the given data?

- Do you notice any patterns or anomalies in the data? Can you plot them?


3. Performing Statistical Analysis
4. Data Visualization and Further Analysis
5. Forming Data-Driven Solutions


## Findings:

Patterns:
1. High-Income People
— tend to spend more and purchase more.
— tend to visit the company’s website less frequently than other people.
— tend to has few numbers of purchases made with a discount

2. People having kids at home
— tend to spend less and purchase less.
— tend to has a high number of purchases made with a discount

3. People who purchased with high average order volume
— tend to buy more wines and meat products
— tend to make a high number of purchases made using a catalog
— tend not to visit the company’s website.


Anomalies:
1. Intuitively, I’d think the more complaints a customer has, the less they may spend on our store, but the number of complaints in the last two years has almost no correlation with the total amount spent in the last two years. => After further investigating the data, I found that it is because we only have 20 customers who complained in the last two years, but we have 2200 customers in total. So, because of the imbalanced ratio, they don’t correlate. The customer service department in the company has done a wonderful job in the last two years.


https://towardsdatascience.com/data-science-project-marketing-analytics-data-driven-solutions-72d050084642