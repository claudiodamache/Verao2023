import ROOT

file = ROOT.TFile("/user/c/cbeiraod/local-area/Verao2023/2016/ZZ.root")

tree = file.Get("bdttree")

# TH1D(name, title, nbin, xmin, xmax)
hist = ROOT.TH1D("lepPtHist", "Histogram of LepPt", 20, 0, 100)
tree.Draw("LepPt>>lepPtHist", "weight", "goff")

# TCanvas(name, title, sizeX, sizeY)
c1 = ROOT.TCanvas("c1", "c1", 800, 600)
#c1.cd()
hist.Draw()
c1.SaveAs("file.pdf")
