from Plots import Plots

import argparse


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Read JSON file")
    parser.add_argument("-jp", "--json_plot", type=str, default= "/lstore/cms/cbeiraod/Verao2023/plot2016.json")
    parser.add_argument("-jv", "--json_var", type=str, default= "/lstore/cms/cbeiraod/Verao2023/variablesAN_DataMC.json")
    parser.add_argument("-f", "--files", type=str, default= "/user/c/cbeiraod/local-area/Verao2023/2016/")
    parser.add_argument("-unblind", "--data", type=bool, default=False )
    args = parser.parse_args()
    
    graf = Plots(args.json_plot, args.json_var, args.files, args.data)

    graf.data_processing()
