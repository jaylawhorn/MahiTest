#if !defined(__CINT__) || defined(__MAKECINT__)
#include <TROOT.h>                        // access to gROOT, entry point to ROOT system
#include <TSystem.h>                      // interface to OS
#include <TStyle.h>                       // class to handle ROOT plotting styles
#include <TFile.h>                        // file handle class
#include <TTree.h>                        // class to access ntuples
#include <TChain.h>                        // class to access ntuples
#include <TH1D.h>
#include <TH2D.h>
#include <TProfile2D.h>
#include <TCanvas.h>
#include <TLegend.h>
#include <TBenchmark.h>                   // class to track macro running statistics
#include <vector>                         // STL vector class
#include <iostream>                       // standard I/O
#include <iomanip>                        // functions to format standard I/O
#include <fstream>                        // functions for file I/O
#include <string>                         // C++ string class
#include <sstream>                        // class for parsing strings
#endif

void makeComparisons() {

  TString fname = "MC_noPU_SiPM";
  
  TFile *inf = new TFile(fname+".root","read");
  TTree *t = (TTree*) inf->Get("flat/HcalTree");

  int ieta;
  int iphi;
  int depth;
  double mahiE;
  double m2E;
  double m3E;
  double simE;

  t->SetBranchAddress("ieta", &ieta);
  t->SetBranchAddress("iphi", &iphi);
  t->SetBranchAddress("depth", &depth);
  t->SetBranchAddress("mahiE", &mahiE);
  t->SetBranchAddress("m2E", &m2E);
  t->SetBranchAddress("m3E", &m3E);
  t->SetBranchAddress("simE", &simE);

  TCanvas *c = new TCanvas("c","",800, 800);
  gStyle->SetOptStat(0);
  gStyle->SetPalette(55);
  c->SetLogz(1);
  
  TH2D *hSimVsMahiE = new TH2D("hSimVsMahiE", "", 50, 0, 200, 50, 0, 200);
  t->Draw("mahiE:simE>>hSimVsMahiE","","colz");
  hSimVsMahiE->SetTitle("");
  hSimVsMahiE->GetXaxis()->SetTitle("Sim Energy");
  hSimVsMahiE->GetYaxis()->SetTitle("Mahi Energy");
  c->SaveAs(fname+"_Mahi_v_Sim.png");

  TH1D *hSimVsMahiE2 = new TH1D("hSimVsMahiE2","",20,0,2);
  t->Draw("mahiE/simE>>hSimVsMahiE2","simE>0.1");
  hSimVsMahiE2->SetTitle("");
  hSimVsMahiE2->GetXaxis()->SetTitle("MAHI/Sim");
  hSimVsMahiE2->GetYaxis()->SetTitle("Hits");
  c->SaveAs(fname+"_MahiSim.png");

  TH2D *hSimVsMahiE_lo = new TH2D("hSimVsMahiE_lo", "", 40, 0, 20, 40, 0, 20);
  t->Draw("mahiE:simE>>hSimVsMahiE_lo","","colz");
  hSimVsMahiE_lo->SetTitle("");
  hSimVsMahiE_lo->GetXaxis()->SetTitle("Sim Energy");
  hSimVsMahiE_lo->GetYaxis()->SetTitle("Mahi Energy");
  c->SaveAs(fname+"_Mahi_v_Sim_lo.png");

  TH2D *hLegacyVsMahiE = new TH2D("hLegacyVsMahiE", "", 50, 0, 200, 50, 0, 200);
  t->Draw("mahiE:m2E>>hLegacyVsMahiE","","colz");
  hLegacyVsMahiE->SetTitle("");
  hLegacyVsMahiE->GetXaxis()->SetTitle("Method 2 Energy");
  hLegacyVsMahiE->GetYaxis()->SetTitle("Mahi Energy");
  c->SaveAs(fname+"_Mahi_v_M2.png");

  TH1D *hLegacyVsMahiE2 = new TH1D("hLegacyVsMahiE2","",20,0,2);
  t->Draw("mahiE/m2E>>hLegacyVsMahiE2","");
  hLegacyVsMahiE2->SetTitle("");
  hLegacyVsMahiE2->GetXaxis()->SetTitle("MAHI/M2");
  hLegacyVsMahiE2->GetYaxis()->SetTitle("Hits");
  c->SaveAs(fname+"_MahiM2.png");

  TH2D *hLegacyVsMahiE_lo = new TH2D("hLegacyVsMahiE_lo", "", 40, 0, 20, 40, 0, 20);
  t->Draw("mahiE:m2E>>hLegacyVsMahiE_lo","","colz");
  hLegacyVsMahiE_lo->SetTitle("");
  hLegacyVsMahiE_lo->GetXaxis()->SetTitle("Method 2 Energy");
  hLegacyVsMahiE_lo->GetYaxis()->SetTitle("Mahi Energy");
  c->SaveAs(fname+"_Mahi_v_M2_lo.png");

  TH2D *hHltVsMahiE = new TH2D("hHltVsMahiE", "", 50, 0, 200, 50, 0, 200);
  t->Draw("mahiE:m3E>>hHltVsMahiE","","colz");
  hHltVsMahiE->SetTitle("");
  hHltVsMahiE->GetXaxis()->SetTitle("Method 3 Energy");
  hHltVsMahiE->GetYaxis()->SetTitle("Mahi Energy");
  c->SaveAs(fname+"_Mahi_v_M3.png");

  TH1D *hHltVsMahiE2 = new TH1D("hHltVsMahiE2","",20,0,2);
  t->Draw("mahiE/m3E>>hHltVsMahiE2","");
  hHltVsMahiE2->SetTitle("");
  hHltVsMahiE2->GetXaxis()->SetTitle("MAHI/M3");
  hHltVsMahiE2->GetYaxis()->SetTitle("Hits");
  c->SaveAs(fname+"_MahiM3.png");

  TH2D *hHltVsMahiE_lo = new TH2D("hHltVsMahiE_lo", "", 40, 0, 20, 40, 0, 20);
  t->Draw("mahiE:m3E>>hHltVsMahiE_lo","","colz");
  hHltVsMahiE_lo->SetTitle("");
  hHltVsMahiE_lo->GetXaxis()->SetTitle("Method 3 Energy");
  hHltVsMahiE_lo->GetYaxis()->SetTitle("Mahi Energy");
  c->SaveAs(fname+"_Mahi_v_M3_lo.png");
  
  TH2D *hHltVsM2E = new TH2D("hHltVsM2E", "", 50, 0, 200, 50, 0, 200);
  t->Draw("m3E:m2E>>hHltVsM2E","","colz");
  hHltVsM2E->SetTitle("");
  hHltVsM2E->GetXaxis()->SetTitle("Method 2 Energy");
  hHltVsM2E->GetYaxis()->SetTitle("Method 3 Energy");
  c->SaveAs(fname+"_M3_v_M2.png");

  TH1D *hHltVsM2E2 = new TH1D("hHltVsM2E2","",20,0,2);
  t->Draw("m3E/m2E>>hHltVsM2E2","");
  hHltVsM2E2->SetTitle("");
  hHltVsM2E2->GetXaxis()->SetTitle("M3/M2");
  hHltVsM2E2->GetYaxis()->SetTitle("Hits");
  c->SaveAs(fname+"_M3M2.png");

  TH2D *hHltVsM2E_lo = new TH2D("hHltVsM2E_lo", "", 40, 0, 20, 40, 0, 20);
  t->Draw("m3E:m2E>>hHltVsM2E_lo","","colz");
  hHltVsM2E_lo->SetTitle("");
  hHltVsM2E_lo->GetXaxis()->SetTitle("Method 2 Energy");
  hHltVsM2E_lo->GetYaxis()->SetTitle("Method 3 Energy");
  c->SaveAs(fname+"_M3_v_M2_lo.png");
    
}
