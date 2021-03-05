# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideCandidateModules#Analyzer_Modules

import FWCore.ParameterSet.Config as cms
process = cms.Process("ParticleTree")

from Configuration.AlCa.autoCond import autoCond
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = '92X_upgrade2017_realistic_v7'
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        # madgraph samples
        #'/store/mc/RunIISummer19UL17MiniAOD/VBFHToGG_M125_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/D0784E65-9A11-B744-B773-FBE5C851B227.root',
        '/store/mc/RunIIAutumn18MiniAOD/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/01177A57-504C-4C47-9259-D60A8FB0B5CB.root', 
    ),
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(5)
)


process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.printList = cms.EDAnalyzer("ParticleListDrawer",
  maxEventsToPrint = cms.untracked.int32(100),
  printVertex = cms.untracked.bool(False),
  printOnlyHardInteraction = cms.untracked.bool(False), # Print only status=3 particles. This will not work for Pythia8, which does not have any such particles.
  src = cms.InputTag("prunedGenParticles") 
)

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.printTree = cms.EDAnalyzer("ParticleTreeDrawer",
                                   src = cms.InputTag("prunedGenParticles"),                                                                 
                                   printP4 = cms.untracked.bool(False),
                                   printPtEtaPhi = cms.untracked.bool(False),
                                   printVertex = cms.untracked.bool(False),
                                   printStatus = cms.untracked.bool(True),
                                   printIndex = cms.untracked.bool(True),
                                   printOnlyHardInteraction = cms.untracked.bool(False) 
                                   )


process.p = cms.Path(
    process.printList *
    process.printTree
)
