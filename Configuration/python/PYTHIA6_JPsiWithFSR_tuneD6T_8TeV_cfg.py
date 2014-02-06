# Auto generated configuration file
# using:
# Revision: 1.381.2.18
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v
# with command line options: Configuration/GenProduction/python/EightTeV/PYTHIA6_JPsiWithFSR_tuneD6T_8TeV_cff.py -s GEN,FASTSIM,HLT --pileup=LowLumiPileUp --conditions auto:mc --eventcontent=RECO --datatier GEN-SIM-DIGI-RECO -n 10
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')

# seed generation
import random
seed1 = random.randint(0, 900000000)
seed2 = random.randint(0, 900000000)
seed3 = random.randint(0, 900000000)
seed4 = random.randint(0, 900000000)
print "Initial seeds for random number service:"
print "  generator  = ", seed1
print "  VtxSmeared = ", seed2
print "  g4SimHits  = ", seed3
print "  mix        = ", seed4
process.RandomNumberGeneratorService.generator.initialSeed  = seed1
process.RandomNumberGeneratorService.VtxSmeared.initialSeed = seed2
process.RandomNumberGeneratorService.g4SimHits.initialSeed  = seed3
process.RandomNumberGeneratorService.mix.initialSeed        = seed4

process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('FastSimulation.Configuration.EventContent_cff')
#process.load('FastSimulation.PileUpProducer.PileUpSimulator_LowLumiPileUp_cff')
#process.load('Configuration.GenProduction.EightTeV.PileUpSimulator_2012_S10_inTimeOnly_cff')
process.load('FastSimulation.PileUpProducer.PileUpSimulator_2012_Summer_inTimeOnly_cff')
process.load('FastSimulation.Configuration.Geometries_START_cff')
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('FastSimulation.Configuration.FamosSequences_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedParameters_cfi')
process.load('HLTrigger.Configuration.HLT_7E33v2_Famos_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(100000)
        )

process.MessageLogger.cerr.FwkReport.reportEvery = 100

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

    )

# Production Info
process.configurationMetadata = cms.untracked.PSet(
        version = cms.untracked.string('$Revision: 1.1 $'),
            annotation = cms.untracked.string('Summer09: Pythia6 generation of prompt JPsi, 7TeV, D6T tune'),
            name = cms.untracked.string('$Source: /local/reps/CMSSW/CMSSW/Configuration/GenProduction/python/EightTeV/PYTHIA6_JPsiWithFSR_tuneD6T_8TeV_cff.py,v $')
        )

# Output definition

process.RECOoutput = cms.OutputModule("PoolOutputModule",
                                          splitLevel = cms.untracked.int32(0),
                                          eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
                                          outputCommands = process.AODSIMEventContent.outputCommands,
                                          fileName = cms.untracked.string('jpsiee_GEN_FASTSIM_HLT_PUS10.root'),
                                          dataset = cms.untracked.PSet(
            filterName = cms.untracked.string(''),
                    dataTier = cms.untracked.string('AODSIM')
                ),
                                          SelectEvents = cms.untracked.PSet(
            SelectEvents = cms.vstring('generation_step')
                )
                                      )

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
process.famosSimHits.SimulateCalorimetry = True
process.famosSimHits.SimulateTracking = True
process.simulation = cms.Sequence(process.simulationWithFamos)
process.HLTEndSequence = cms.Sequence(process.reconstructionWithFamos)
process.Realistic8TeVCollisionVtxSmearingParameters.type = cms.string("BetaFunc")
process.famosSimHits.VertexGenerator = process.Realistic8TeVCollisionVtxSmearingParameters
process.famosPileUp.VertexGenerator = process.Realistic8TeVCollisionVtxSmearingParameters
process.GlobalTag.globaltag = 'START53_V7C::All'

process.oniafilter = cms.EDFilter("PythiaFilter",
                                      MaxEta = cms.untracked.double(1e+100),
                                      Status = cms.untracked.int32(2),
                                      MinEta = cms.untracked.double(-1e+100),
                                      MinPt = cms.untracked.double(5.0),
                                      ParticleID = cms.untracked.int32(443)
                                  )


