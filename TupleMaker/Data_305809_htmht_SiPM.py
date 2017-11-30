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
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
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
    input = cms.untracked.int32(50)
)

# Input source
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
        #"/store/data/Run2017F/HTMHT/RAW/v1/000/305/809/00000/62439AF2-78BB-E711-8066-02163E019CC0.root",
        #"/store/data/Run2017F/HTMHT/RAW/v1/000/305/809/00000/72EB8201-79BB-E711-A53A-02163E01A2F5.root",
        #"/store/data/Run2017F/HTMHT/RAW/v1/000/305/809/00000/7A064FEE-83BB-E711-9573-02163E013645.root",
        #"/store/data/Run2017F/HTMHT/RAW/v1/000/305/809/00000/7AB1CE24-87BB-E711-9544-02163E01A5E6.root",
        #"/store/data/Run2017F/HTMHT/RAW/v1/000/305/809/00000/9A6CF309-84BB-E711-A738-02163E01A1EF.root",
        #"/store/data/Run2017F/HTMHT/RAW/v1/000/305/809/00000/A206AA3C-85BB-E711-972C-02163E0139B8.root",
        #"/store/data/Run2017F/HTMHT/RAW/v1/000/305/809/00000/BE1E948E-88BB-E711-AD99-02163E01A6F2.root",
        #"/store/data/Run2017F/HTMHT/RAW/v1/000/305/809/00000/DE6CDE38-8ABB-E711-96A8-02163E01344D.root",
        "/store/data/Run2017F/HTMHT/RAW/v1/000/305/809/00000/E001CFB7-88BB-E711-9408-02163E0143F6.root",
        "/store/data/Run2017F/HTMHT/RAW/v1/000/305/809/00000/E444E08D-82BB-E711-83CE-02163E0146E6.root",
        "/store/data/Run2017F/HTMHT/RAW/v1/000/305/809/00000/E63BA5A2-82BB-E711-A248-02163E01A6E2.root"
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
process.GlobalTag = GlobalTag(process.GlobalTag, '92X_dataRun2_Prompt_v9', '')

process.load("Configuration.StandardSequences.RawToDigi_Data_cff")

process.hcalDigis.UnpackZDC = cms.untracked.bool(False)

process.hcalLocalRecoSequence.remove(process.zdcreco)
process.hcalLocalRecoSequence.remove(process.hfprereco)
process.hcalLocalRecoSequence.remove(process.horeco)
process.hcalLocalRecoSequence.remove(process.hfreco)

process.hbheprereco.processQIE11 = cms.bool(True)
process.hbheprereco.processQIE8 = cms.bool(False)

process.hbheprereco.algorithm.activeBXs=cms.vint32(0)

process.mahi = process.hbheprereco.clone()
process.mahi.algorithm.useM2=cms.bool(False)
process.mahi.algorithm.useM3=cms.bool(False)
process.mahi.algorithm.useMahi=cms.bool(True)

process.met2 = process.hbheprereco.clone()
process.met2.algorithm.useM2=cms.bool(True)
process.met2.algorithm.useM3=cms.bool(False)
process.met2.algorithm.useMahi=cms.bool(False)

process.met3 = process.hbheprereco.clone()
process.met3.algorithm.useM2=cms.bool(False)
process.met3.algorithm.useM3=cms.bool(True)
process.met3.algorithm.useMahi=cms.bool(False)

process.hbheprereco.saveInfos = cms.bool(True)


process.load("RecoLocalCalo.HcalRecProducers.hbheplan1_cfi") #import hbheplan1

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.hcalDigis)
process.reconstruction_step = cms.Path(process.hcalLocalRecoSequence+process.hbheplan1)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGoutput_step = cms.EndPath(process.FEVTDEBUGoutput)

process.m2_step = cms.Path(process.met2)
process.m3_step = cms.Path(process.met3)
process.mahi_step = cms.Path(process.mahi)

process.dump=cms.EDAnalyzer('EventContentAnalyzer')
process.dump_step = cms.Path(process.dump)

process.flat = cms.EDAnalyzer('TupleMaker')

process.TFileService = cms.Service(
    "TFileService",
    fileName = cms.string("testtesttest.root")
    #fileName = cms.string("temp.root")
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
