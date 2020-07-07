# Instagram Insights
Instagram Insights is a set of Python web crawlers / bots to help you with acing your Instagram.

### Objectives
* Get hashtags related to given keyword.
* Get the list of inactive followers.
* Get the list of people that don't follow back.

### Libraries
* time
* random
* pandas==1.0.5
* PyAutoGUI==0.9.50
* selenium==3.141.0

### Setup
* Download chrome driver and place it in the same directory as the scripts.
* Rename chrome driver to "chromedriver.exe" (If not Windows, make necessary changes in script).
* Create a folder called "cache" in the same directory.
* Add your username and password in place of "rms13607" and "imsosorry" throughout the scripts.

### Present Scope
* No GUI.
* Significant execution time; Can be made faster through threading.
* "Fragile" code i.e. can break if Instagram changes the structure of its website.
* "Unrefined" code.