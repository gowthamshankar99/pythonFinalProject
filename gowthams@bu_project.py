"""
Created on Sun Apr 22 19:42:50 2018

@author: Gowtham
"""

import requests
import sys
import datetime
from StockAnalysis import StockAnalysis


API_KEY = '9cjx6en2H1_XFehNXrGx'

def getStockValue(tickerName):
    """
    Description : Get Stock Value based on tickerName value
    """
    r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + stockTicker + '&apikey=' + API_KEY)
    if r.status_code == 200:
        result = ""
        for key, value in r.json()['Time Series (Daily)'].items():
            print("The current stock price of {} is {}".format(stockTicker,value['4. close']))
            result = "The current stock price of {} is {}".format(stockTicker,value['4. close'])
            break
    return result

def getStockValueOnTimeFrame(startDate, endDate, stockTicker):
    """
    Description : Get Stock Value on certain Time frame based on the start date and end date entered in
    """    
    r = requests.get('https://www.quandl.com/api/v1/datasets/WIKI/' + stockTicker + '.json?column=4&sort_order=asc&collapse=daily&trim_start='+ startDate +'&trim_end=' + endDate + '&api_key=' + API_KEY)
    if r.status_code == 200:
        # Iterate through the list
        avg = 0.0
        results = ""
        for list1 in r.json()['data']:
            avg = avg + (float)(list1[1])
        print("Average stock price for {} in the specifed timeframe is {}".format(stockTicker,round(avg/len(r.json()['data']),2)))
        results = "Average stock price for {} in the specifed timeframe is {}".format(stockTicker,round(avg/len(r.json()['data']),2))
        return results
    else:
        results = ""
        print("Issue calling the web service app")    
    return results

def getStockPriceOnSpecificDate(stockTicker,closingDate):
    """
    Description : Get stock price on a specific mentioned Date
    """  
    r = requests.get('https://www.quandl.com/api/v1/datasets/WIKI/' + stockTicker + '.json?column=4&sort_order=asc&collapse=daily&trim_start='+ closingDate +'&trim_end=' + closingDate + '&api_key=' + API_KEY)
    if r.status_code == 200:
        avg = 0.0
        if not r.json()['data']:
            print("Unfortunately the selected Date falls on a Saturday/Sunday.\nThe Stock Market is Open Monday - Friday!")

        else:

            # Iterate through the list
            
            for list1 in r.json()['data']:
                avg = avg + (float)(list1[1])

            print('Stock Price on the specified Date was ' + (str)(avg))
    return (str)(avg)

def getStockPriceOnSpecificDate2Aletered(stockTicker,closingDate):
    """
    Description : Get stock price on a specific mentioned Date
    """ 
    r = requests.get('https://www.quandl.com/api/v1/datasets/WIKI/' + stockTicker + '.json?column=4&sort_order=asc&collapse=daily&trim_start='+ closingDate +'&trim_end=' + closingDate + '&api_key=' + API_KEY)
    if r.status_code == 200:
        avg = 0.0
        if not r.json()['data']:
            newClosingDate = getNextDate(closingDate)
            newClosingDateString = (str)(newClosingDate)
            newClosingDateString = newClosingDateString[:10]
            avg = getStockPriceOnSpecificDate2Aletered(stockTicker,newClosingDateString)
        else:

            # Iterate through the list
            
            for list1 in r.json()['data']:
                avg = avg + (float)(list1[1])
    return (str)(avg)    

def stockAnalysisComparison(firstTicker,SecondTicker):
    """
    Description : Compare One stock with another to find which one is a better buy
    """ 
    # do the one year 
    #oneYearAnalysis(firstTicker,SecondTicker)
    getTheDates = getDates()
    getDatesList = getTheDates.split("!!")

    endDate = getDatesList[0]
    startDate = getDatesList[1]
    stockProceFirstTicker = getStockPriceOnSpecificDate2Aletered(firstTicker,startDate)

    stockProceFirstTickerEndDate = getStockPriceOnSpecificDate2Aletered(firstTicker,endDate)

    percentageDifference1 = calcPercentageDifference(stockProceFirstTickerEndDate,stockProceFirstTicker)
    
    
    stockProceSecondTicker = getStockPriceOnSpecificDate2Aletered(SecondTicker,startDate)
    
    stockProceSecondTickerEndDate = getStockPriceOnSpecificDate2Aletered(SecondTicker,endDate)
    percentageDifference2 = calcPercentageDifference(stockProceSecondTickerEndDate,stockProceSecondTicker)
    
    print("Considering the last one year DATA, Please find the below analysis.\n\n")
    
    if percentageDifference1 > 0:
        print("{} has INCREASED by {} %".format(firstTicker,round(percentageDifference1,2)))
    else:
        print("{} has DECREASED by {} %".format(firstTicker,round(percentageDifference1,2)))
        
    if percentageDifference2 > 0:
        print("{} has INCREASED by {} %".format(SecondTicker,round(percentageDifference2,2)))
    else:
        print("{} has DECREASED by {} %".format(SecondTicker,round(percentageDifference2,2)))        

    if percentageDifference1 > percentageDifference2:
        print("Based on the above Data ,  {} is a better buy than {}".format(firstTicker,SecondTicker))
    else:
        print("Based on the above Data ,  {} is a better buy than {}".format(SecondTicker,firstTicker))
    return

