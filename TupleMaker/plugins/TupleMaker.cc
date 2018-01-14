// -*- C++ -*-
//
// Package:    MahiTest/TupleMaker
// Class:      TupleMaker
// 
/**\class TupleMaker TupleMaker.cc MahiTest/TupleMaker/plugins/TupleMaker.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Jay Mathew Lawhorn
//         Created:  Sun, 22 Oct 2017 12:46:00 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/ESHandle.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/HcalRecHit/interface/HBHERecHit.h"
#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"

#include "Geometry/HcalCommonData/interface/HcalHitRelabeller.h"

#include "CalibFormats/HcalObjects/interface/HcalCoderDb.h"
#include "CalibFormats/HcalObjects/interface/HcalCalibrations.h"
#include "CalibFormats/HcalObjects/interface/HcalDbService.h"
#include "CalibFormats/HcalObjects/interface/HcalDbRecord.h"
#include "CalibCalorimetry/HcalAlgos/interface/HcalPulseShapes.h"

#include "Geometry/CaloTopology/interface/HcalTopology.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "Geometry/Records/interface/CaloGeometryRecord.h"

#include "SimDataFormats/CaloHit/interface/PCaloHit.h"
#include "SimDataFormats/CaloHit/interface/PCaloHitContainer.h"
#include "SimCalorimetry/HcalSimAlgos/interface/HcalSimParameterMap.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include <iostream>
#include <fstream>

#include "TTree.h"
#include "TFile.h"
#include "TH1D.h"

//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

class TupleMaker : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit TupleMaker(const edm::ParameterSet&);
      ~TupleMaker();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      // ----------member data ---------------------------

  std::map<int, double> hitEnergySumMap_;
  HcalSimParameterMap simParameterMap_;
  
  edm::EDGetTokenT<HBHEChannelInfoCollection> token_ChannelInfo_;
  edm::EDGetTokenT<HBHERecHitCollection> token_RecHit_;
  edm::EDGetTokenT<edm::PCaloHitContainer> tok_hbhe_sim_;

  edm::Service<TFileService> FileService;

  const HcalDDDRecConstants *hcons;
  const CaloGeometry *Geometry;

  TTree *outTree;

  int ieta;
  int iphi;
  int depth;
  double mahiE;
  double mahiT;
  double mahiX;
  double m2E;
  double m2X;
  double m0E;
  double simE;
  double mahiSimR;
  double m2SimR;
  double m0SimR;

  TH1D *hMahiSimR;
  TH1D *hM2SimR;
  TH1D *hM0SimR;
  TH1D *hMahiM2R;
  TH1D *hNiters;

};


//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
TupleMaker::TupleMaker(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed
   usesResource("TFileService");

   token_ChannelInfo_ = consumes<HBHEChannelInfoCollection>(edm::InputTag("hbheprereco",""));
   token_RecHit_ = consumes<HBHERecHitCollection>(edm::InputTag("hbheprereco",""));
   tok_hbhe_sim_ = consumes<edm::PCaloHitContainer>(edm::InputTag("g4SimHits","HcalHits"));
   //token_RecHit_ = consumes<HBHERecHitCollection>(edm::InputTag("hbhereco",""));

}


TupleMaker::~TupleMaker()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
TupleMaker::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   ESHandle<HcalDDDRecConstants> pHRNDC;
   iSetup.get<HcalRecNumberingRecord>().get( pHRNDC );
   hcons = &(*pHRNDC);

   Handle<HBHEChannelInfoCollection> hChannelInfo;
   iEvent.getByToken(token_ChannelInfo_, hChannelInfo);

   Handle<HBHERecHitCollection> hRecHit;
   iEvent.getByToken(token_RecHit_, hRecHit);

   Handle<PCaloHitContainer> hSimHits;
   iEvent.getByToken(tok_hbhe_sim_,hSimHits);

   ESHandle<HcalDbService> hConditions;
   iSetup.get<HcalDbRecord>().get(hConditions);

   ESHandle<CaloGeometry> hGeometry;
   iSetup.get<CaloGeometryRecord>().get(hGeometry);
   Geometry = hGeometry.product();

   //std::cout << "-----" << std::endl;
   //std::cout << hRecHit->size() << std::endl;

   for (HBHERecHitCollection::const_iterator iter = hRecHit->begin(); iter!=hRecHit->end(); iter++) {
     const HBHERecHit& rh(*iter);
     const HcalDetId detid =rh.id();
     //std::cout << rh.energy() << std::endl;
     
     //if (rh.eaux()<1) continue;

     ieta=detid.ieta();
     iphi=detid.iphi();
     depth=detid.depth();

     mahiE=rh.energy();
     mahiT=rh.time();
     mahiX=rh.chi2();

     hNiters->Fill(int(mahiT)%1000);

     m2E=rh.eaux();
     m2X=0;//rh.chi2();

     m0E=rh.eraw();

     simE=0;
     mahiSimR=-1;
     m2SimR=-1;
     m0SimR=-1;

     if (!iEvent.isRealData()) {
       double SamplingFactor = 1;
       if(detid.subdet() == HcalBarrel) {
	 SamplingFactor = simParameterMap_.hbParameters().samplingFactor(detid);
       } else if (detid.subdet() == HcalEndcap) {
	 SamplingFactor = simParameterMap_.heParameters().samplingFactor(detid);
       }
       if (ieta>15 && ieta<30 && iphi>62 && iphi<67 && depth==1) SamplingFactor/=1.5;
       for (int j = 0; j < (int) hSimHits->size(); j++) {

	 HcalDetId simId = HcalHitRelabeller::relabel((*hSimHits)[j].id(), hcons);
	    
	 if (simId == detid) {
	   simE+=SamplingFactor*((*hSimHits)[j].energy());
	 }
       }
       if (simE!=0) {
	 mahiSimR=mahiE/simE;
	 hMahiSimR->Fill(mahiSimR);
	 m2SimR=m2E/simE;
	 hM2SimR->Fill(m2SimR);
	 m0SimR=m0E/simE;
	 hM0SimR->Fill(m0SimR);
       }
     }
     if (m2E!=0) {
       hMahiM2R->Fill(mahiE/m2E);
     }

     outTree->Fill();

   }

  //int ieta;
  //int iphi;
  //int depth;
  //double mahiE;
  //double mahiX;
  //double m2E;
  //double m2X;
  //double m3E;


   //Yeah, such a hack                                                                
   //float tdcTime = info.soiRiseTime();
   //if (!HcalSpecialTimes::isSpecial(tdcTime))
   //  tdcTime += timeShift_;
   //rh = HBHERecHit(channelId, m10E, chi2_mahi, tdcTime);
   //rh.setRawEnergy(m3E);
   //rh.setAuxEnergy(m2E);
   //rh.setChiSquared(chi2);

}


// ------------ method called once each job just before starting event loop  ------------
void 
TupleMaker::beginJob()
{

  //int ieta;
  //int iphi;
  //int depth;
  //double mahiE;
  //double mahiX;
  //double m2E;
  //double m2X;
  //double m3E;


   //TH2D *hMahiSimR;
   //TH2D *hM2SimR;
   //TH2D *hM3SimR;
   //TH2D *hMahiM2R;

  hMahiSimR = FileService->make<TH1D>("hMahiSimR", "", 100, 0, 2);
  hMahiSimR->SetLineColor(kBlack);
  hM2SimR   = FileService->make<TH1D>("hM2SimR", "",   100, 0, 2);
  hM2SimR->SetLineColor(kBlue);
  hM0SimR   = FileService->make<TH1D>("hM0SimR", "",   100, 0, 2);
  hM0SimR->SetLineColor(kRed);
  hMahiM2R  = FileService->make<TH1D>("hMahiM2R", "",  100, 0, 2);

  hNiters = FileService->make<TH1D>("hNiters","", 51, 0, 510);

  outTree = FileService->make<TTree>("HcalTree","HcalTree");

  outTree->Branch("ieta",&ieta,"ieta/I");
  outTree->Branch("iphi",&iphi,"iphi/I");
  outTree->Branch("depth",&depth,"depth/I");

  outTree->Branch("mahiE",&mahiE,"mahiE/D");
  outTree->Branch("mahiT",&mahiT,"mahiT/D");
  outTree->Branch("mahiX",&mahiX,"mahiX/D");

  outTree->Branch("m2E",&m2E,"m2E/D");
  outTree->Branch("m2X",&m2X,"m2X/D");

  outTree->Branch("m0E",&m0E,"m0E/D");

  outTree->Branch("simE",&simE,"simE/D");
  outTree->Branch("mahiSimR",&mahiSimR,"mahiSimR/D");
  outTree->Branch("m2SimR",&m2SimR,"m2SimR/D");
  outTree->Branch("m0SimR",&m0SimR,"m0SimR/D");


}

// ------------ method called once each job just after ending the event loop  ------------
void 
TupleMaker::endJob() 
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TupleMaker::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TupleMaker);
