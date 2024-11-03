import numpy as np

class DynamicBayesianNetwork:
    def __init__(self, states, transition_model, emission_model):
        self.states = states
        self.transition_model = transition_model 
        self.emission_model = emission_model     
    def predict(self, current_state):
        probabilities = self.transition_model[current_state]
        next_state = np.random.choice(self.states, p=probabilities)
        return next_state

    def emit(self, current_state):
        probabilities = self.emission_model[current_state]
        observation = np.random.choice(list(probabilities.keys()), p=list(probabilities.values()))
        return observation

if __name__ == "__main__":
    states = ['Rainy', 'Sunny']

    transition_model = {
        'Rainy': [0.7, 0.3],  # Probabilidades de transición a Rainy, Sunny
        'Sunny': [0.4, 0.6]
    }

    emission_model = {
        'Rainy': {'Walk': 0.1, 'Shop': 0.4, 'Clean': 0.5},
        'Sunny': {'Walk': 0.6, 'Shop': 0.3, 'Clean': 0.1}
    }

    dbn = DynamicBayesianNetwork(states, transition_model, emission_model)

    current_state = 'Rainy'
    for _ in range(5): 
        next_state = dbn.predict(current_state)
        observation = dbn.emit(current_state)
        print(f"Estado actual: {current_state}, Estado siguiente: {next_state}, Observación: {observation}")
        current_state = next_state
