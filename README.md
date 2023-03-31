
#  Emissions by Country

## 1. *What is it?*
This dataset provides an in-depth look into the global CO2 emissions at the country level, allowing for a better understanding of how much each country contributes to the global cumulative human impact on climate. 
It contains information on total emissions as well as from coal, oil, gas, cement production and flaring, and other sources.   


## 2.  *## Do the set up work*
1. We need to enter our file 
 ```
 cd GroupProject
``` 
 2. via the terminal and execute these commands:
 ```
    pyenv local 3.10.7 # this sets the local version of python to 3.7.0
    python3 -m venv .venv # this creates the virtual environment for you
    source .venv/bin/activate # this activates the virtual environment
    pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.
```
 3. We install that with
 ```
    pip install django
```
 4. And that will install Django version 3.1.3 (or newer) with its associated dependencies. we can start to create the site using the Django admin tools.
 ```
    django-admin startproject mysite .
```
## 3.   *Start the Server*
We do this using the manage.py  command tool by entering this command in the terminal:
```
    python3 manage.py runserver
```

If you're doing this on another platform, then you might need to use this instead (change the port number from 8000 as required):
```
    python3 manage.py runserver 0.0.0.0:8000 
```

If it went well, then you should see the python rocket launching your site.
## 4.   *What you can do with this application*

You can view global CO2 emissions for each country so that you can better understand the extent to which each country contributes to the cumulative global human impact on the climate. 

It contains information on total emissions as well as from coal, oil, gas, cement production and combustion and other sources
1. We have a page for home, country data, and values.
2. You can go through country data to see each country
3. You can go through values to see total emissions and information on coal, oil, gas, cement production and combustion and other sources.
## 5. Background

The data is come from kaggle:
**[link(https://www.kaggle.com/datasets/thedevastator/global-fossil-co2-emissions-by-country-2002-2022)]**
## 6.Contributing
Contributions are welcome! Please fork this repository and submit a pull request.
## 7.  License
This project is licensed under the MIT License. See the file for more information.`LICENSE`
