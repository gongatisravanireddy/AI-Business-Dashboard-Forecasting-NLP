\# AI Business Dashboard with Forecasting \& NLP Insights



\## Project Overview



AI Business Dashboard is a Flask-based business analytics application that analyzes sales and customer review data to provide useful business insights.



The system combines data cleaning, KPI analysis, sales forecasting, and NLP-based sentiment analysis in a single dashboard.



\## Key Features



\- Sales data analysis

\- Data cleaning and preprocessing

\- Business KPI calculation

\- Revenue and profit analysis

\- Month-over-Month growth analysis

\- Top product and region identification

\- Sales forecasting using ARIMA

\- Forecast evaluation using MAE and MAPE

\- Customer review sentiment analysis

\- Positive, Negative, and Neutral sentiment classification

\- Automated business insights

\- Interactive web dashboard



\## Technologies Used



\- Python

\- Flask

\- Pandas

\- Statsmodels

\- Scikit-learn

\- NLTK

\- VADER Sentiment Analysis

\- HTML



\## Machine Learning \& NLP Techniques



\### Sales Forecasting



The project uses the ARIMA (AutoRegressive Integrated Moving Average) model to forecast future monthly sales.



\### Evaluation Metrics



The forecasting model is evaluated using:



\- Mean Absolute Error (MAE)

\- Mean Absolute Percentage Error (MAPE)



\### Sentiment Analysis



Customer reviews are analyzed using the VADER sentiment analysis technique.



The system classifies customer reviews into:



\- Positive

\- Negative

\- Neutral



\## Business KPIs



The dashboard calculates important business metrics such as:



\- Total Revenue

\- Total Profit

\- Profit Margin

\- Month-over-Month Growth

\- Top Performing Product

\- Highest Sales Region



\## Automated Business Insights



The system generates insights based on:



\- Revenue and profit performance

\- Monthly business growth

\- Top-performing products

\- Top-performing regions

\- Forecasted sales

\- Customer sentiment



\## Project Structure



```text

AI-Business-Dashboard/

│

├── backend/

│   ├── data\_cleaning.py

│   ├── forecasting\_engine.py

│   ├── insight\_generator.py

│   ├── kpi\_engine.py

│   └── nlp\_engine.py

│

├── data/

│   ├── reviews\_data.csv

│   └── sales\_data.csv

│

├── templates/

│   └── dashboard.html

│

├── app.py

├── create\_reviews\_data.py

├── create\_sales\_data.py

├── test\_forecast.py

├── test\_insights.py

├── test\_kpi.py

├── test\_nlp.py

├── requirements.txt

├── .gitignore

└── README.md

