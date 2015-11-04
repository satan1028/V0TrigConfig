# V0 Trigger Config
Pythia 8 config:


git clone git://github.com/satan1028/V0TrigConfig.git

mv V0TrigConfig/Pythia8/V0fragmentfile/ V0TrigConfig/

scram b


1. pp configuration:

Ks GEN-SIM:

cmsDriver.py V0TrigConfig/V0fragmentfile/python/Pythia8_Kspt1p0_Pthat80_TuneCUETP8M1_5020GeV_cfi.py -n 20000 --conditions auto:run2_mc --eventcontent RAWSIM -s GEN,SIM --datatier GEN-SIM --beamspot NominalHICollision2015 --no_exec

Lamda GEN-SIM:

cmsDriver.py V0TrigConfig/V0fragmentfile/python/Pythia8_Lamdapt1p0_Pthat80_TuneCUETP8M1_5020GeV_cfi.py -n 20000 --conditions auto:run2_mc --eventcontent RAWSIM -s GEN,SIM --datatier GEN-SIM --beamspot NominalHICollision2015 --no_exec

Step2:

cmsDriver.py step2 --conditions auto:run2_mc -n 10 --eventcontent RAWSIM -s DIGI:pdigi_valid,L1,DIGI2RAW,HLT:Fake,RAW2DIGI,L1Reco --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --no_exec

2 PbPb configuration:

Ks GEN-SIM:

cmsDriver.py V0TrigConfig/V0fragmentfile/python/Pythia8_Kspt1p0_Pthat80_TuneCUETP8M1_5020GeV_cfi.py --conditions auto:run2_mc_HIon -s GEN,SIM --pileup_input das:/Hydjet_Quenched_MinBias_5020GeV_750/HiFall15-75X_mcRun2_HeavyIon_v1_75X_mcRun2_HeavyIon_v1-v1/GEN-SIM -n 10 --eventcontent RAWSIM --scenario HeavyIons --pileup HiMixGEN --datatier GEN-SIM --beamspot MatchHI --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1_HI --pileup_dasoption "--limit 0" --no_exec

Lamda GEN-SIM:

cmsDriver.py V0TrigConfig/V0fragmentfile/python/Pythia8_Lamdapt1p0_Pthat80_TuneCUETP8M1_5020GeV_cfi.py --conditions auto:run2_mc_HIon -s GEN,SIM --pileup_input das:/Hydjet_Quenched_MinBias_5020GeV_750/HiFall15-75X_mcRun2_HeavyIon_v1_75X_mcRun2_HeavyIon_v1-v1/GEN-SIM -n 10 --eventcontent RAWSIM --scenario HeavyIons --pileup HiMixGEN --datatier GEN-SIM --beamspot MatchHI --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1_HI --pileup_dasoption "--limit 0" --no_exec


Step2:
cmsDriver.py step2 --conditions auto:run2_mc_HIon --scenario HeavyIons --pileup_input das:/Hydjet_Quenched_MinBias_5020GeV/HiFall14-START71_V1-v2/GEN-SIM --pileup_dasoption "--limit 0" -n -1 --eventcontent RAWSIM -s DIGI:pdigi_valid,L1,DIGI2RAW,HLT:HIon,RAW2DIGI,L1Reco --datatier GEN-SIM-DIGI-RAW --pileup HiMix --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1_HI --filein file:Pyquen_Unquenched_AllQCDPhoton30_PhotonFilter20GeV_eta24_TuneZ2_PbPb_5020GeV_cfi_py_GEN_SIM_PU.root --no_exec

