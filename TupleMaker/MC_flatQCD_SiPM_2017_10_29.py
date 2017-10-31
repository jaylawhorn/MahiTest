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
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v4-v1/10000/04EE54D5-1BBB-E711-8309-0CC47A4C8EC6.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v4-v1/10000/068DAFCA-1BBB-E711-9CB8-0025905B85F6.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v4-v1/10000/122386D4-1BBB-E711-8C95-0CC47A78A340.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v4-v1/10000/12DEE3E9-1FBB-E711-B1FD-0CC47A4C8E64.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v4-v1/10000/18ACF066-1CBB-E711-A1E3-0CC47A78A408.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v4-v1/10000/1E518EE6-1CBB-E711-B652-0025905A60A0.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v4-v1/10000/2042E3D1-1BBB-E711-8006-0CC47A745298.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v4-v1/10000/2049D5E6-1CBB-E711-B03B-0CC47A78A340.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v4-v1/10000/2C7ADDCA-1BBB-E711-9CD4-0025905B8568.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v4-v1/10000/30872D69-1CBB-E711-A334-0CC47A7C34D0.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v4-v1/10000/3090D954-1CBB-E711-9468-0CC47A78A2EC.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v4-v1/10000/3258D0F2-1CBB-E711-878E-0CC47A4C8EC6.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v4-v1/10000/38095F5D-1CBB-E711-BC0C-0025905B85BC.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v4-v1/10000/428FB25B-1CBB-E711-8C3B-0CC47A74527A.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v4-v1/10000/42C961D7-1BBB-E711-B166-0CC47A7C345C.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v4-v1/10000/4E394DD4-1BBB-E711-8187-0CC47A78A3F8.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v4-v1/10000/562DA7D8-1BBB-E711-875F-0CC47A7C35F8.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v4-v1/10000/5AB0A2D3-1BBB-E711-AF30-0CC47A7C3424.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v4-v1/10000/5CFEC7E4-1CBB-E711-B402-0025905B85AA.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v4-v1/10000/6069985F-1CBB-E711-9775-0CC47A4D7662.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v4-v1/10000/621A53E2-1CBB-E711-8E91-0025905B8582.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v4-v1/10000/6A747950-1CBB-E711-82B9-0025905A60CE.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v4-v1/10000/78A606CA-1BBB-E711-8307-0025905B8596.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/PU25ns_94X_mc2017_realistic_v4-v1/10000/80BBB8BE-1BBB-E711-BD2D-0CC47A7C35A8.root"
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
#process.GlobalTag = GlobalTag(process.GlobalTag, '92X_dataRun2_Prompt_v9', '')
process.GlobalTag = GlobalTag(process.GlobalTag, '92X_upgrade2017_realistic_v7', '')

process.load("Configuration.StandardSequences.RawToDigi_Data_cff")

process.hcalDigis.UnpackZDC = cms.untracked.bool(False)

process.hcalLocalRecoSequence.remove(process.zdcreco)
process.hbheprereco.processQIE11 = cms.bool(True)
process.hbheprereco.processQIE8 = cms.bool(False)
process.hbheprereco.digiLabelQIE8 = cms.InputTag("simHcalDigis")
process.hbheprereco.digiLabelQIE11 = cms.InputTag("simHcalDigis","HBHEQIE11DigiCollection")

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
    fileName = cms.string("MC_flatQCD_SiPM_2017_10_29.root")
    )

process.flat_step = cms.Path(process.flat)


# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,
                                process.reconstruction_step,
                                #process.dump_step,
                                process.flat_step,
                                process.endjob_step)
#process.FEVTDEBUGoutput_step)

#from Configuration.DataProcessing.Utils import addMonitoring
#process = addMonitoring(process)
