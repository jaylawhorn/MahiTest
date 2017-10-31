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
  
  TFile *inf = new TFile("temp.root","read");
  TTree *t = (TTree*) inf->Get("flat/HcalTree");

  int ieta;
  int iphi;
  int depth;
  double mahiE;
  double mahiX;
  double m2E;
  double m2X;
  double m3E;

  t->SetBranchAddress("ieta", &ieta);
  t->SetBranchAddress("iphi", &iphi);
  t->SetBranchAddress("depth", &depth);
  t->SetBranchAddress("mahiE", &mahiE);
  t->SetBranchAddress("mahiX", &mahiX);
  t->SetBranchAddress("m2E", &m2E);
  t->SetBranchAddress("m2X", &m2X);
  t->SetBranchAddress("m3E", &m3E);

  TCanvas *c = new TCanvas("c","",800, 800);
  gStyle->SetOptStat(0);
  gStyle->SetPalette(55);
  c->SetLogz(1);
  //gStyle->SetPaintTextFormat("2.2f");
  
  TH2D *hLegacyVsMahiE = new TH2D("hLegacyVsMahiE", "", 50, 0, 500, 50, 0, 500);
  t->Draw("mahiE:m2E>>hLegacyVsMahiE","","colz");
  hLegacyVsMahiE->GetXaxis()->SetTitle("Method 2 Energy");
  hLegacyVsMahiE->GetYaxis()->SetTitle("MAHI Energy");
  c->SaveAs("hLegacyVsMahiE.png");

  TH2D *hLegacyVsMahiE_cleaned = new TH2D("hLegacyVsMahiE_cleaned", "", 50, 0, 500, 50, 0, 500);
  t->Draw("mahiE:m2E>>hLegacyVsMahiE_cleaned","mahiX<100","colz");
  hLegacyVsMahiE_cleaned->GetXaxis()->SetTitle("Method 2 Energy");
  hLegacyVsMahiE_cleaned->GetYaxis()->SetTitle("MAHI Energy");

  c->SaveAs("hLegacyVsMahiE_cleaned.png");

  TH2D *hLegacyVsMahiE_lo = new TH2D("hLegacyVsMahiE_lo", "", 50, 0, 50, 50, 0, 50);
  t->Draw("mahiE:m2E>>hLegacyVsMahiE_lo","","colz");
  hLegacyVsMahiE_lo->GetXaxis()->SetTitle("Method 2 Energy");
  hLegacyVsMahiE_lo->GetYaxis()->SetTitle("MAHI Energy");

  c->SaveAs("hLegacyVsMahiE_lo.png");

  TH2D *hLegacyVsMahiE_lo_cleaned = new TH2D("hLegacyVsMahiE_lo_cleaned", "", 50, 0, 50, 50, 0, 50);
  t->Draw("mahiE:m2E>>hLegacyVsMahiE_lo_cleaned","mahiX<100","colz");
  hLegacyVsMahiE_lo_cleaned->GetXaxis()->SetTitle("Method 2 Energy");
  hLegacyVsMahiE_lo_cleaned->GetYaxis()->SetTitle("MAHI Energy");

  c->SaveAs("hLegacyVsMahiE_lo_cleaned.png");

  TH2D *hLegacyVsMahiX = new TH2D("hLegacyVsMahiX", "", 50, 0, 500, 50, 0, 500);
  t->Draw("mahiX:m2X>>hLegacyVsMahiX","","colz");
  hLegacyVsMahiX->GetXaxis()->SetTitle("Method 2 Chi2");
  hLegacyVsMahiX->GetYaxis()->SetTitle("MAHI Chi2");

  c->SaveAs("hLegacyVsMahiX.png");

  //TH2D *hLegacyVsMahiX_cleaned = new TH2D("hLegacyVsMahiX_cleaned", "", 50, 0, 500, 50, 0, 500);
  //t->Draw("mahiX:m2X>>hLegacyVsMahiX_cleaned","");

  TH2D *hLegacyVsMahiX_lo = new TH2D("hLegacyVsMahiX_lo", "", 30, 0, 15, 30, 0, 15);
  t->Draw("mahiX:m2X>>hLegacyVsMahiX_lo","","colz");
  hLegacyVsMahiX_lo->GetXaxis()->SetTitle("Method 2 Chi2");
  hLegacyVsMahiX_lo->GetYaxis()->SetTitle("MAHI Chi2");

  c->SaveAs("hLegacyVsMahiX_lo.png");

  TH2D *hLegacyVsMahiX_lo_cleaned = new TH2D("hLegacyVsMahiX_lo_cleaned", "", 30, 0, 15, 30, 0, 15);
  t->Draw("mahiX:m2X>>hLegacyVsMahiX_lo_cleaned","m2X<15 && mahiX<15","colz");
  hLegacyVsMahiX_lo_cleaned->GetXaxis()->SetTitle("Method 2 Chi2");
  hLegacyVsMahiX_lo_cleaned->GetYaxis()->SetTitle("MAHI Chi2");

  c->SaveAs("hLegacyVsMahiX_lo_cleaned.png");

  TH2D *hHltVsMahiE = new TH2D("hHltVsMahiE", "", 50, 0, 500, 50, 0, 500);
  t->Draw("mahiE:m3E>>hHltVsMahiE","","colz");
  hHltVsMahiE->GetXaxis()->SetTitle("HLT Energy");
  hHltVsMahiE->GetYaxis()->SetTitle("MAHI Energy");

  c->SaveAs("hHltVsMahiE.png");

  TH2D *hHltVsMahiE_cleaned = new TH2D("hHltVsMahiE_cleaned", "", 50, 0, 500, 50, 0, 500);
  t->Draw("mahiE:m3E>>hHltVsMahiE_cleaned","mahiX<100","colz");  
  hHltVsMahiE_cleaned->GetXaxis()->SetTitle("HLT Energy");
  hHltVsMahiE_cleaned->GetYaxis()->SetTitle("MAHI Energy");

  c->SaveAs("hHltVsMahiE_cleaned.png");

  TH2D *hHltVsMahiE_lo = new TH2D("hHltVsMahiE_lo", "", 50, 0, 50, 50, 0, 50);
  t->Draw("mahiE:m3E>>hHltVsMahiE_lo","","colz");
  hHltVsMahiE_lo->GetXaxis()->SetTitle("HLT Energy");
  hHltVsMahiE_lo->GetYaxis()->SetTitle("MAHI Energy");

  c->SaveAs("hHltVsMahiE_lo.png");
    
  TH2D *hHltVsMahiE_lo_cleaned = new TH2D("hHltVsMahiE_lo_cleaned", "", 50, 0, 50, 50, 0, 50);
  t->Draw("mahiE:m3E>>hHltVsMahiE_lo_cleaned","mahiX<100","colz");
  hHltVsMahiE_lo_cleaned->GetXaxis()->SetTitle("HLT Energy");
  hHltVsMahiE_lo_cleaned->GetYaxis()->SetTitle("MAHI Energy");

  c->SaveAs("hHltVsMahiE_lo_cleaned.png");

  TH2D *hMahiXVsMahiE = new TH2D("hMahiXVsMahiE", "", 50, 0, 500, 50, 0, 500);
  t->Draw("mahiX:mahiE>>hMahiXVsMahiE","","colz");
  hMahiXVsMahiE->GetXaxis()->SetTitle("MAHI Energy");
  hMahiXVsMahiE->GetYaxis()->SetTitle("MAHI Chi2");

  c->SaveAs("hMahiXVsMahiE.png");

  TH2D *hMahiXVsMahiE_cleaned = new TH2D("hMahiXVsMahiE_cleaned", "", 50, 0, 500, 50, 0, 500);
  t->Draw("mahiX:mahiE>>hMahiXVsMahiE_cleaned", "mahiX<100","colz");
  hMahiXVsMahiE_cleaned->GetXaxis()->SetTitle("MAHI Energy");
  hMahiXVsMahiE_cleaned->GetYaxis()->SetTitle("MAHI Chi2");

  c->SaveAs("hMahiXVsMahiE_cleaned.png");

  TH2D *hMahiXVsMahiE_lo = new TH2D("hMahiXVsMahiE_lo", "", 50, 0, 50, 50, 0, 50);
  t->Draw("mahiX:mahiE>>hMahiXVsMahiE_lo","","colz");
  hMahiXVsMahiE_lo->GetXaxis()->SetTitle("MAHI Energy");
  hMahiXVsMahiE_lo->GetYaxis()->SetTitle("MAHI Chi2");

  c->SaveAs("hMahiXVsMahiE_lo.png");

  TH2D *hMahiXVsMahiE_lo_cleaned = new TH2D("hMahiXVsMahiE_lo_cleaned", "", 50, 0, 50, 50, 0, 50);
  t->Draw("mahiX:mahiE>>hMahiXVsMahiE_lo_cleaned", "mahiX<100","colz");
  hMahiXVsMahiE_lo_cleaned->GetXaxis()->SetTitle("MAHI Energy");
  hMahiXVsMahiE_lo_cleaned->GetYaxis()->SetTitle("MAHI Chi2");

  c->SaveAs("hMahiXVsMahiE_lo_cleaned.png");

  TH2D *hLegacyXVsLegacyE = new TH2D("hLegacyXVsLegacyE", "", 50, 0, 500, 50, 0, 500);
  t->Draw("m2X:m2E>>hLegacyXVsLegacyE","","colz");
  hLegacyXVsLegacyE->GetXaxis()->SetTitle("M2 Energy");
  hLegacyXVsLegacyE->GetYaxis()->SetTitle("M2 Chi2");

  c->SaveAs("hLegacyXVsLegacyE.png");

  TH2D *hLegacyXVsLegacyE_cleaned = new TH2D("hLegacyXVsLegacyE_cleaned", "", 50, 0, 500, 50, 0, 500);
  t->Draw("m2X:m2E>>hLegacyXVsLegacyE_cleaned", "m2X<100","colz");
  hLegacyXVsLegacyE_cleaned->GetXaxis()->SetTitle("M2 Energy");
  hLegacyXVsLegacyE_cleaned->GetYaxis()->SetTitle("M2 Chi2");

  c->SaveAs("hLegacyXVsLegacyE_cleaned.png");

  TH2D *hLegacyXVsLegacyE_lo = new TH2D("hLegacyXVsLegacyE_lo", "", 50, 0, 50, 50, 0, 50);
  t->Draw("m2X:m2E>>hLegacyXVsLegacyE_lo","","colz");
  hLegacyXVsLegacyE_lo->GetXaxis()->SetTitle("M2 Energy");
  hLegacyXVsLegacyE_lo->GetYaxis()->SetTitle("M2 Chi2");

  c->SaveAs("hLegacyXVsLegacyE_lo.png");

  TH2D *hLegacyXVsLegacyE_lo_cleaned = new TH2D("hLegacyXVsLegacyE_lo_cleaned", "", 50, 0, 50, 50, 0, 50);
  t->Draw("m2X:m2E>>hLegacyXVsLegacyE_lo_cleaned", "m2X<100","colz");
  hLegacyXVsLegacyE_lo_cleaned->GetXaxis()->SetTitle("M2 Energy");
  hLegacyXVsLegacyE_lo_cleaned->GetYaxis()->SetTitle("M2 Chi2");

  c->SaveAs("hLegacyXVsLegacyE_lo_cleaned.png");
  
}
