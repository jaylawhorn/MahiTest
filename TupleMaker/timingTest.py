# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: reco -s RAW2DIGI,RECO --filein file:pickevents.root --fileout file:useless.root --conditions 92X_dataRun2_HLT_v7 --eventcontent FEVTDEBUG
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO2')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.MessageLogger.categories.append('FastReport')
process.MessageLogger.cerr.FastReport = cms.untracked.PSet( limit = cms.untracked.int32(10000000) )
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
        #"file:/eos/cms/tier0/store/data/Run2017F/HTMHT/RAW/v1/000/305/809/00000/BE1E948E-88BB-E711-AD99-02163E01A6F2.root",
        "file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/0421C5DB-A5B9-E711-8713-0CC47A7C34C8.root",
        "file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/0E1E29D8-A7B9-E711-8873-0CC47A7C354C.root",
        "file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/168847F2-A7B9-E711-8C20-0CC47A7C35D8.root",
        #"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/22E3CF32-A5B9-E711-99F2-0025905A60BC.root",
        #"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/3689DD7F-A9B9-E711-B148-0CC47A4D7690.root",
        #"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/3890021A-A5B9-E711-9CB2-0CC47A4D7628.root",
        #"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/48065BEF-A5B9-E711-AD66-0CC47A4D7698.root",
        #"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/4C4CA5E3-A4B9-E711-A145-0CC47A7C3612.root",
        #"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/4CAC944E-A9B9-E711-BAC0-0CC47A4C8E98.root",
        #"file:/eos/cms/store/relval/CMSSW_9_4_0_pre3/RelValQCD_FlatPt_15_3000HS_13/GEN-SIM-DIGI-RAW/94X_mc2017_realistic_v4-v1/10000/50185785-A9B9-E711-A296-0025905A611C.root"
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
#process.GlobalTag = GlobalTag(process.GlobalTag, '92X_dataRun2_Prompt_v10', '')
process.GlobalTag = GlobalTag(process.GlobalTag, '92X_upgrade2017_realistic_v7', '')

process.load("Configuration.StandardSequences.RawToDigi_Data_cff")

process.hcalDigis.UnpackZDC = cms.untracked.bool(False)

process.mahiprereco = process.hbheprereco.clone()
process.m3prereco = process.hbheprereco.clone()

process.mahiprereco.processQIE11 = cms.bool(True)
process.mahiprereco.processQIE8 = cms.bool(True)
process.hbheprereco.processQIE11 = cms.bool(True)
process.hbheprereco.processQIE8 = cms.bool(True)
process.m3prereco.processQIE11 = cms.bool(True)
process.m3prereco.processQIE8 = cms.bool(True)

process.mahiprereco.algorithm.useM2=cms.bool(False)
process.mahiprereco.algorithm.useM3=cms.bool(False)
process.mahiprereco.algorithm.useMahi=cms.bool(True)

process.hbheprereco.algorithm.useM2=cms.bool(True)
process.hbheprereco.algorithm.useM3=cms.bool(False)
process.hbheprereco.algorithm.useMahi=cms.bool(False)

process.m3prereco.algorithm.useM2=cms.bool(False)
process.m3prereco.algorithm.useM3=cms.bool(True)
process.m3prereco.algorithm.useMahi=cms.bool(False)

process.hbheprereco.digiLabelQIE8 = cms.InputTag("simHcalDigis")
process.hbheprereco.digiLabelQIE11 = cms.InputTag("simHcalDigis","HBHEQIE11DigiCollection")

process.mahiprereco.digiLabelQIE8 = cms.InputTag("simHcalDigis")
process.mahiprereco.digiLabelQIE11 = cms.InputTag("simHcalDigis","HBHEQIE11DigiCollection")

process.m3prereco.digiLabelQIE8 = cms.InputTag("simHcalDigis")
process.m3prereco.digiLabelQIE11 = cms.InputTag("simHcalDigis","HBHEQIE11DigiCollection")


process.load("RecoLocalCalo.HcalRecProducers.hbheplan1_cfi") #import hbheplan1

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.hcalDigis)
process.m2_step = cms.Path(process.hbheprereco)
process.m3_step = cms.Path(process.m3prereco)
process.mahi_step = cms.Path(process.mahiprereco)
    #process.hcalLocalRecoSequence+
    #process.hbheplan1
     #                                  )

process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGoutput_step = cms.EndPath(process.FEVTDEBUGoutput)

process.flat = cms.EDAnalyzer('TupleMaker')

process.TFileService = cms.Service(
    "TFileService",
    fileName = cms.string("temp.root")
    )

process.flat_step = cms.Path(process.flat)

process.dump=cms.EDAnalyzer('EventContentAnalyzer')
process.dump_step = cms.Path(process.dump)


# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,
                                #process.reconstruction_step,
                                process.m3_step,
                                process.mahi_step,
                                process.m2_step,
                                #process.dump_step,
                                process.flat_step,
                                process.endjob_step)

#from Configuration.DataProcessing.Utils import addMonitoring
#process = addMonitoring(process)

if 'FastTimerService' in process.__dict__:
    del process.FastTimerService

process.load("HLTrigger.Timer.FastTimerService_cfi")

#process.FastTimerService.printEventSummary =True
#process.FastTimerService.printRunSummary =True
#process.FastTimerService.printJobSummary =True
#
#process.FastTimerService.enableDQM = True
#
#process.FastTimerService.enableDQMbyModule = True
#process.FastTimerService.dqmPath = "HLT/TimerService"
#
#process.load("DQMServices.Components.fastTimerServiceClient_cfi")
#process.fastTimerServiceClient.dqmPath = "HLT/TimerService"
#
#process.load("DQMServices.Components.DQMFileSaver_cfi")
#process.dqmSaver.workflow = "/HLT/FastTimerService/All"
#
#process.DQMFileSaverOutput = cms.EndPath ( process.fastTimerServiceClient + process.dqmSaver)
