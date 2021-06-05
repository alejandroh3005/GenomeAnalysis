# Created by Alejandro Hernandez, Sept 2020


class GeneString:
    def __init__(self, sequence):
        self.sequence = str(sequence).upper()

    def add_marker(self, marker):
        # if given marker is not of bases A, C, G, or T, marker is invalid
        for base in marker:
            if base == "A" or base == "C" or base == "G" or base == "T":
                pass
            else:
                return print("Marker is invalid. Cannot add marker '" + str(marker) + "'")
        if len(marker) != 3 or marker == "TAG" or marker == "TAA" or marker == "TGA":
            print("Marker is invalid. Cannot add marker '" + marker + "'")
        else:   # if marker is valid, insert given marker before last marker
            self.sequence = self.sequence[0:-3] + marker + self.sequence[-3:len(self.sequence)]

    def base_at(self, base_position):
        if 0 <= int(base_position) < len(self.sequence):
            return str(self.sequence[base_position])
        else: return "Position " + str(base_position) + " is out of bounds."

    def is_potential_gene(self):
        # conduct necessary checks on String sequence
        if(len(self.sequence) % 3 == 0 and self.sequence.startswith("ATG")
                and (self.sequence.endswith("TAG") or self.sequence.endswith("TAA") or
                     self.sequence.endswith("TGA")) is True):
            # check if sequence contains multiple stop markers
            # split sequence into a String list of 3 bases/letters
            markers = []
            index = 0
            while index < len(self.sequence):
                markers.append(self.sequence[index:index+3])
                index += 3
            # check if more than one stop marker is in markers[] using a count variable
            count_of_stop_markers = 0
            if markers.count("TAG") == 1: count_of_stop_markers += 1
            if markers.count("TAA") == 1: count_of_stop_markers += 1
            if markers.count("TGA") == 1: count_of_stop_markers += 1
            return count_of_stop_markers == 1
        return False

    def display_statistics(self):
        dictionary = {}
        markers = []
        index = 0
        while index < len(self.sequence):                   # make list of sequence
            markers.append(self.sequence[index:index + 3])
            index += 3
        for marker in markers:  # add dictionary element {marker: marker freq per thousand with one decimal place}
            dictionary[marker] = round(1000 * markers.count(marker)/len(markers), 1)
        counter = 0
        for marker in dictionary:
            if counter % 4 == 0 and counter != 0:
                print("")
            print(str(marker) + " " + str(dictionary.get(marker)), end=" ")
            counter += 1
