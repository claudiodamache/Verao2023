from Plots import Plots

import argparse


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Read JSON file")
    parser.add_argument("-j", "--json", type=str)
    parser.add_argument("-f", "--files", type=str)
    parser.add_argument("-v", "--variables", type=list)
    args = parser.parse_args()
    
    graf = Plots(args.json, args.files, args.variables)

    graf.data_processing()