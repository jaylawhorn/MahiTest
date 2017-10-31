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

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/HcalRecHit/interface/HBHERecHit.h"
#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"

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
  
  edm::EDGetTokenT<HBHEChannelInfoCollection> token_ChannelInfo_;
  edm::EDGetTokenT<HBHERecHitCollection> token_RecHit_;

  edm::Service<TFileService> FileService;

  TTree *outTree;

  int ieta;
  int iphi;
  int depth;
  double mahiE;
  double mahiX;
  double m2E;
  double m2X;
  double m3E;

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

   Handle<HBHEChannelInfoCollection> hChannelInfo;
   iEvent.getByToken(token_ChannelInfo_, hChannelInfo);

   Handle<HBHERecHitCollection> hRecHit;
   iEvent.getByToken(token_RecHit_, hRecHit);

   //std::cout << "-----" << std::endl;
   //std::cout << hRecHit->size() << std::endl;

   for (HBHERecHitCollection::const_iterator iter = hRecHit->begin(); iter!=hRecHit->end(); iter++) {
     const HBHERecHit& rh(*iter);
     const HcalDetId detid =rh.id();
     //std::cout << rh.energy() << std::endl;

     if (rh.eaux()<1) continue;

     ieta=detid.ieta();
     iphi=detid.iphi();
     depth=detid.depth();

     mahiE=rh.energy();
     mahiX=rh.time();

     m2E=rh.eaux();
     m2X=rh.chi2();

     m3E=rh.eraw();

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


  outTree = FileService->make<TTree>("HcalTree","HcalTree");

  outTree->Branch("ieta",&ieta,"ieta/I");
  outTree->Branch("iphi",&iphi,"iphi/I");
  outTree->Branch("depth",&depth,"depth/I");

  outTree->Branch("mahiE",&mahiE,"mahiE/D");
  outTree->Branch("mahiX",&mahiX,"mahiX/D");

  outTree->Branch("m2E",&m2E,"m2E/D");
  outTree->Branch("m2X",&m2X,"m2X/D");

  outTree->Branch("m3E",&m3E,"m3E/D");


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
