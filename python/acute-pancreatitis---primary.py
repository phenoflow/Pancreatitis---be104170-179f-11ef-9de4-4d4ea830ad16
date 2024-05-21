# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"J670000","system":"readv2"},{"code":"J670900","system":"readv2"},{"code":"J670700","system":"readv2"},{"code":"J670200","system":"readv2"},{"code":"J670600","system":"readv2"},{"code":"J670300","system":"readv2"},{"code":"J670z00","system":"readv2"},{"code":"J670.00","system":"readv2"},{"code":"J670400","system":"readv2"},{"code":"J670100","system":"readv2"},{"code":"K85","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('pancreatitis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["acute-pancreatitis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["acute-pancreatitis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["acute-pancreatitis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
