import json
import ROOT


class Plots :
    def __init__(self, json:str, files:str, variables:list):
        #path to json
        self.__json = json
        
        #path to files
        self.__files = files
        
        #which variables
        self.__var = variables
    

    def read_json(self):
        
        try:
            with open(self.__json, "r") as file:
                data = json.load(file)
            return data
        
        except FileNotFoundError:
            print(f' Error: {self.__json} not found.')
            return None
        
        except json.JSONDecodeError:
            print(f'Error: {self.__json} not in JSON format')
            return None
        
        
        
    # filename = self.__files + (name of file)
    def file_getter(self, filename):

        try:
            with open(filename, 'r') as local_file:
                file_content = local_file.read()
            return file_content
        
        except FileNotFoundError as e:
            print(f"File not found: {e}")
            return None
        

    def data_processing(self):
        
        data = self.read_json()
        main_counter = 0
        c1 = ROOT.TCanvas("c1", "c1", 800, 600)
        
        for entry in data['lines']:
            #colour = entry['color']
            stack = ROOT.THStack("nome", entry['tag'] )
            counter = 0


            for b_file in entry['files']:
                file = ROOT.TFile(f'{self.__files}{b_file["tag"]}.root')
                tree = file.Get("bdttree")

                hist_name = f'{b_file["tag"]}'
                hist_number = f'Histogram {counter}'

                hist = ROOT.TH1D(hist_name, hist_number, 20, 0, 100) #personalizar o numero de bin e dimensoes
                
                for variable in self.__var: 
                    tree.Draw(f'{variable}>>{hist_name}',"weight", "goff")
                
                #hist.SetFillColor(colour)
                stack.Add(hist)
                counter += 1

            stack.Draw()
            c1.SaveAs(f'stack{main_counter}.pdf')
            main_counter += 1

                    
        return None
    

