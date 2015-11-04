import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(5020.0),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(     
            'HardQCD:all = on',
            'PhaseSpace:pTHatMin = 5.', #min pthat
        ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CUEP8M1Settings',
            'processParameters',
        )
    )
)

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)


partonfilter = cms.EDFilter("PythiaFilter",
    ParticleID = cms.untracked.int32(5) # 4 for prompt D0 and 5 for non-prompt D0
	)
##or
#partonfilter = cms.EDFilter("MCSingleParticleFilter",
#                       MaxEta     = cms.untracked.vdouble(999.0, 999.0),
#                       MinEta     = cms.untracked.vdouble(-999.0, -999.0),
#                       MinPt      = cms.untracked.vdouble(0.0, 0.0),
#                       ParticleID = cms.untracked.vint32(4, -4)
#                       )
#

Dfilter = cms.EDFilter("MCSingleParticleFilter",
    MaxEta = cms.untracked.vdouble(2.4, 2.4),
    MinEta = cms.untracked.vdouble(-2.4, -2.4),
    MinPt = cms.untracked.vdouble(5.0, 5.0), #min pt
    ParticleID = cms.untracked.vint32(431, -431)
)

ProductionFilterSequence = cms.Sequence(generator*partonfilter*Dfilter)
