#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 11:06:14 2018

@author: Gowtham shankar Gowri Shankar
"""

class StockAnalysis:
    """
    This class contains the instances variables, getter and setter methods needed for
    the Stock Market analysis application
    """
    def __init__(self,stockTicker = "",firstTicker = "",secondTicker = "",startDate="",endDate="",closingDate=""):
        self.__stockTicker = stockTicker
        self.__firstTicker = firstTicker
        self.__secondTicker = secondTicker
        self.__startDate = startDate
        self.__endDate = endDate
        self.__closingDate = closingDate
            
    def getStockTicker(self):
        return self.__stockTicker
     
    def getFirstTicker(self):
        return self.__firstTicker
     
    def getSecondTicker(self):
        return self.__secondTicker
     
    def getStartDate(self):
        return self.__startDate

    def getEndDate(self):
        return self.__endDate

    def getClosingDate(self):
        return self.__closingDate      
         
