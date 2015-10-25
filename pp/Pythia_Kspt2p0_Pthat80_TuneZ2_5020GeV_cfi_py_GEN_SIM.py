# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: fragmentfile/inclusiveD/python/Pythia_D0pt15p0_Pthat15_TuneZ2_5020GeV_cfi.py --conditions auto:run2_mc --eventcontent RAWSIM -s GEN,SIM --datatier GEN-SIM --beamspot NominalCollision2015 --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedNominalCollision2015_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(25000) #to get around ~100 output
#     output = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('fragmentfile/inclusiveD/python/Pythia_D0pt15p0_Pthat15_TuneZ2_5020GeV_cfi.py nevts:1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('Pythia_Kspt2p0_Pthat80_TuneZ2_5020GeV_cfi_py_GEN_SIM.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')

process.D0filter = cms.EDFilter("MCSingleParticleFilter",
    MaxEta = cms.untracked.vdouble(2.4, 2.4),
    MinEta = cms.untracked.vdouble(-2.4, -2.4),
    MinPt = cms.untracked.vdouble(2.0, 2.0),
    ParticleID = cms.untracked.vint32(310, 310)
)


process.generator = cms.EDFilter("Pythia6GeneratorFilter",
    ExternalDecays = cms.PSet(
        EvtGen = cms.untracked.PSet(
            decay_table = cms.FileInPath('GeneratorInterface/ExternalDecays/data/DECAY_NOLONGLIFE.DEC'),
            list_forced_decays = cms.vstring('myD0', 
                'myanti-D0'),
            operates_on_particles = cms.vint32(0),
            particle_property_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/evt.pdl'),
            use_default_decay = cms.untracked.bool(False),
            use_internal_pythia = cms.untracked.bool(False),
            user_decay_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/D0_Kpi.dec')
        ),
        parameterSets = cms.vstring('EvtGen')
    ),
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters'),
        processParameters = cms.vstring('MSEL=1   ! QCD hight pT processes', 
            'CKIN(3)= 15  ! minimum pt hat for hard interactions'),
        pythiaUESettings = cms.vstring('MSTU(21)=1     ! Check on possible errors during program execution', 
            'MSTJ(22)=2     ! Decay those unstable particles', 
            'PARJ(71)=10 .  ! for which ctau  10 mm', 
            'MSTP(33)=0     ! no K factors in hard cross sections', 
            'MSTP(2)=1      ! which order running alphaS', 
            'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)', 
            'MSTP(52)=2     ! work with LHAPDF', 
            'PARP(82)=1.832 ! pt cutoff for multiparton interactions', 
            'PARP(89)=1800. ! sqrts for which PARP82 is set', 
            'PARP(90)=0.275 ! Multiple interactions: rescaling power', 
            'MSTP(95)=6     ! CR (color reconnection parameters)', 
            'PARP(77)=1.016 ! CR', 
            'PARP(78)=0.538 ! CR', 
            'PARP(80)=0.1   ! Prob. colored parton from BBR', 
            'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter', 
            'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter', 
            'PARP(62)=1.025 ! ISR cutoff', 
            'MSTP(91)=1     ! Gaussian primordial kT', 
            'PARP(93)=10.0  ! primordial kT-max', 
            'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default', 
            'MSTP(82)=4     ! Defines the multi-parton model')
    ),
    comEnergy = cms.double(5020.0),
    crossSection = cms.untracked.double(0.2035),
    filterEfficiency = cms.untracked.double(0.09132),
    maxEventsToPrint = cms.untracked.int32(-1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(False)
)


process.ProductionFilterSequence = cms.Sequence(process.generator+process.D0filter)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 


