// -*- C++ -*-
//
// Package:    LeptonInt
// Class:      LeptonInt
// 
/**\class LeptonInt LeptonInt.cc RA2Classic/LeptonInt/src/LeptonInt.cc
 * 
 * Description: [one line class summary]
 * 
 * Implementation:
 *     [Notes on implementation]
 */
//
// Original Author:  Arne-Rasmus Draeger,68/111,4719,
//         Created:  Fri Apr 11 16:35:33 CEST 2014
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Candidate/interface/Candidate.h"

//
// class declaration
//

class LeptonInt : public edm::global::EDProducer<> {
public:
	explicit LeptonInt(const edm::ParameterSet&);
	~LeptonInt();
	
	static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	
private:
	virtual void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;
	
	// ----------member data ---------------------------
	std::vector<edm::InputTag> leptonTag_;
	std::vector<edm::EDGetTokenT<edm::View<reco::Candidate>>> leptonTok_;
};

//
// constructors and destructor
//
LeptonInt::LeptonInt(const edm::ParameterSet& iConfig)
{
	//register your products
	leptonTag_ 				= 	iConfig.getParameter< std::vector<edm::InputTag> >("LeptonTag");
	for(auto& tag: leptonTag_) leptonTok_.push_back(consumes<edm::View<reco::Candidate>>(tag));
	
	produces<int>("");
	
}


LeptonInt::~LeptonInt()
{
	
	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)
	
}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
LeptonInt::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
	using namespace edm;
	int Leptons=0;
	for(unsigned int i=0; i< leptonTok_.size();i++)
	{
		edm::Handle< edm::View<reco::Candidate> > cands;
		iEvent.getByToken(leptonTok_.at(i),cands);
		if( cands.isValid() ) 
		{
			Leptons+=cands->size();
		}
		else edm::LogWarning("TreeMaker")<<"LeptonIntProducer::Error tag invalid: "<<leptonTag_[i];
	}

	auto htp = std::make_unique<int>(Leptons);
	iEvent.put(std::move(htp));
	
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
LeptonInt::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(LeptonInt);
