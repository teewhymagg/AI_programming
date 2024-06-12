# 22200849
"""
hashmap for menace
access or modification of any state will also modify similar "in terms of being just a rotation
was initially a good idea, but later we found out it has several problems (unsolvable)
"""

# Import necessary libraries
from collections.abc import MutableMapping
import numpy as np
import json
import pickle


# Initialize class Menace with a child class MutableMapping
class Menace(MutableMapping):
    def __init__(self):
        self.menace_dict = {}  # Hash map to store Menace values {hash:weights}
        self.hash_mapping = {}  # Dict to remember which strings got which hashes hash:{set of strings}
        self.full_dict = {}  # Same as previous but to get exact mapping string:hash

    def do_hash(self, state):
        # Function to compute the hash value for a given state
        if state in self.full_dict:
            return self.full_dict[state]
        else:
            hashed = self.hash_function(state)
            for s in self.possible_states(state):
                self.full_dict[s] = hashed
            return hashed
    
    def representative_state(self, equivalent_states):
        # Choose a representative state, for example, the lexicographically smallest one
        return min(equivalent_states)

    def hash_function(self, state):
        # Function to generate a hash value for a given state
        if isinstance(state, int):
            return state
        # Use the representative state to produce a hash value
        out_hash = hash(self.representative_state(self.possible_states(state)))
        self.hash_mapping[out_hash] = self.possible_states(state)
        return out_hash

    def __getitem__(self, state):
        # Get the weights for a given state
        hash_value = self.do_hash(state)
        return self.menace_dict[hash_value]

    def __setitem__(self, state, value):
        # Set the weights for a given state
        hash_value = self.do_hash(state)
        self.menace_dict[hash_value] = value

    def __delitem__(self, state):
        # Delete the weights for a given state
        hash_value = self.do_hash(state)
        del self.menace_dict[hash_value]

    def __iter__(self):
        # Return iterator over keys (hash values)
        return iter(self.menace_dict.keys())

    def __len__(self):
        # Return the number of states in Menace
        return len(self.menace_dict)

    def __contains__(self, state):
        # Check if a state is present in Menace
        hash_value = self.do_hash(state)
        return hash_value in self.menace_dict

    def rotate_clockwise(self, matrix):
        # Rotate a matrix clockwise
        return np.rot90(matrix, k=-1)

    def mirror_horizontal(self, matrix):
        # Mirror a matrix horizontally
        return np.flipud(matrix)

    def mirror_vertical(self, matrix):
        # Mirror a matrix vertically
        return np.fliplr(matrix)

    def string_to_matrix(self, s):
        # Convert a string representation of a state to a matrix
        return np.array(list(s)).reshape(3, 3)

    def matrix_to_string(self, matrix):
        # Convert a matrix representation of a state to a string
        return "".join(matrix.flatten())

    def all_clocks(self, matrix):
        # Generate all possible rotations of a matrix
        matrices = set()
        matrices.add(self.matrix_to_string(matrix))
        orig_matrix = np.copy(matrix)
        for i in range(3):
            orig_matrix = self.rotate_clockwise(orig_matrix)
            matrices.add(self.matrix_to_string(orig_matrix))

        return matrices

    def all_mirrors(self, matrix):
        # Generate all possible mirror configurations of a matrix
        matrices = set()
        matrices.add(self.matrix_to_string(matrix))
        matrices.add(self.matrix_to_string(self.mirror_vertical(matrix)))
        matrices.add(self.matrix_to_string(self.mirror_horizontal(matrix)))
        return matrices

    def all_diagonals(self, matrix):
        # Generate all possible diagonal configurations of a matrix
        matrices = set()
        matrices.add(self.matrix_to_string(matrix))
        matrices.add(self.matrix_to_string(
            np.transpose(matrix)))  # Main diagonal flip
        matrices.add(self.matrix_to_string(
            np.flipud(np.fliplr(matrix))))  # Anti-diagonal
        return matrices

    def possible_states(self, state):
        # Generate all possible configurations of a given state
        state_matrix = self.string_to_matrix(state)
        set_of_states = set()
        set_of_states.add(state)
        clocks = self.all_clocks(state_matrix)  # All rotated versions of state
        mirrors = set()  # All mirrored versions of all rotated versions
        set_of_states.update(clocks)

        array_of_clockwised_sets_matrices = [numpy_matrix for numpy_matrix in map(
            self.string_to_matrix, clocks)]  # Need to mirror all
        array_of_mirrored_matrices = [new_variant_of_state for new_variant_of_state in map(
            self.all_mirrors, array_of_clockwised_sets_matrices)]
        set_of_mirrored_matrices = {
            string for subset in array_of_mirrored_matrices for string in subset}
        mirrors.update(set_of_mirrored_matrices)
        set_of_states.update(mirrors)

        array_of_set_of_states_matrices = [
            numpy_matrix for numpy_matrix in map(self.string_to_matrix, set_of_states)]
        array_of_diagonaled_matrices = [new_variant_of_state for new_variant_of_state in map(
            self.all_diagonals, array_of_set_of_states_matrices)]
        set_of_diagonaled_matrices = {
            string for subset in array_of_mirrored_matrices for string in subset}

        set_of_states.update(set_of_diagonaled_matrices)
        return set_of_states

    @property
    def return_normal_dict(self):
        # Return a normalized dictionary with string keys and corresponding weights
        normal_dict = {}
        for hash_key, hash_values in self.hash_mapping.items():
            for value in hash_values:
                normal_dict[value] = self.menace_dict[hash_key]
        return normal_dict
    
    def read_from_json(self, file_path):
        # Read Menace weights from a JSON file
        print("Reading may take a while, please wait")
        # Reset maps just to be sure
        self.menace_dict = {}
        self.hash_mapping = {}
        self.full_dict = {} 
        with open(file_path, "r") as weights_file:
            temp_dict = json.load(weights_file)
            for key, value in temp_dict.items():
                self.__setitem__(key, value)
        print("Reading done, you can now use AI")
    
    def dump_to_binary_file(self, file_path):
        # Dump Menace instance to a binary file
        with open(file_path, "wb") as dump_file:
            pickle.dump(self, dump_file)
            
    @classmethod
    def read_binary_weights(cls, file_path):
        # Read Menace weights from a binary file
        with open(file_path, 'rb') as read_file:
            return pickle.load(read_file)
        
if __name__ == "__main__":
    m = Menace().read_binary_weights("binary_menace.bin")
    print(m["O_X_X____"])
    print(m.full_dict["O_X_X____"])
    print(m.hash_mapping[m.full_dict["O_X_X____"]])
    print(m.representative_state(m.hash_mapping[m.full_dict["O_X_X____"]]))