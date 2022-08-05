
from turtle import hideturtle
import requests
#to import the inbuilt request module  that has been installed in the computer  

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=T6RUC1GIJE0O6U1T'
# get the url to extract data from alphavantage
link = requests.get(url)
# create as a variable inorder to use the json function later to gather data from the api
data = link.json()
# variable is created to use the json() funtion 
def api_function():
    """
    Function is to extract real time currency exchange from USD to SGD from alphavantage.co
    """

    return float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])

forex = api_function()
#equating the creatd API function to a varaible inorder to write lines in the next line of code 

with open("summary_report.txt", "w") as a:
    a.write(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{forex}\n")
    #to append the Real time Currenecy to the csv file created in the other files 

# test 2 