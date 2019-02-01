# HR-Assist (Read document carefully to perform actions)
# This bot is based on 'FormAction' where in action file we used FormAction Feature to get slots of data from the user. Store them temporarily and retrive them back.


### 1. Training the NLU model

Training of the NLU model:  

``` python nlu_model.py ```


### 2. Run the Weather action file:

''' python actions.py'''

### 3. Training the Rasa Core model: 

1. Start the custom action server by running:  

``` python -m rasa_core_sdk.endpoint --actions actions ```  

2. Open a new terminal and train the Rasa Core model by running:  

``` python dialogue_management_model.py```  

if the error occures like "Addressed is already in Used with some port number like ex. 5055/8000 etc" or CannotListenError: Couldn't listen on 0.0.0.0:8081:Address already in use.
then run:

'''lsof -ti:5055 | xargs kill -9''' # To kill the running port by changing port number



