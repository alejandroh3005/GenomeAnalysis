# Created by Alejandro Hernandez, Sept 2020


class GeneArray:
    def __init__(self, sequence):
        sequence = str(sequence).upper()
        self.sequence = []
        index = 0
        while index < len(sequence):
            self.sequence.append(sequence[index:index + 1])
            index += 1

    def add_marker(self, marker):
        # if given marker is not of bases A, C, G, or T, then marker is invalid
        for base in marker:
            if base == "A" or base == "C" or base == "G" or base == "T":
                pass
            else:
                return print("Marker is invalid. Cannot add marker '" + str(marker) + "'")
        if len(marker) != 3 or marker == "TAG" or marker == "TAA" or marker == "TGA":
            print("Marker is invalid. Cannot add marker '" + marker + "'")
        else:   # if marker is valid, remove last marker, add new marker, add last marker
            last_marker = self.sequence.pop()
            last_marker += self.sequence.pop()
            last_marker += self.sequence.pop()
            new_marker = marker[0] + marker[1] + marker[2]
            self.sequence += new_marker
            self.sequence += last_marker

    def base_at(self, base_position):
        if 0 <= int(base_position) < len(self.sequence):
            return self.sequence[base_position]
        else: return "Position " + str(base_position) + " is out of bounds."

    def is_potential_gene(self):
        if len(self.sequence)%3 == 0:
            temp_sequence = []          # create temp list of 3 bases per element
            index = 0
            while index < len(self.sequence):
                temp_sequence.append(self.sequence[index] + self.sequence[index+1] + self.sequence[index+2] )
                index += 3
            # conduct necessary checks on temp list sequence
            if ((temp_sequence[-1] == "TAG" or temp_sequence[-1] == "TAA" or temp_sequence[-1] == "TGA") is True) and\
                    temp_sequence[0] == "ATG":
                # check if temp sequence contains multiple stop markers
                count_of_stop_markers = 0
                if temp_sequence.count("TAG") == 1:
                    count_of_stop_markers += 1
                if temp_sequence.count("TAA") == 1:
                    count_of_stop_markers += 1
                if temp_sequence.count("TGA") == 1:
                    count_of_stop_markers += 1
                return count_of_stop_markers == 1   # is a potential gene
            return False                            # is not a potential gene
        return False

    def display_statistics(self):
        dictionary = {}
        markers = []  # create temp list of 3 bases per element
        index = 0
        while index < len(self.sequence):
            markers.append(self.sequence[index] + self.sequence[index + 1] + self.sequence[index + 2])
            index += 3
        for marker in markers:  # add dictionary element {marker: marker freq per thousand with one decimal place}
            dictionary[marker] = round(1000 * markers.count(marker)/len(markers), 1)
        counter = 0
        for marker in dictionary:
            if counter % 4 == 0 and counter != 0:
                print("")
            print(str(marker) + " " + str(dictionary.get(marker)), end=" ")
            counter += 1
