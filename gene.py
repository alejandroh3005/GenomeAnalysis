# Created by Alejandro Hernandez, Sept 2020
import sys
from geneString import GeneString
from geneArray import GeneArray
from geneBoolean import GeneBoolean


# test variables
add_test1 = "TGA"   # stop markers
add_test2 = "AAB"   # invalid letter
add_test3 = "AAAA"  # too long marker
add_test4 = "TTT"
add_test5 = "GGG"
base_test1 = -2
base_test2 = 3
base_test3 = 100
base_test4 = 3000
file = open("textfile.txt", "r")

# get genome sequence file (must be a single line file)
try:
    with open(sys.argv[1], "r") as file:
        genome = file.readline()
        print("Using given genome sequence.")
except:
    file = open("textfile.txt", "r")
    genome = file.readline()
    print("Using default genome sequence.\n")
file.close()

# testing GeneString class methods
analyzed_genome = GeneString(genome)
print("Genome sequence '" + genome + "' has been initialized as \n" + str(analyzed_genome.sequence))
print()
analyzed_genome.add_marker(add_test1)
analyzed_genome.add_marker(add_test2)
analyzed_genome.add_marker(add_test3)
analyzed_genome.add_marker(add_test4)
analyzed_genome.add_marker(add_test5)
print()
print("What is base at position " + str(base_test1) + "?")
print(analyzed_genome.base_at(base_test1))
print("What is base at position " + str(base_test2) + "?")
print(analyzed_genome.base_at(base_test2))
print("What is base at position " + str(base_test3) + "?")
print(analyzed_genome.base_at(base_test3))
print("What is base at position " + str(base_test4) + "?")
print(analyzed_genome.base_at(base_test4))
print("Is the current sequence a potential gene? " + str(analyzed_genome.is_potential_gene()))
print()
print("Final genome sequence: \n" + str(analyzed_genome.sequence))
print()
print("Displayed Statistics: ")
analyzed_genome.display_statistics()

print("\n-----------------------------------------------------------------------------------------------------------\n")

# testing Gene Array class methods
analyzed_genome = GeneArray(genome)
print("Genome sequence '" + genome + "' has been initialized as \n" + str(analyzed_genome.sequence))
print()
analyzed_genome.add_marker(add_test1)
analyzed_genome.add_marker(add_test2)
analyzed_genome.add_marker(add_test3)
analyzed_genome.add_marker(add_test4)
analyzed_genome.add_marker(add_test5)
print()
print("What is base at position " + str(base_test1) + "?")
print(analyzed_genome.base_at(base_test1))
print("What is base at position " + str(base_test2) + "?")
print(analyzed_genome.base_at(base_test2))
print("What is base at position " + str(base_test3) + "?")
print(analyzed_genome.base_at(base_test3))
print("What is base at position " + str(base_test4) + "?")
print(analyzed_genome.base_at(base_test4))
print("Is the current sequence a potential gene? " + str(analyzed_genome.is_potential_gene()))
print()
print("Final genome sequence: \n" + str(analyzed_genome.sequence))
print()
print("Displayed Statistics: ")
analyzed_genome.display_statistics()

print("\n-----------------------------------------------------------------------------------------------------------\n")

# testing GeneBoolean class methods
analyzed_genome = GeneBoolean(genome)
print("Genome sequence '" + genome + "' has been initialized as \n" + str(analyzed_genome.sequence))
print()
analyzed_genome.add_marker(add_test1)
analyzed_genome.add_marker(add_test2)
analyzed_genome.add_marker(add_test3)
analyzed_genome.add_marker(add_test4)
analyzed_genome.add_marker(add_test5)
print()
print("What is base at position " + str(base_test1) + "?")
print(analyzed_genome.base_at(base_test1))
print("What is base at position " + str(base_test2) + "?")
print(analyzed_genome.base_at(base_test2))
print("What is base at position " + str(base_test3) + "?")
print(analyzed_genome.base_at(base_test3))
print("What is base at position " + str(base_test4) + "?")
print(analyzed_genome.base_at(base_test4))
print("Is the current sequence a potential gene? " + str(analyzed_genome.is_potential_gene()))
print()
print("Final genome sequence: \n" + str(analyzed_genome.sequence))
print()
print("Displayed Statistics: ")
analyzed_genome.display_statistics()
