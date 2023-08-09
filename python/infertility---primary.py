# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"K5B..00","system":"readv2"},{"code":"104569.0","system":"med"},{"code":"16360.0","system":"med"},{"code":"1808.0","system":"med"},{"code":"25077.0","system":"med"},{"code":"30392.0","system":"med"},{"code":"35074.0","system":"med"},{"code":"36458.0","system":"med"},{"code":"45985.0","system":"med"},{"code":"48461.0","system":"med"},{"code":"4977.0","system":"med"},{"code":"50116.0","system":"med"},{"code":"52132.0","system":"med"},{"code":"53018.0","system":"med"},{"code":"54282.0","system":"med"},{"code":"60861.0","system":"med"},{"code":"61299.0","system":"med"},{"code":"62084.0","system":"med"},{"code":"62698.0","system":"med"},{"code":"63421.0","system":"med"},{"code":"68664.0","system":"med"},{"code":"69324.0","system":"med"},{"code":"69884.0","system":"med"},{"code":"73151.0","system":"med"},{"code":"8352.0","system":"med"},{"code":"91280.0","system":"med"},{"code":"96463.0","system":"med"},{"code":"97461.0","system":"med"},{"code":"99069.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('female-infertility-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["infertility---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["infertility---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["infertility---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
