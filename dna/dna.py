import re
import csv
from sys import argv

def main():
    
    # if an incorrect number of cmd-lines are typed in then exit the program altogether
    if len(argv) != 3:
        print("Invalid number of cmd-lines")
        exit(1)

    # large or small csv file
    if re.search("large", argv[1]):
        iteration = 8
    else:
        iteration = 3

    # open the .csv file and then read it into the var called csv_file
    with open(argv[1]) as file:
        csv_file = csv.reader(file)

        # after the csv file, the text file is also opened and read into the var text_file
        with open(argv[2]) as text:
            sequence = text.readline().rstrip("\n")

            # check which database is being accessed
            if iteration == 8: 
                
                AGATC = count_str("AGATC", sequence)
                TTTTTTCT = count_str("TTTTTTCT", sequence)
                TCTAG = count_str("TCTAG", sequence)
                AATG = count_str("AATG", sequence)
                GATA = count_str("GATA", sequence)
                TATC = count_str("TATC", sequence)
                GAAA = count_str("GAAA", sequence)
                TCTG = count_str("TCTG", sequence)
                
                # Create CSV formatted list
                list_str = [AGATC, TTTTTTCT, AATG, TCTAG, GATA, TATC, GAAA, TCTG]
                
            else:
            
                AGATC = count_str("AGATC", sequence)
                AATG = count_str("AATG", sequence)
                TATC = count_str("TATC", sequence)
                
                # Create CSV formatted list
                list_str = [AGATC, AATG, TATC]


            counter = 1
            found = False
            
            # Look for name of person in CSV file
            for person in csv_file:
                if person[0] != "name":
                    while counter <= iteration:
                        if list_str[counter - 1] == int(person[counter]):
                            found = True
                        else:
                            found = False
                            counter = 1
                            break

                        counter += 1

                    counter = 1

                    if found == True:
                        print(person[0])
                        exit(0)
    print ("No match")
    print (iteration)

# Count the number of STR
def count_str(c, s):
    l = rf'({c})\1*'
    str_list = re.compile(l)
    found = [found for found in str_list.finditer(s)]
    max = 0
    for i in range(len(found)):
        if found[i].group().count(c) > max:
            max = found[i].group().count(c)
    return max

main()

