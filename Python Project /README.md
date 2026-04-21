                                   ACADEMICTASK-02 INT375 
(Data Science Toolbox - Python Programming Syllabus) 
             COMPUTER SCIENCE AND ENGINEERING 
Submitted by: 
Name: Rizzu Khan 
Registration number: 12417714 
Roll No.: 30 
Section: 224YM 
 
Submitted to: 
Baljinder Kaur 
 
 
 
 
 
 
 
LOVELY PROFESSIONAL UNIVERSITY 
 
 
 
DECLARATION 
 
I, RIZZU KHAN, a student of Bachelor of Technology under CSE discipline at Lovely Professional University, Punjab, hereby declare that all the information furnished in this project report is based on my own work and is genuine  


LinkedInLink: https://www.linkedin.com/feed/update/urn:li:activity:7452388259583668224/ 
GitHub Link:

ACKNOWLEDGEMENT
I would like to express my sincere gratitude to all those who have contributed to the successful completion of this project. This project would not have been possible without the support and guidance of many individuals.
I am especially thankful to my faculty coordinator for their valuable guidance, constant encouragement, and constructive feedback throughout the project. Their knowledge and expertise in Python programming and data analysis helped me understand the concepts effectively.
I would also like to thank the faculty members of the Department of Computer Science and Engineering at Lovely Professional University for providing a supportive academic environment that encouraged learning and innovation.
I am grateful to Lovely Professional University for providing the necessary resources and tools, including Python libraries such as Pandas, NumPy, Matplotlib, and Seaborn, which were essential for completing this project.
I would like to extend my thanks to my classmates and friends for their support and helpful suggestions during the development of this project.
Finally, I express my deepest gratitude to my family for their continuous support, patience, and encouragement throughout my academic journey.
Rizzu Khan
Registration No.: 12417714



TABLE OF CONTENTS
S.No.	Section Title	Page No.
—	Declaration	ii
—	Certificate	iii
—	Acknowledgement	iv
—	Table of Contents	v
 1  Introduction  1 
 1.1  Source of Dataset  2 
 1.2  Exploratory Data Analysis (EDA) Process  3
1.3  Dataset Analysis (Sales, Profit, Region, Category)  4 
| 2 | System Description | 5 |
| 2.1 | General Description | 5 |
| 2.2 | Requirements, Functions and Formulas Used | 6 |
| 2.3 | Analysis Results | 7 |
| 3 | Visualization | 8 |
| 3.1 | Objectives of Visualization | 8 |
| 3.2 | Numeric Prediction using Linear Regression | 9 |
| 3.3 | Conclusion | 10 |
| 3.4 | Future Scope | 11 |
| 4 | References | 12 |

1.Introduction
Retail businesses generate a large amount of data every day, including sales transactions, customer details, product information, and shipping records. Analyzing this data helps organizations understand their performance, identify trends, and make better business decisions.
This project focuses on performing Exploratory Data Analysis (EDA) and Machine Learning (ML) on the Superstore dataset using Python. The main objective is to analyze sales, profit, customer behavior, and regional performance, and to build a predictive model for profit using Linear Regression.
The project aims to extract meaningful insights from the dataset and present them using data visualization techniques.
Project Objectives
• Analyze sales and profit trends across different regions and categories.
• Identify top-performing products, customers, and regions.
• Study the relationship between discount and profit.
• Perform data cleaning and preprocessing for accurate analysis.
• Visualize data using graphs such as bar charts, scatter plots, and heatmaps.
• Build a Linear Regression model to predict profit based on sales and other features.
2.Source of Dataset
Source of Dataset
The dataset used in this project is the Superstore dataset, which is widely recognized in the field of data analytics and business intelligence. It is commonly used for learning and practicing data analysis, visualization, and machine learning techniques due to its structured format and real-world retail context.
The dataset contains detailed transactional records of a retail business, including information about orders, customers, products, sales, profit, and shipping details. It provides a comprehensive view of business operations, enabling analysis of performance across different dimensions such as time, geography, and product categories.
The dataset includes the following key attributes:
• Order ID, Customer Name, and Customer Segment
• Product Category and Sub-Category
• Sales, Quantity, Discount, and Profit
• Region, State, and City
• Order Date and Ship Date
This dataset is publicly available and has been obtained from Kaggle, a widely used platform for data science and machine learning resources. It is frequently used by students and professionals for practicing exploratory data analysis (EDA), visualization, and predictive modeling.
Source Link:
https://www.kaggle.com/code/tarekmasryo/superstore-sales-forecasting/input
3.EDA Process
Exploratory Data Analysis (EDA) is the process of analyzing datasets to summarize their main characteristics and discover patterns before applying machine learning models.
EDA Workflow
1.	Data Loading — Import dataset using Pandas.
2.	Data Inspection — Check shape, columns, data types, and summary statistics.
3.	Data Cleaning — Handle missing values and incorrect data types.
4.	Feature Engineering — Extract Year and Month from Order Date.
5.	Univariate Analysis — Study distribution of Sales, Profit, and Discount.
6.	Bivariate Analysis — Analyze relationships such as Sales vs Profit.
7.	Multivariate Analysis — Use correlation heatmaps for deeper insights.
8.	Business Analysis — Region-wise, category-wise, and customer analysis.
9.	Machine Learning — Build a Linear Regression model for prediction.
10.	Analysis on Dataset
(i) Introduction
The Superstore dataset contains detailed transactional records of a retail business operating across multiple regions. Each row in the dataset represents a single order placed by a customer and includes comprehensive information such as product details, sales amount, quantity purchased, discount applied, and the resulting profit or loss.
In addition to product-level data, the dataset also provides customer-related information including customer name, segment (Consumer, Corporate, or Home Office), and geographic details such as city, state, and region. It also includes time-based attributes like order date and shipping date, which allow for trend analysis over time.
This dataset is highly valuable for business analytics as it helps in understanding customer behavior, identifying profitable products and regions, analyzing the impact of discounts on profitability, and evaluating overall business performance. By using this dataset, various analytical and predictive techniques can be applied to support data-driven decision-making.
(ii) General Description
Column | Data Type | Description
Order ID | String | Unique order identifier
Customer Name | String | Name of customer
Category | String | Product category
Sub-Category | String | Product sub-category
Sales | Float | Sales amount
Quantity | Integer | Number of items sold
Discount | Float | Discount applied
Profit | Float | Profit earned
Region | String | Sales region
Order Date | Date | Date of order
(iii) Data Loading & Cleaning
 The dataset was loaded using Pandas and basic preprocessing steps were applied to ensure data quality.  


  (iv)Remove missing values
 
