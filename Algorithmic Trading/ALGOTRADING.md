# StrategiesAnalyzed = 
      {
      # 1 - Equal-Weight S&P 500 Screener 
      # 2 - Quantitative Momentum Screener Strategy
      # 3 - Quantitative Value Screener Strategy
      }

1. Algorithmic Trading Basics
2. API Basics and Course Configuration
3. Project 1
4. Project 2
5. Project 3



1. # ------------------------------------------------------------------------------------------------------------------------

Algorithmic Trading Means using Computer to make Investment Decisions.
# In the Past: Analyzer Team
# Now: More Computers Than Humans

There are many different types of Algorithmic trading.
The main difference is their speed of execution.

Main Players in the Algorithmic trading Landscape:
----------------------------------------------------------------------------
# Renaissance Technologies $165B in AUM 50% | Year for 20 Years -> Founded by a Phd Student
# AQR Capital Management $61B in AUM
# Citadel Securities: $32B in AUM High Frequency Trading

AlgoTrading With Python:
Python is the #1 most popular language for algorithmic trading. Quantitative Finance.
+ A lot of libraries
- Python is slow
Solution: Is often used as Glow to trigger code that runs in other languages
Common Example: NumPy -> The most popular python Library for Performing numerical Computing
Although its written for use in Python, its underlying functionalities are written in C.

The Algorithmic Trading Process:
The Process of running a quantitative investing Strategy can be broken down into the following steps:
1. Collect Data
2. Develop a Hypothesis for a strategy
3. Backtest that strategy (Could work with past data?)
4. Implement the strategy in production (real money)

NOT COVERING: AKA CHECK: WORKS WITH REAL DATA? WORKS WITH REAL TRADES? WE WILL OUTPUT AN EXCEL DOCUMENT, ORDER SHEETS.




2. # ------------------------------------------------------------------------------------------------------------------------

API Basics and Course Configuration
API: Application Programming Interface
USe API to interact with someone else software

Examples here will be with IEX Cloud API to gather stock market data to make investment decisions.

# GET -> Gather Data 
# POST -> Add Data to the DB
# PUT -> Add/Modify/Overwrite Data on the DB
# DELETE -> Delete Data from the API's DB




3. # ------------------------------------------------------------------------------------------------------------------------
# PROJECT 1:
Equal Weight S&P 500 Screener
# ---------------------------------------------
The World Most Popular Stock Market Index
Many Investment funds are benchmarked to the S&P 500.
This means that they seek to replicate the performance of this index by owning all the stock that are held by the Index.

500 Largest company in US. One of the most important characteristics of the S&P 500 is that is is market capitalization-weighted (Size-Large Company).
This means that larger companies get a correspondingly larger weight in the index.
In this project, each company in the S&P 500 has the same weight.



4. # ------------------------------------------------------------------------------------------------------------------------
# PROJECT 2:
Quantitative Momentum Screener
# ---------------------------------------------
Momentum Investing means investing in assets that have increased in price the most.
That means if for example a Stock had a higher return over last year, Momentum investing would suggest to invest on that stock over a second which would have less return.

There are many over nuances to momentum investing strategies.
High Quality Momentum - EX.



5. # ------------------------------------------------------------------------------------------------------------------------
# PROJECT 3:
Quantitative Value Screener
# ---------------------------------------------
Value Investing means investing in stocks that are trading below their perceived intrinsic value.
Value investing was popularized by investors like Warren Buffett, Seth Klarman, and Benjamin Graham 

Creating algorithmic value investing strategies relies on a concept called:
# Multiples
Which are simply how investors estimate how valuable a company is.
Multiples are calculated by dividing a Company's stock price by some measures of the company's worth-like earnings or assets.
# Some Examples Are:
- Price - to - earnings
(Divide Company's Stock Price by Earnings per Share)
- Price - to - book - value
(Divide Company's Stock Price by its Book Value per Share)
- Price - to - free - cash flow
(Divide Company's by its Free Cash FLow per Share)

Each of the individual multiples used by value investors has its pros and cons.
One Way to minimize the impact of any specific Multiple is by using a:
# Composite
Which is a Average of many different Value Strategies (We gonna analyze 5 different value Metrics)

