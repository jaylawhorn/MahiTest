# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: reco -s RAW2DIGI,RECO --filein file:pickevents.root --fileout file:useless.root --conditions 92X_dataRun2_HLT_v7 --eventcontent FEVTDEBUG
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
#process.MessageLogger.categories.append('FastReport')
#process.MessageLogger.cerr.FastReport = cms.untracked.PSet( limit = cms.untracked.int32(10000000) )
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

# Input source
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
        #"file:/eos/cms/store/relval/CMSSW_10_0_0_pre1/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v10-v1/10000/00F81697-AECB-E711-A8DB-0CC47A4D7600.root",
        # "file:/eos/cms/store/relval/CMSSW_10_0_0_pre1/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v10-v1/10000/02270F3A-B0CB-E711-B800-003048FF9ABC.root",
        # "file:/eos/cms/store/relval/CMSSW_10_0_0_pre1/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v10-v1/10000/02B2350A-B1CB-E711-9604-0025905A60D6.root",
        # "file:/eos/cms/store/relval/CMSSW_10_0_0_pre1/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v10-v1/10000/08F493FF-B5CB-E711-AD3B-0025905B8576.root",
        #"file:/eos/cms/store/relval/CMSSW_10_0_0_pre1/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v10-v1/10000/0E64333A-B6CB-E711-8C67-0CC47A4C8EB6.root",
         "file:/eos/cms/store/relval/CMSSW_10_0_0_pre1/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v10-v1/10000/12A31658-AECB-E711-9625-0CC47A7C3410.root",
         "file:/eos/cms/store/relval/CMSSW_10_0_0_pre1/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v10-v1/10000/16A56D40-AFCB-E711-868A-0CC47A4D7666.root",
         "file:/eos/cms/store/relval/CMSSW_10_0_0_pre1/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v10-v1/10000/1809A88C-AECB-E711-9C70-0CC47A78A2EC.root",
         "file:/eos/cms/store/relval/CMSSW_10_0_0_pre1/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v10-v1/10000/2E7C28F9-B5CB-E711-B6FB-0025905B85EE.root",
         "file:/eos/cms/store/relval/CMSSW_10_0_0_pre1/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v10-v1/10000/301D06C6-AECB-E711-979F-0CC47A4D769A.root"
        ),
                            secondaryFileNames = cms.untracked.vstring()
                            )

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('reco nevts:1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string(''),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:temp.root'),
    outputCommands = process.FEVTDEBUGEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2017_realistic', '')

process.load("Configuration.StandardSequences.RawToDigi_Data_cff")

process.hcalDigis.UnpackZDC = cms.untracked.bool(False)

process.hcalLocalRecoSequence.remove(process.zdcreco)
process.hcalLocalRecoSequence.remove(process.hfprereco)
process.hcalLocalRecoSequence.remove(process.horeco)
process.hcalLocalRecoSequence.remove(process.hfreco)

process.hbheprereco.algorithm.useM2=cms.bool(True)
process.hbheprereco.algorithm.useM3=cms.bool(True)
process.hbheprereco.algorithm.useMahi=cms.bool(True)

process.hbheprereco.processQIE11 = cms.bool(False)
process.hbheprereco.processQIE8 = cms.bool(True)
process.hbheprereco.digiLabelQIE8 = cms.InputTag("simHcalDigis")
process.hbheprereco.digiLabelQIE11 = cms.InputTag("simHcalDigis")

process.load("RecoLocalCalo.HcalRecProducers.hbheplan1_cfi") #import hbheplan1

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.hcalDigis)
process.reconstruction_step = cms.Path(process.hcalLocalRecoSequence+process.hbheplan1)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGoutput_step = cms.EndPath(process.FEVTDEBUGoutput)

process.dump=cms.EDAnalyzer('EventContentAnalyzer')
process.dump_step = cms.Path(process.dump)

process.flat = cms.EDAnalyzer('TupleMaker')

process.TFileService = cms.Service(
    "TFileService",
    fileName = cms.string("MC_flatQCD_HPD.root")
    )

process.flat_step = cms.Path(process.flat)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,
                                process.reconstruction_step,
                                #process.dump_step,
                                process.flat_step,
                                #process.m2_step, process.m3_step, process.mahi_step,
                                process.endjob_step)
#process.FEVTDEBUGoutput_step)

#from Configuration.DataProcessing.Utils import addMonitoring
#process = addMonitoring(process)

#if 'FastTimerService' in process.__dict__:
#    del process.FastTimerService
#
#process.load("HLTrigger.Timer.FastTimerService_cfi")