(v)Outlier Removal using IQR Method
 
This step removes extreme values in the Sales column to improve the accuracy of analysis and machine learning models.

(vi) Feature Engineering / Calculations
      Key business metrics were calculated using the following formulas:
 
These metrics help in understanding overall business performance.
A Linear Regression model was applied to predict Profit based on Sales.
 


Train-test split:
 

Model training:
 


Prediction:
 

Evaluation formulas:
 
These evaluation metrics measure how well the model predicts profit values.
Visualization
Various visualization techniques are used to understand the dataset:
• Bar Charts — Category and Region analysis 

 

• Box Plot — Outlier detection
 




• Scatter Plot — Sales vs Profit relationship
 



 

• Heatmap — Correlation analysis
 

Pie Chart — Category share
 
• Line Chart — Sales trend over time


 

7. Conclusion
This project successfully analyzes retail sales data using Python. The insights obtained help understand business performance, identify key trends, and highlight areas that require improvement. The analysis reveals how different factors such as product category, region, and discount impact overall sales and profitability.The machine learning model provides a reasonable prediction of profit, demonstrating the usefulness of data-driven decision-making. Although the model is relatively simple, it effectively captures the relationship between sales and profit and can be further improved by incorporating additional features.The visualizations created in this project make it easier to interpret complex data patterns and support better business strategies. Overall, this project shows how data analysis and machine learning techniques can be applied to real-world business problems to generate meaningful insights and improve decision-making processes.
8.	Future Scope
Apply advanced machine learning models such as Random Forest, XGBoost, or Gradient Boosting to improve prediction accuracy.Develop an interactive dashboard using tools like Streamlit or Plotly to allow users to explore data dynamically. Integrate real-time sales data to perform live analysis and support real-time business decision-making. Perform customer segmentation using clustering techniques (e.g., K-Means) to identify different customer groups and improve marketing strategies. Include additional features such as product ratings, customer feedback, or seasonal trends to enhance the analysis.Extend the model to forecast future sales and profit using time series techniques.
9.	References

 Kaggle Superstore Dataset — The dataset used in this project was obtained from Kaggle, a widely recognized platform for data science and machine learning resources. It provides real-world retail data suitable for analysis and visualization.
Python Documentation — Official documentation of Python libraries such as Pandas, NumPy, Matplotlib, and Seaborn was used for understanding data manipulation, statistical analysis, and visualization techniques.
Scikit-learn Documentation — Used for implementing machine learning algorithms, particularly Linear Regression, along with model evaluation techniques such as R² score and Mean Squared Error.
 Data Science Tutorials and Online Resources — Various online tutorials, articles, and educational platforms were referred to for guidance on data preprocessing, exploratory data analysis (EDA), and visualization methods.
 Academic and Learning Materials — Course notes and instructional materials provided during the study of data science and Python programming were also utilized to support this project.

