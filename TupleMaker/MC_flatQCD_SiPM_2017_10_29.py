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
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/0421C5DB-A5B9-E711-8713-0CC47A7C34C8.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/0E1E29D8-A7B9-E711-8873-0CC47A7C354C.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/168847F2-A7B9-E711-8C20-0CC47A7C35D8.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/22E3CF32-A5B9-E711-99F2-0025905A60BC.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/3689DD7F-A9B9-E711-B148-0CC47A4D7690.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/3890021A-A5B9-E711-9CB2-0CC47A4D7628.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/48065BEF-A5B9-E711-AD66-0CC47A4D7698.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/4C4CA5E3-A4B9-E711-A145-0CC47A7C3612.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/4CAC944E-A9B9-E711-BAC0-0CC47A4C8E98.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/50185785-A9B9-E711-A296-0025905A611C.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/54320DAB-A5B9-E711-8189-0CC47A7C340C.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/54B00EF7-A7B9-E711-83B9-0025905A605E.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/58DE628E-A8B9-E711-B6E3-0CC47A7C34A0.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/5A0B15E2-A5B9-E711-B633-00248C55CC9D.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/5A0F9013-A5B9-E711-B489-0CC47A4C8F12.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/68719B7F-A9B9-E711-8CC1-0CC47A4D7628.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/6C2C504F-A7B9-E711-9E6F-0025905B8600.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/6CB165ED-A5B9-E711-9435-0CC47A4D763C.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/70B8AA77-A8B9-E711-8C33-0CC47A4C8F08.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/76CBF73A-ACB9-E711-9F15-0CC47A4D75F4.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/787B3CF6-A4B9-E711-A595-0CC47A4C8E82.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/7895751B-A5B9-E711-82E4-0CC47A7C3638.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/7A053B4E-A9B9-E711-BC42-0025905B855A.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/7AEDA5F5-A4B9-E711-9E6E-0CC47A4D7628.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/7C7CA485-A8B9-E711-9D76-0CC47A78A456.root",
"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/7EF9EE49-A7B9-E711-AED4-0CC47A78A3F8.root"
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
