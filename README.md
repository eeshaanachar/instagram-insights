# Instagram Insights

Instagram Insights is a set of Python web crawlers that can be used to scrape information from the Instagram website.

## Objectives

Even though the bot can be used in other ways, the following objectives were kept in mind during the development:

* Get a list of people that don't follow back an account.
* Get a list of inactive followers of an account.
* Get related hashtags using keyword.

## Setup

* Download chrome driver and place it in the same directory as the scripts.
* Ensure the name of the driver is "chromedriver.exe". On platforms other than Windows, make necessary changes in constructor of ```InstagramBot``` inside ```instagram_bot.py``` file.
* Install the packages listed in requirements.txt using pip3 as follows:

        pip3 install -r requirements.txt

## Usage

The class ```InstagramBot``` defines several methods that can be used to gain valuable insights. The following files demonstrate some of the ways the bot can be used:

* Getting non followers - ```getNonFollowers.py```
* Getting inactive followers - ```getDeadFollowers.py```
* Getting related hashtags - ```downloadHashtags.py``` and ```getCachedHashtags.py```

## Present Scope

* No GUI.
* Significant execution time.
* The individual methods need to be documented.
* "Fragile" code that might break if Instagram updates its website or due to network errors.
