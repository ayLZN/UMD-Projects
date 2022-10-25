#Project 1

##Libraries to import

pip install requests
pip install pandas
pip install csv
pip install BeautifulSoup
pip install time
pip install random

##Documentation

This project is a program that reads the CSV file using pandas. I first created a new list to append the lyric URLs from the CSV. I then created another new list to append and hold the lyrics from each URL. Using the python library BeautifulSoup I was able to webscrape the lyrics using regex and performed cleaning techniques. The columns in the dataframe were then zipped and saved into a new CSV.

#Project 2

##Libraries to import

pip install pandas
pip install numpy
pip install sklearn
pip install re
pip install seaborn
pip install matplotlib

##Documentation

Using the new CSV file from previous project, we take preprocessing steps such as cleaning and stemming. Using relplot from the seaborn library to show the song length over the years. The coefficient for year after running linear regression on year and minmax-scaled version of song length was 0.00129637, with this positive number we can say that as the independent variable (year) goes up the mean of the dependent variable (minmax-scaled version of song length) also tends to go up. The coefficient for year after running linear regression on year and minmax-scaled version of unique length was 0.00119658, with this positive number we can say that as the mean of the independent variable (year)goes up the dependent variable (minmax-scaled version of unique length) also tends to go up. The coefficient for year after running linear regression on year and minmax-scaled version of song ratio was -0.0013415, with this negative number we can say that as the independent variable (year) goes up the dependent variable (minmax-scaled version of ratio) also tends to go down. This analysis also shows me that there will likely be increased unique words being used rather than increased song length as the years continue as unique words coefficient is higher (higher level indicator).
