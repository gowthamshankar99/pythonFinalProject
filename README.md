								Gowtham Shankar Gowri Shankar		 		

Summary
STOCK MARKET ANALYSIS APPLICATION

Objective : 

The objective of this application is to analysis the stock price of any publicly owned company. Below are the specific offerings of this application.

a.	Get the current Stock price of any publicly owned company 
b.	Compare the stock price of two organizations.
c.	Get Average Stock Price of a Share in a certain timeframe.
d.	Get Closing Stock Price of any public company on a certain Date.

How did I accomplish this ?

The application calls a QUANDL REST API(stock market REST API) using an API key that was generated. Depending on the options selected and user input, the data will be sent to the API as part of the URL parameters and response are returned in the form of JSON ( dictionary format). 

Additional data manipulation/massaging/calculations are done based on the option selected.

Dependencies:

This Application calls an external REST API , hence it is dependent on an external python module called “requests”. Other than that, it is also dependent on sys, datetime modules.

Description:

Option A: Get the current Stock price of any publicly owned company.
For Option A and B – results can be written to a text file(results.txt) on request.
Input Parameter : Stock Ticker Name ( Example : AAPL, GOOG)

Description : This option allows the user to get the stock price of any company in the share market. 
	
Example:  Please find the below screenshot for the sample run.
 


Option B: Get the Average stock price of a company in a certain Timeframe. For Option A and B – results can be written to a text file(results.txt) on request.

Input parameter : Stock Ticker Name, Start Date, End Date
Additional Information: Date needs to be in YYYY-MM-DD format

Description : This option consolidates all the stock closing price of each and every day between the selected Time frame and finds the average price of the stock.

Example : Please find the screenshot below for the sample run.

 
Option C: Compare two stocks and find which is a better buy
Input parameter : First Stock Ticker Name, Second Stock Ticker Name 

Description : This option compares two stock and analysis which stock is a better buy. This consolidates the high , low prices of the two stocks in the last one year and calculates the percentage in differences and compares to one another to find the better stock.

Example : Please find the screenshot below for the sample run.


 


Option D: Get the stock closing price on a certain Date.
Input parameter : Stock Ticker Name, Closing Date
Additional Information: Date needs to be in YYYY-MM-DD format

Description : This option compares takes the date inputted and gets that respective closing Date stock Price. The application is intelligent enough to find if the Date falls on a Saturday/Sunday or on a Federal holiday.

Example : Please find the screenshot below for the sample run.