def oneYearAnalysis(firstTicker,secondTicker):
    """
    Description : Get the dates and do one year analysis of stock
    """ 
    getTheDates = getDates()
    getDatesList = getTheDates.split("!!")

    endDate = getDatesList[0]
    startDate = getDatesList[1]

    r = requests.get('https://www.quandl.com/api/v1/datasets/WIKI/' + firstTicker + '.json?column=4&sort_order=asc&collapse=daily&trim_start='+ startDate +'&trim_end=' + endDate + '&api_key=' + API_KEY)
    if r.status_code == 200:
        avg = 0.0
        for list1 in r.json()['data']:
            avg = avg + (float)(list1[1])
        print("Average stock price for {} for One year timeframe is {}".format(firstTicker,round(avg/len(r.json()['data']),2)))        

    return
    
def getDates():
    """
    Description : Get date from dated one year back
    """ 
    d = datetime.date.today()
    today = datetime.date.today()
    today3 = today.replace(day=30)
    today2 = today3.replace(month=today3.month-1)

    yearbackDate = today2.replace(d.year-1)
    return (str)(today2)+"!!"+ (str)(yearbackDate)


def getNextDate(dateObject):
    """
    Description : Get Previous day's Date
    """ 
    GetNextDate = datetime.datetime(*[int(item) for item in dateObject.split('-')])
    getNextDate2 = GetNextDate.replace(day=GetNextDate.day-1)
    return getNextDate2


def calcPercentageDifference(currentValue,oldValue):
    """
    Description : Calculate percentage from current stock value to old value
    """ 
    return ((((float)(currentValue))*100)/(float)(oldValue))-100
    


def writeToFiles(content):
    """
    Description : Get contents to a file.
    """ 
    newFile = open('results.txt','w')
    newFile.write(content)
    newFile.close()
    print('File written successfully. Please check the results.txt file')
    return


    
if __name__ == "__main__":
    

    print("************* Welcome to Stock Analysis Application ********************")

    print("            ******* What do you want to do here ? *******             ")
    
    while True:
        
        print("\n\n1. Get the current stock Price.")
        print("2. Average stock price in a certain Timeframe." )
        print("3. Compare Two stocks to find which is a better buy.")
        print("4. Get Stock closing price on a certain date.")
        print("5. Exit\n")

        inputValue = input('Please Enter [1-5] based on the above questions.')
        

        if (inputValue == "1" or inputValue == "2" or inputValue == "3" or inputValue == "4" or inputValue == "5"):
            if (int)(inputValue) == 1:
                stockTicker = input('Enter the stock Ticker value Ex. AAPL : ')
                # create a stock analysis object
                stockAnalysisObj = StockAnalysis(stockTicker)            
                #get the Stock price value
                result = getStockValue(stockAnalysisObj.getStockTicker())
                yesOrNo = input('Do you want to write the results to a file?')
                if (yesOrNo == "Yes" or yesOrNo == "Y" or yesOrNo == "y" or yesOrNo == "YES"):
                    writeToFiles(result)
                else:
                    print('Results were NOT written to the File')
            elif (int)(inputValue) == 2:

                stockTicker = input('Enter the stock Ticker value Ex. AAPL : ')
                startDate = input('Enter the start Date( Format - YYYY-MM-DD ): ')
                endDate = input('Enter the end Date( Format - YYYY-MM-DD ): ')
                # create a stock analysis object
                stockAnalysisObj = StockAnalysis(stockTicker,"","",startDate,endDate)  
                result = getStockValueOnTimeFrame(stockAnalysisObj.getStartDate(),stockAnalysisObj.getEndDate(), stockAnalysisObj.getStockTicker())            
                if result != "":
                    yesOrNo = input('Do you want to write the results to a file?')
                    if (yesOrNo == "Yes" or yesOrNo == "Y" or yesOrNo == "y" or yesOrNo == "YES"):
                        writeToFiles(result)
                    else:
                        print('Results were NOT written to the File')
            elif (int)(inputValue) == 3:
                firstTicker = input('Enter the first Stock Ticker : ')
                secondTicker = input('Enter the second Stock Ticker : ')
                # create a stock analysis object
                stockAnalysisObj = StockAnalysis("",firstTicker,secondTicker)
                stockAnalysisComparison(stockAnalysisObj.getFirstTicker(),stockAnalysisObj.getSecondTicker())
            elif (int)(inputValue) == 4:
                stockTicker = input('Enter the stock Ticker value Ex. AAPL : ')
                closingDate = input('Enter the date to retrieve the closing Date( Format - YYYY-MM-DD ): ')
                # create a stock analysis object
                stockAnalysisObj = StockAnalysis(stockTicker,"","","","",closingDate)            
                getStockPriceOnSpecificDate(stockAnalysisObj.getStockTicker(), stockAnalysisObj.getClosingDate())
            elif (int)(inputValue) == 5:
                sys.exit()    
            else: 
                print("Invalid Entry")
        else:
                print("Invalid Entry!!")