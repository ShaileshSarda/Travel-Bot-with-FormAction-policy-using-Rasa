
# This bot is based on 'FormAction' where in action file we used FormAction Feature to get slots of data from the user. Store them temporarily and retrive them back.


### 1. Training the NLU model

Training of the NLU model:  

``` python rasa_nlu_model.py ```


### 2. Run the custom action file (FormAction):

''' python actions.py'''

### 3. Training the Rasa Core model: 

1. Start the custom action server by running:  

``` python -m rasa_core_sdk.endpoint --actions actions ```  

2. Open a new terminal and train the Rasa Core model by running:  

``` python dialogue_management_model.py```  



