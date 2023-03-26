#  Emissions by Country

## 1. *What is it?*
This dataset provides an in-depth look into the global CO2 emissions at the country level, allowing for a better understanding of how much each country contributes to the global cumulative human impact on climate. 
It contains information on total emissions as well as from coal, oil, gas, cement production and flaring, and other sources.   

The data also provides a breakdown of per capita CO2 emission per country - showing which countries are leading in pollution levels and identifying potential areas where reduction efforts should be concentrated. 

This dataset is essential for anyone wanting to get informed about their environmental footprint or research international development trends.  
## 2.  *We need to build an environment*

 1. We need to enter our file 
 ```
    cd Golf 
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
