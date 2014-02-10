# Auto generated configuration file
# using: 
# Revision: 1.381.2.28 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: sim_reco_DIGI_RECO -s DIGI,DIGI2RAW,RAW2DIGI,RECO --conditions auto:mc -n 10 --beamspot Realistic8TeVCollisions --pileup NoPileUp --datamix NODATAMIXER --eventcontent RECOSIM --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
#process.load('Geometry.CMSCommonData.cmsIdealGeometryXML_cfi')
process.load('Configuration.StandardSequences.GeometryExtended_cff')

#process.load('Geometry.CaloEventSetup.CaloTopology_cfi')
#process.load('Geometry.CaloEventSetup.CaloGeometry_cff')
#process.load('Geometry.CaloEventSetup.EcalTrigTowerConstituents_cfi')
#process.load('Geometry.EcalMapping.EcalMapping_cfi')
#process.load('Geometry.EcalMapping.EcalMappingRecord_cfi')
#process.load('Geometry.CommonDetUnit.globalTrackingGeometryDB_cfi')
#process.load('RecoTracker.GeometryESProducer.TrackerRecoGeometryESProducer_cfi')
#process.load('RecoMuon.DetLayers.muonDetLayerGeometry_cfi')
#process.load('Geometry.TrackerGeometryBuilder.idealForDigiTrackerGeometryDB_cff')
process.load('Geometry.CSCGeometryBuilder.idealForDigiCscGeometryDB_cff')
#process.load('Geometry.DTGeometryBuilder.idealForDigiDtGeometryDB_cff')


process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring(
            'file:singleGammaFlatPt10To100.root'
            )
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.381.2.28 $'),
    annotation = cms.untracked.string('sim_reco_DIGI_RECO nevts:10'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RECOSIMEventContent.outputCommands,
#   fileName = cms.untracked.string('sim_reco_DIGI_RECO_DIGI_DIGI2RAW_RAW2DIGI_RECO.root'),
    fileName = cms.untracked.string('singleGammaFlatPt10To100_RECOSIM.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('')
    )
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:mc', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step,process.raw2digi_step,process.reconstruction_step,process.endjob_step,process.RECOSIMoutput_step)
