import json
import ROOT


class Plots :
    def __init__(self, json_plot:str, json_var:str, files:str, variables:list, data_draw:bool):
        #path to json with plot data
        self.__json = json_plot
        
        #path to json with var data
        self.__var_data = json_var
        
        #path to files
        self.__files = files
        
        #which variables
        self.__var = variables
        
        #draw data or not
        self.__data = data_draw
        

    

    def read_json(self, file_:str):
        
        try:
            with open(file_, "r") as file:
                data = json.load(file)
            return data
        
        except FileNotFoundError:
            print(f' Error: {file_} not found.')
            return None
        
        except json.JSONDecodeError:
            print(f'Error: {file_} not in JSON format')
            return None
        
        

    def dafault_setter(self):

        data = self.read_json(self.__json)

        for entry in data['lines']:
            if 'tag' not in entry:
                entry['tag'] = ""

            if 'label' not in entry:
                entry['label'] = ""

            if 'isdata' not in entry:
                entry['isdata'] = False

            if 'issignal' not in entry:
                entry['issignal'] = False
            
            if 'isfastsim' not in entry:
                entry['isfastsim'] = False

            if 'spimpose' not in entry:
                entry['spimpose'] = False
            
            if 'color' not in entry:
                entry['color'] = 1
            
            if 'lcolor' not in entry:
                entry['lcolor_'] = 1
            
            if 'lwidth' not in entry:
                entry['lwidth'] = 1

            if 'lstyle' not in entry:
                entry['lstyle'] = 1

            if 'fill_' not in entry:
                entry['fill'] = 0
            
            if 'marker' not in entry:
                entry['marker'] = 1
            
            if 'mcolor' not in entry:
                entry['mcolor'] = 1


        return data
    
    
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
        
        data = self.dafault_setter()
        var_data = self.read_json(self.__var_data)
        
        
        c1 = ROOT.TCanvas("c1", "c1", 800, 600)

        for variable in var_data['variables']:
            var_name = variable['expression']
            var_min = variable['min']
            var_max = variable['max']
            var_bins = variable['bins']
            stack = ROOT.THStack('stack', f'{var_name}')

            for entry in data['lines']:
                Process_hist = ROOT.TH1D( entry['tag'], entry['tag'], var_bins, var_min, var_max) 
                chain = ROOT.TChain("bdttree")

                for b_file in entry['files']:
                    #file = ROOT.TFile(f'/user/c/cbeiraod/local-area/Verao2023/2016/{b_file["tag"]}.root')   #alterar com o path também se quisermos
                    #chain.Add(f'/user/c/cbeiraod/local-area/Verao2023/2016/{b_file["tag"]}.root')      
                    chain.Add(f'{self.__files}{b_file["tag"]}.root')

                #chain.Draw(f'{variable}>> entry["tag"] ',f'weight*({prefilter})*({selection})', "goff")
                chain.Draw(f'{variable}>> entry["tag"] ','weight', "goff")
                Process_hist.SetFillColor(entry['color'])
                Process_hist.SetLineWidth(entry['lwidth'])
                Process_hist.SetLineColor(entry['lcolor'])
                Process_hist.SetLineStyle(entry['lStyle'])
                Process_hist.SetMarkerStyle(entry['marker'])
                Process_hist.SetMarkerColor(entry['mcolor'])

                if entry['isdata']:
                    Process_hist.Draw()

                else: 
                    Process_hist.Draw('hist')

                c1.SaveAs(f'Histogram{entry["tag"]}_{variable}.pdf')
                
                if not entry['isdata'] or entry['issignal']:
                    stack.Add(Process_hist)
            
            stack.Draw()
            #draw data e sinal
            #adicionar se queremos draw do data ou não, default = no
            c1.BuildLegend(0.8, 0.8, 0.7, 0.7)
            c1.SaveAs(f'Stack{variable}.pdf')

            #ciclo externo termina aqui

                    
        return None
    



    

