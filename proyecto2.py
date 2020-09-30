# 	{(0,p,p),(0,p,q),(1,p,p),(0,q,r),(1,q,r),(0,r,s),(0,s,s),(1,s,s)}

class State_switch(object):
    def __init__(self, from_node, to_node, input_to_switch):
        self.from_node = from_node
        self.to_node = to_node
        self.input_to_switch = input_to_switch

    def __repr__(self):
        return 'from %s, to %s when %s' % (self.from_node, self.to_node,
                                           self.input_to_switch)

    def __str__(self):
        return 'from %s, to %s when %s' % (self.from_node, self.to_node,
                                           self.input_to_switch)


def input_processing(filename):
    with open(filename, 'r') as input_file:
        line = input_file.readline()
        state_switches_input = line[2:-2].split('),(')
        state_switches = []
        for state_switch in state_switches_input:
            input_to_switch, from_node, to_node = state_switch.split(',')
            state_switches.append(State_switch(from_node, to_node,
                                               input_to_switch))
        return state_switches


def main():
    state_switches = input_processing('input.txt')
    print(state_switches)


if __name__ == "__main__":
    main()
