import ROOT
import numpy as np

data_x = np.linspace(0.,10.)
data_y = np.sin(data_x)

canvas = ROOT.TCanvas("Nome Scemo")
histo = ROOT.TH1F("Histo","Istogramma",64,0,16)
graph = ROOT.TGraph()

histo.FillRandom('pol1')
histo.SetLineWidth(2)

graph.SetTitle("MyGraph;MyX;MyZ")
for x,y in zip(data_x,data_y):
    graph.AddPoint(x,y)
graph.SetMarkerStyle(22)
graph.SetMarkerColor(ROOT.kRed)
graph.SetLineColor(0)

graph.Draw()
canvas.Draw()
