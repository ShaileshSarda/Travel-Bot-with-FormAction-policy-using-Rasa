from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import rasa_core
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
from rasa_core.run import serve_application
from rasa_core import config
from rasa_core.policies.form_policy import FormPolicy


logger = logging.getLogger(__name__)

def train_dialogue(domain_file = 'domain.yml',
					model_path = './models/dialogue',
					training_data_file = './data/stories.md'):
					
	agent = Agent(domain_file, policies = [MemoizationPolicy(), KerasPolicy(max_history=5, epochs=100, batch_size=25),  FormPolicy()])
	data = agent.load_data(training_data_file)	
	

	agent.train(data)
				
	agent.persist(model_path)
	return agent
	
if __name__ == '__main__':
	train_dialogue()
