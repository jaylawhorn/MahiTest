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


//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

class PedestalCheck : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit PedestalCheck(const edm::ParameterSet&);
      ~PedestalCheck();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      // ----------member data ---------------------------

  std::map<int, double> hitEnergySumMap_;
  HcalSimParameterMap simParameterMap_;
  
  edm::EDGetTokenT<HBHEChannelInfoCollection> token_ChannelInfo_;

  edm::Service<TFileService> FileService;

  TTree *outTree;

  int ieta;
  int iphi;
  int depth;
  int capID;
  double ts0;
  double ped0;
  double ts1;
  double ped1;

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
PedestalCheck::PedestalCheck(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed
   usesResource("TFileService");

   token_ChannelInfo_ = consumes<HBHEChannelInfoCollection>(edm::InputTag("hbheprereco",""));

}


PedestalCheck::~PedestalCheck()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
PedestalCheck::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   Handle<HBHEChannelInfoCollection> hChannelInfo;
   iEvent.getByToken(token_ChannelInfo_, hChannelInfo);

   for (HBHEChannelInfoCollection::const_iterator iter = hChannelInfo->begin(); iter!=hChannelInfo->end(); iter++) {
     const HBHEChannelInfo& chi(*iter);
     const HcalDetId detid =chi.id();
     
     ieta=detid.ieta();
     iphi=detid.iphi();
     depth=detid.depth();
     capID=chi.capid();
     ts0=chi.tsRawCharge(0);
     ped0=chi.tsPedestal(0);
     ts1=chi.tsRawCharge(1);
     ped1=chi.tsPedestal(1);
     outTree->Fill();
   }

}


// ------------ method called once each job just before starting event loop  ------------
void 
PedestalCheck::beginJob()
{

  outTree = FileService->make<TTree>("HcalTree","HcalTree");

  outTree->Branch("ieta",&ieta,"ieta/I");
  outTree->Branch("iphi",&iphi,"iphi/I");
  outTree->Branch("depth",&depth,"depth/I");
  outTree->Branch("capID",&capID,"capID/I");

  outTree->Branch("ts0",&ts0,"ts0/D");
  outTree->Branch("ped0",&ped0,"ped0/D");

  outTree->Branch("ts1",&ts1,"ts1/D");
  outTree->Branch("ped1",&ped1,"ped1/D");

}

// ------------ method called once each job just after ending the event loop  ------------
void 
PedestalCheck::endJob() 
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
PedestalCheck::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PedestalCheck);
