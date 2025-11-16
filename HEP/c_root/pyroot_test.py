import ROOT
f = ROOT.TFile("hsimple.root")
h = ROOT.TH1F("h","h",64,-10,10)
for evt in f.hsimple:
    if evt.pz > 0:
        h.Fill(evt.py * evt.pz)
h.Draw()