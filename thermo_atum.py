import input.reader as reader
import core.main as core
import pandas as pd
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='input_path', required=True)
    parser.add_argument("-o", dest="output_path", required=True)
    parser.add_argument("--start", dest="start", default=None, required=False)
    parser.add_argument("--end", dest="end", default=None, required=False)
    args = parser.parse_args()
    sheet = reader.read_sheet(args.input_path)
    start = 0
    end = len(sheet.index)-1
    if args.start is not None:
        start_index= sheet.index[sheet.iloc[:, 0] >= float(args.start)]
        if len(start_index)>0:
            start = start_index[0]

    if args.end is not None:
        end_index = sheet.index[sheet.iloc[:, 0] <= float(args.end)]
        if len(end_index)>0:
            end = end_index[-1]
    new_data = core.calculate_sheet_data(sheet, start, end)
    df = pd.DataFrame.from_dict(new_data)
    df.to_excel(args.output_path, index=False)


if __name__ == '__main__':
    main()