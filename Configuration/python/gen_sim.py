# Auto generated configuration file
# using: 
# Revision: 1.381.2.28 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: sim_reco -s SIM --conditions auto:mc -n 10 --beamspot Realistic8TeVCollisions --pileup NoPileUp --datamix NODATAMIXER --eventcontent RAWSIM --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('GENSIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
#process.load('Geometry.CMSCommonData.cmsIdealGeometryXML_cfi')
#process.load('Configuration.StandardSequences.GeometryExtended_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)


# Input source
process.source = cms.Source("EmptySource")

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")

process.generator = cms.EDProducer("FlatRandomPtGunProducer",
    PGunParameters = cms.PSet(
        MaxPt = cms.double(100.0),
        MinPt = cms.double(10.0),
        PartID = cms.vint32(22),
        MaxEta = cms.double(3.0),
        MaxPhi = cms.double(3.14159265359),
        MinEta = cms.double(1.48),
        MinPhi = cms.double(-3.14159265359)
    ),
    Verbosity = cms.untracked.int32(0),
    psethack = cms.string('single gamma pt 10 to 100'),
    AddAntiParticle = cms.bool(False),
    firstRun = cms.untracked.uint32(1)
)




process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.381.2.28 $'),
    annotation = cms.untracked.string('sim_reco nevts:10'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('singleGammaFlatPt10To100.root'),
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
process.generation_step = cms.Path(process.generator)
process.simulation_step = cms.Path(process.psim)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step, process.simulation_step, process.endjob_step, process.RAWSIMoutput_step)

