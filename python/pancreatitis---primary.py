# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"J670z11","system":"readv2"},{"code":"D201612","system":"readv2"},{"code":"A785100","system":"readv2"},{"code":"A723.00","system":"readv2"},{"code":"1113.0","system":"readv2"},{"code":"104611.0","system":"readv2"},{"code":"14905.0","system":"readv2"},{"code":"18544.0","system":"readv2"},{"code":"105910.0","system":"readv2"},{"code":"105066.0","system":"readv2"},{"code":"24984.0","system":"readv2"},{"code":"31395.0","system":"readv2"},{"code":"42278.0","system":"readv2"},{"code":"12316.0","system":"readv2"},{"code":"49499.0","system":"readv2"},{"code":"48685.0","system":"readv2"},{"code":"1506.0","system":"readv2"},{"code":"104385.0","system":"readv2"},{"code":"44278.0","system":"readv2"},{"code":"49353.0","system":"readv2"},{"code":"44571.0","system":"readv2"},{"code":"61326.0","system":"readv2"},{"code":"656.0","system":"readv2"},{"code":"4650.0","system":"readv2"},{"code":"1419.0","system":"readv2"},{"code":"105194.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('pancreatitis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["pancreatitis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["pancreatitis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["pancreatitis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
