# Created by Alejandro Hernandez, Sept 2020


class GeneBoolean:
    def __init__(self, seq):
        self.sequence = str(seq).upper()                    # read seq argument as a string and set as sequence
        self.sequence = self.sequence.replace("A", "00")    # replace bases into binary representation
        self.sequence = self.sequence.replace("C", "01")
        self.sequence = self.sequence.replace("G", "10")
        self.sequence = self.sequence.replace("T", "11")
        sequence = []                                       # make self.sequence String into list
        index = 0
        while index < len(self.sequence):
            sequence.append(self.sequence[index:index + 6])
            index += 6
        self.sequence = sequence

    def add_marker(self, given_marker):
        for base in given_marker:       # if given marker isn't of bases A, C, G, or T, marker is invalid
            if base == "A" or base == "C" or base == "G" or base == "T": pass
            else:
                return print("Marker is invalid. Cannot add marker '" + str(given_marker) + "'")
        if len(given_marker) != 3 or given_marker == "TAG" or given_marker == "TAA" or given_marker == "TGA":
            return print("Marker is invalid. Cannot add marker '" + str(given_marker) + "'")
        else:   # else marker is valid and inserted
            marker = str(given_marker)
            marker = marker.replace("A", "00")
            marker = marker.replace("C", "01")
            marker = marker.replace("G", "10")
            marker = marker.replace("T", "11")
            self.sequence.insert(-1, marker)

    def base_at(self, base_position):
        if str(base_position).isnumeric():  # check is given position is valid
            if int(base_position) < len(self.sequence)*3:
                target_marker = int(int(base_position) / 3)
                target_base = int(base_position) % 3          # this value will either be 0,1,or 3. See IF block below
                target_marker = self.sequence[target_marker]
                target_base = str(target_base)  # make target_base str b/c later will be converted (binary --> alphabet)
                if target_base == "0":          # this IF block selects 1st,2nd,or 3rd base in target marker
                    target_base = str(target_marker)[0:2]
                elif target_base == "1":
                    target_base = str(target_marker)[2:4]
                else:
                    target_base = str(target_marker)[4:6]
                target_base = target_base.replace("00", "A")    # convert to alphabet and return target base
                target_base = target_base.replace("01", "C")
                target_base = target_base.replace("10", "G")
                target_base = target_base.replace("11", "T")
                return target_base
            else: return "Position " + str(base_position) + " is out of bounds."
        else: return "Position must a positive numeric value."

    def is_potential_gene(self):
        # conduct necessary checks on list sequence
        if self.sequence[0] == "001110" and (self.sequence[-1] == "110010" or self.sequence[-1] == "110000" or
                                             self.sequence[-1] == "111000") is True:
            # check if sequence contains multiple stop markers
            count_of_stop_markers = 0
            if self.sequence.count("110010") == 1: count_of_stop_markers += 1
            if self.sequence.count("110000") == 1: count_of_stop_markers += 1
            if self.sequence.count("111000") == 1: count_of_stop_markers += 1
            return count_of_stop_markers == 1   # is a potential gene
        return False                            # is not a potential gene
    # NOTE: no need to check length of array because
    # if length is not multiple of 3, self.sequence[-1] will not be a stop marker

    def display_statistics(self):
        translated_marker = ""
        sequence = self.sequence
        dictionary = {}
        for marker in sequence:
            dictionary[marker] = round(1000 * self.sequence.count(marker)/len(self.sequence), 1)
        counter = 0
        for marker in dictionary:
            translated_marker = marker      # leave 'marker' alone because it's how I get to that key's value later
            base1 = translated_marker[0:2]  # split markers into bases and manually translate
            if base1 == "00": base1 = "A"
            elif base1 == "01": base1 = "C"
            elif base1 == "10": base1 = "G"
            elif base1 == "11": base1 = "T"
            base2 = translated_marker[2:4]
            if base2 == "00": base2 = "A"
            elif base2 == "01": base2 = "C"
            elif base2 == "10": base2 = "G"
            elif base2 == "11": base2 = "T"
            base3 = translated_marker[4:6]
            if base3 == "00": base3 = "A"
            elif base3 == "01": base3 = "C"
            elif base3 == "10": base3 = "G"
            elif base3 == "11": base3 = "T"

            translated_marker = base1 + base2 + base3
            if counter % 4 == 0 and counter != 0:
                print("")
            print(translated_marker + " " + str(dictionary.get(marker)), end=" ")
            counter += 1
