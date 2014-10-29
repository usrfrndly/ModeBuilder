"""

Jaclyn Horowitz
Music Software 2014
"""
import csv
import this

csv_list = []
mode_names = ('Ionian', 'Dorian', 'Phrygian', 'Lydian', 'Mixolydian', 'Aeolian', 'Locrian', 'Ionian')

# Change csv file to be compared to here
with open('pythag_sheet_phase3.csv', 'rU') as my_file:
    reader = csv.reader(my_file, skipinitialspace=True, delimiter=',', quoting=csv.QUOTE_NONE)
    # Skip all empty rows
    # for row in reader:
    row_count = 0
    cell_count = None
    found = False
    for row in reader:
        newrow = []
        if not found:
            cell_count = 0
        for cell in row:
            if cell == 'c':
                newrow.append(cell)
                found = True
            else:
                if cell != '':
                    newrow.append(cell)
                if not found:
                    cell_count += 1
                    continue
        if len(newrow) != 0:
            csv_list.append(row)
        if not found:
            row_count += 1
    csv_list = csv_list[row_count:]

my_file.close()

# Tests the pythag natural scale
def test_natural_scale(pythag_series):
    print("*** Beginning test_natural_scale() tests ***")
    # How many tests failed
    failed = 0
    column_padding = cell_count
    # The csv file is in sorted order, so we should begin by sorting our own collection to compare
    sorted_pythag_list = pythag_series.sort_by_final_frequency()
    for ordered_interval_index in range(pythag_series.NUM_INTERVALS):
        pythag_interval_array = sorted_pythag_list[ordered_interval_index].to_array()

        print("pythag array: " + str(pythag_interval_array))

        # Iterate through each property of the interval, the array should have the same order of interval properties as the csv
        for prop_index, prop in enumerate(pythag_interval_array):
            prop_name = csv_list[prop_index][column_padding - 1]
            # Return a property at a certain interval index
            csv_prop = csv_list[prop_index][column_padding + ordered_interval_index]
            # Check if the csv property and the calculated property match
            if ordered_interval_index in range(1, 7) or (
                            ordered_interval_index == 0 and prop_index in [0, 1, 2, 10]) or (
                            ordered_interval_index == 7 and prop_index in [0, 1]):
                if csv_prop and prop and isfloat(str(csv_prop)):
                    if isfloat(str(prop)):
                        p1 = round(float(csv_prop), 3)
                        p2 = round(float(prop), 3)
                        if round(float(prop), 3) == round(float(csv_prop), 3):
                            print(
                                "CORRECT: Index: " + str(
                                    ordered_interval_index) + " Property:  " + str(prop_name) + "  Value: " + str(
                                    prop))
                        else:
                            print(
                                "INCORRECT: Index: %s  Property: %s CSV Cell: %s , Pythag Calculated: %s" % (
                                    str(ordered_interval_index), str(prop_name), str(csv_prop), str(prop)))
                            failed += 1
                    else:
                        if str(csv_prop) == str(prop):
                            print(
                                "CORRECT: Index: " + str(
                                    ordered_interval_index) + " Property:  " + str(prop_name) + "  Value: " + str(
                                    prop))
                        else:
                            print(
                                "INCORRECT: Index: %s  Propert: %s CSV Cell: %s , Pythag Calculated: %s" % (
                                    str(ordered_interval_index), str(prop_name), str(csv_prop), str(prop)))
                            failed += 1
                else:
                    if str(csv_prop) == str(prop):
                        print(
                            "CORRECT: Index: " + str(
                                ordered_interval_index) + " Property:  " + str(prop_name) + "  Value: " + str(
                                prop))
                    else:
                        print(
                            "INCORRECT: Index: %s  Propert: %s CSV Cell: %s , Pythag Calculated: %s" % (
                                str(ordered_interval_index), str(prop_name), str(csv_prop), str(prop)))
                        failed += 1
    print("*** test_natural_Scale() SUMMARY *** ")
    print("Failed: %d " % failed)

# Tests octave modes computer to the csv file
def test_octave_scale(scale):
    print("*** Beginning test_octave_scale() tests ***")
    # How many tests failed
    failed = 0
    # The column index in the csv list
    colnum = cell_count
    # The row index in the csv list
    rownum = row_count + scale.NUM_INTERVALS + 1
    # The csv file is in sorted order, so we should begin by sorting our own collection to compare
    sorted_list = scale.sort_by_final_frequency()
    # Iterates through the list of modes
    for mode in mode_names:
        i = 0
        # Computes each interval in the scale
        for c in range(colnum, colnum + scale.NUM_INTERVALS):
            print("Modal index: " + str(i))
            calculated_frequency = sorted_list[i].final_frequency
            csv_frequency = csv_list[rownum][c]
            if csv_frequency and calculated_frequency and isfloat(str(csv_frequency)):
                if isfloat(str(calculated_frequency)):
                    # Checks if the frequencies are the same
                    if eq(round(float(calculated_frequency), 2), round(float(csv_frequency), 2)):
                        print(
                            "CORRECT: Modal index: " + str(
                                i) + ":  Calculated Frequency: " + str(
                                calculated_frequency))
                    else:
                        print(
                            "INCORRECT: Modal index: %s  CSV Frequency: %s ,  Calculated Frequency: %s" % (
                                str(i), str(csv_frequency), str(calculated_frequency)))
                        failed += 1
                # probably not used
                else:
                    if str(csv_frequency) == str(calculated_frequency):
                        print(
                            "CORRECT: Modal index: " +
                            str(i) + " Frequency: " + str(
                                calculated_frequency))

                    else:
                        print(
                            "INCORRECT: Modal index: %s CSV Frequency: %s ,  Calculated Frequency: %s" % (
                                str(c), str(csv_frequency), str(calculated_frequency)))

                        failed += 1
            else:
                if str(csv_frequency) == str(calculated_frequency):
                    print(
                        "CORRECT: Modal index: " +
                        str(i) + "Value: " + str(calculated_frequency))

                else:
                    print(
                        "INCORRECT: Modal index: %s CSV Frequency: %s ,  Calculated Frequency: %s" % (
                            str(i), str(csv_frequency), str(calculated_frequency)))

                    failed += 1
            i += 1
        colnum += 1
        rownum += 1
        # Retrieve the next mode
        sorted_list = scale.get_next_mode()

    print("*** test_octave_scale() SUMMARY *** ")
    print("Failed: %d " % failed)


def eq(a, b, eps=0.01):
    return abs(a - b) <= eps


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False