process.generator = cms.EDFilter("Pythia6GeneratorFilter",
                                     ExternalDecays = cms.PSet(
            EvtGen = cms.untracked.PSet(
                use_default_decay = cms.untracked.bool(False),
                            decay_table = cms.FileInPath('GeneratorInterface/ExternalDecays/data/DECAY_NOLONGLIFE.DEC'),
                            particle_property_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/evt.pdl'),
                            user_decay_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/Onia_ee.dec'),
                            list_forced_decays = cms.vstring('MyJ/psi'),
                            operates_on_particles = cms.vint32(0)
                        ),
                    parameterSets = cms.vstring('EvtGen')
                ),
                                     pythiaPylistVerbosity = cms.untracked.int32(0),
                                     filterEfficiency = cms.untracked.double(0.0463),
                                     pythiaHepMCVerbosity = cms.untracked.bool(False),
                                     comEnergy = cms.double(8000.0),
                                     crossSection = cms.untracked.double(13775390),
                                     maxEventsToPrint = cms.untracked.int32(0),
                                     PythiaParameters = cms.PSet(
            pythiaUESettings = cms.vstring('MSTJ(11)=3     ! Choice of the fragmentation function',
                                                       'MSTJ(22)=2     ! Decay those unstable particles',
                                                       'PARJ(71)=10 .  ! for which ctau  10 mm',
                                                       'MSTP(2)=1      ! which order running alphaS',
                                                       'MSTP(33)=0     ! no K factors in hard cross sections',
                                                       'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)',
                                                       'MSTP(52)=2     ! work with LHAPDF',
                                                       'MSTP(81)=1     ! multiple parton interactions 1 is Pythia default',
                                                       'MSTP(82)=4     ! Defines the multi-parton model',
                                                       'MSTU(21)=1     ! Check on possible errors during program execution',
                                                       'PARP(82)=1.8387   ! pt cutoff for multiparton interactions',
                                                       'PARP(89)=1960. ! sqrts for which PARP82 is set',
                                                       'PARP(83)=0.5   ! Multiple interactions: matter distrbn parameter',
                                                       'PARP(84)=0.4   ! Multiple interactions: matter distribution parameter',
                                                       'PARP(90)=0.16  ! Multiple interactions: rescaling power',
                                                       'PARP(67)=2.5    ! amount of initial-state radiation',
                                                       'PARP(85)=1.0  ! gluon prod. mechanism in MI',
                                                       'PARP(86)=1.0  ! gluon prod. mechanism in MI',
                                                       'PARP(62)=1.25   ! ',
                                                       'PARP(64)=0.2    ! ',
                                                       'MSTP(91)=1      !',
                                                       'PARP(91)=2.1   ! kt distribution',
                                                       'PARP(93)=15.0  ! '),
                    processParameters = cms.vstring('MSEL=61          ! Quarkonia',
                                                                'MDME(858,1) = 1  ! 0.060200    e-    e+',
                                                                'MDME(859,1) = 0  ! 0.060100    mu-  mu+',
                                                                'MDME(860,1) = 0  ! 0.879700    rndmflav        rndmflavbar',
                                                                'MSTP(142)=2      ! turns on the PYEVWT Pt re-weighting routine',
                                                                'PARJ(13)=0.750   ! probability that a c or b meson has S=1',
                                                                'PARJ(14)=0.162   ! probability that a meson with S=0 is produced with L=1, J=1',
                                                                'PARJ(15)=0.018   ! probability that a meson with S=1 is produced with L=1, J=0',
                                                                'PARJ(16)=0.054   ! probability that a meson with S=1 is produced with L=1, J=1',
                                                                'MSTP(145)=0      ! choice of polarization',
                                                                'MSTP(146)=0      ! choice of polarization frame ONLY when mstp(145)=1',
                                                                'MSTP(147)=0      ! particular helicity or density matrix component when mstp(145)=1',
                                                                'MSTP(148)=1      ! possibility to allow for final-state shower evolution, extreme case !',
                                                                'MSTP(149)=1      ! if mstp(148)=1, it determines the kinematics of the QQ~3S1(8)->QQ~3S1(8)+g branching',
                                                                'PARP(141)=1.16   ! New values for COM matrix elements',
                                                                'PARP(142)=0.0119 ! New values for COM matrix elements',
                                                                'PARP(143)=0.01   ! New values for COM matrix elements',
                                                                'PARP(144)=0.01   ! New values for COM matrix elements',
                                                                'PARP(145)=0.05   ! New values for COM matrix elements',
                                                                'PARP(146)=9.28   ! New values for COM matrix elements',
                                                                'PARP(147)=0.15   ! New values for COM matrix elements',
                                                                'PARP(148)=0.02   ! New values for COM matrix elements',
                                                                'PARP(149)=0.02   ! New values for COM matrix elements',
                                                                'PARP(150)=0.085  ! New values for COM matrix elements',
                                                                'BRAT(861)=0.202  ! chi_2c->J/psi gamma',
                                                                'BRAT(862)=0.798  ! chi_2c->rndmflav rndmflavbar',
                                                                'BRAT(1501)=0.013 ! chi_0c->J/psi gamma',
                                                                'BRAT(1502)=0.987 ! chi_0c->rndmflav rndmflavbar',
                                                                'BRAT(1555)=0.356 ! chi_1c->J/psi gamma',
                                                                'BRAT(1556)=0.644 ! chi_1c->rndmflav rndmflavbar'),
                    parameterSets = cms.vstring('pythiaUESettings',
                                                            'processParameters',
                                                            'CSAParameters'),
                    CSAParameters = cms.vstring('CSAMODE = 6     ! cross-section reweighted quarkonia')
                )
                                 )


process.eegenfilter = cms.EDFilter("MCParticlePairFilter",
                                       Status = cms.untracked.vint32(1, 1),
                                       MinPt = cms.untracked.vdouble(5.0, 5.0),
                                       MaxEta = cms.untracked.vdouble(2.5, 2.5),
                                       MinEta = cms.untracked.vdouble(-2.5, -2.5),
                                       ParticleCharge = cms.untracked.int32(-1),
                                       MinP = cms.untracked.vdouble(2.5, 2.5),
                                       ParticleID1 = cms.untracked.vint32(11),
                                       ParticleID2 = cms.untracked.vint32(11)
                                   )


process.es_prefer_GlobalTag = cms.ESPrefer('PoolDBESSource','GlobalTag')

process.ProductionFilterSequence = cms.Sequence(process.generator+process.oniafilter+process.eegenfilter)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen_genonly)
process.simulation_step = cms.Path(process.simulationWithFamos)
process.reconstruction = cms.Path(process.reconstructionWithFamos)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.RECOoutput_step = cms.EndPath(process.RECOoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.simulation_step,process.reconstruction,process.RECOoutput_step])
# filter all path with the production filter sequence
for path in process.paths:
    getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions
    
