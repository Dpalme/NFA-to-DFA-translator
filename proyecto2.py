# 	{(0,p,p),(0,p,q),(1,p,p),(0,q,r),(1,q,r),(0,r,s),(0,s,s),(1,s,s)}
from collections import defaultdict


class State_switch(object):
    def __init__(self, from_node, to_node, input_symbol):
        self.from_node = from_node
        self.to_node = to_node
        self.input_symbol = input_symbol

    def __repr__(self):
        return 'from %s, to %s when %s' % (self.from_node, self.to_node,
                                           self.input_symbol)

    def __str__(self):
        return 'from %s, to %s when %s' % (self.from_node, self.to_node,
                                           self.input_symbol)


def center_string(text, space):
    spaces = " "*int((space-len(text))/2)
    return "%s%s%s" % (spaces, text, spaces)


def transition_table(table, nodes, alphabet, space):
    table_header = " "*space
    for letter in alphabet:
        table_header += center_string(letter, space)
    print(table_header)
    for node, letters in table.items():
        table_entry = node + " "*(space-len(node))
        for letter, transitions in letters.items():
            table_entry += center_string(str(transitions), space)
        print(table_entry)


def join_states(table, nodes, alphabet):
    while True:
        node_length = len(nodes)
        for node, letters in table.copy().items():
            for letter, transitions in letters.items():
                trans_string = str(sorted(transitions)).replace("'", '')
                if len(transitions) > 1 and trans_string not in nodes:
                    table[trans_string] = {letter: [] for letter in alphabet}
                    nodes.append(trans_string)
                    for node_2 in transitions:
                        for letter in alphabet:
                            if letter in table[node_2]:
                                for node_3 in table[node_2][letter]:
                                    table[trans_string][letter].append(node_3)
                                    table[trans_string][letter] = list(dict.fromkeys(table[trans_string][letter]))
        if node_length == len(nodes):
            break
    return table, nodes


def input_processing(filename):
    nodes = []
    alphabet = []
    table = defaultdict(dict)
    with open(filename, 'r') as input_file:
        line = input_file.readline()
        state_switches_input = line[2:-2].split('),(')
        state_switches = []
        for state_switch in state_switches_input:
            input_symbol, from_node, to_node = state_switch.split(',')
            if input_symbol not in alphabet:
                alphabet.append(input_symbol)
            if from_node not in nodes:
                nodes.append(from_node)
            if to_node not in nodes:
                nodes.append(to_node)
            state_switches.append(State_switch(from_node, to_node,
                                               input_symbol))
        for node in nodes:
            for letter in alphabet:
                to_states = []
                for state in state_switches:
                    if node == state.from_node and letter == state.input_symbol:
                        if state.to_node not in to_states:
                            to_states.append(state.to_node)
                table[node][letter] = to_states
        return table, nodes, alphabet


def main():
    filename = input('filename: ')
    table, nodes, alphabet = input_processing(filename)
    dfa_states, nodes = join_states(table, nodes, alphabet)
    transition_table(dfa_states, nodes, alphabet, 25)
    # transition_table(dfa_states)


if __name__ == "__main__":
    main()
