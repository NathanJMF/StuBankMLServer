# PredictingUserSpendingML
## Getting Started
### Prerequisites:
* Python 3.6 or later with pipenv
### Set up:
1) Open cmd on the computer the server will be running on
2) Run the command 'ipconfig' and make note of the ipv4 address of the computer for the network both the android 
device and server will be running on.
3) Open the ServerSystem.py file and on line 11 for variable 'host' replace the current ip with the one you made note of
 earlier.
4) Open PredictFutureSpending.java from the android application code base and on line 239 replace the current ip with 
the same one you made note of earlier. (Both the android app and server should have the same ip entered)

If using PyCharm and it doesnt automatically pick up the Pipfile and Pipfile.lock for the pipenv environment then follow these instructions:

5) Go to project interpreter settings in PyCharm
6) Click add
7) Click pipenv interpreter
8) Make sure that you have your base interpreter selected as your python 3.6 or higher install
9) Make sure 'Install packages from pipfile' is checked

If running the project in cmd then follow this:

5) Open cmd
6) cd to the project directory
7) Use the command 'pipenv shell'
8) Once the env is active you can use the command 'python ServerSystem.py' or 'python AdminOptions.py' to run the 
project

## Usage
This project has two python files that are meant to be ran. A server (ServerSystem.py) and an admin specific program
(AdminOptions.py).

Both programs can be ran at the same time if wanted. But for best functionality the server should be running when the
app is in use, while the admin options is optional.

#### ServerSystem.py:
The job of the server is on receive request from the client to read all their transactions, 
using ML predict their future spending and store those predictions in firestore for the client to read.
Once this is done then the server sends a message back to the client telling it so, so that it knows it can read them 
read now.


NOTE: This request is ran when going to the predict future spending page on the app. Although the reading from firebase
only happens after the server has made the update, due to firebase prioritising read speeds over write speeds the client
 may still read and display the old predictions. Backing out of the page and going back to it should then display the
  updated predictions.

#### AdminOptions.py:
The job of AdminOptions.py is to give more functionality to the administrator for machine learning.
When running this application there are 5 main options:
1) Manual update prediction
2) Generate and store new dataset
3) Retrain model and store it
4) Test model
5) Compare model

Manual update prediction allows the admin to enter an email address of a user and run the same update predictions 
collection code the server runs when that receives a request.

Generate and store new data set allows the admin to select one of the 7 categories to generate a new dataset for and 
update that categories respective CSV file.

Retrain model and store it allows the admin to select one of the 7 categories and will read the CSV for that category and
 retrain the linear regression model and restore it.

Test model allows the admin to select one of the 7 categories and will output the % accuracy of the model as well as 
other important constants.

Compare model allows the admin to select one of the 7 categories and will output the predicted values and actual 
values from the test data for comparison.

## Running the project
#### Server:
1) Make sure you have updated the ip address on line 11 in ServerSystem.py and in line 239 of PredictFutureSpending.java
 in the android application so that they are both the ip of the server.
2) In PyCharm right click ServerSystem.py and click Run 'ServerSystem'.

or

2) If using cmd then run the command 'python ServerSystem.py'. (The pipenv environment must be active)

#### Admin:
1) In PyCharm Right click AdminOptions.py and click Run 'AdminOptions'

or

1) If using cmd then run the command 'python AdminOptions.py'. (The pipenv environment must be active)


###### Author: Nathan Fenwick 