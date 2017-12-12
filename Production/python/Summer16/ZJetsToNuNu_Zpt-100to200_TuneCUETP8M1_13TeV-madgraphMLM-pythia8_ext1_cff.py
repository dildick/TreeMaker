import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/004B2C20-ADE1-E611-A126-0025901D08B8.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/020A0C8E-BBE2-E611-9D4A-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/02731D41-AEE0-E611-A13B-02163E0139EC.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/04DAA861-DAE0-E611-B6A4-0CC47AA98F98.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/0E23C919-B1E3-E611-B6C7-008CFA1113E8.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/14DD2699-DAE0-E611-8B6B-008CFA197A90.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/16A03704-C7E0-E611-B6CC-001E675A6A63.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/18A40614-79E0-E611-AB42-FA163E2C8B0B.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/1C7B3E85-A7F1-E611-898D-02163E0134D0.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/1EB66359-87E0-E611-84D9-FA163EE0F007.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/2241BBFF-E5E0-E611-AB20-008CFA1CBB34.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/24067A4F-CFE0-E611-BFAA-008CFA110B08.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/265EC56E-8DE0-E611-9A6C-FA163E908961.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/268643E0-CFE0-E611-9AA1-001517F7F504.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/2A0DD289-DAE0-E611-AEB3-001E67A400F0.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/2CA58B61-D2E0-E611-935E-0CC47A13CECE.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/34A0E4B0-E0E0-E611-9E1B-0CC47AD98CF2.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/3633A33E-7CE1-E611-A43E-02163E017651.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/38C3DACD-D8E0-E611-9B92-A4BF01025FF9.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/3CADFE11-88E0-E611-99C9-FA163E29BF36.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/3CC09906-B7E1-E611-AB89-A0369F7FE9FC.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/3EA83415-8EE0-E611-8828-02163E017656.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/3EDC61D3-B4E0-E611-8002-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/428DA2E4-E4E0-E611-BC75-008CFA197CA0.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/46072431-D5E0-E611-BED3-001517F7F504.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/4688A43B-E7E0-E611-B9DE-008CFA197A90.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/4C7EB11C-C6E0-E611-9A20-0CC47AD99052.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/507809E5-9DE0-E611-B07C-FA163E8090B6.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/522CBD0C-9EE0-E611-94B5-FA163E2DA0B3.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/5CBB82D8-EBE0-E611-B0CB-549F35AD8B6E.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/6021BD19-9DE0-E611-8E47-02163E00C57E.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/666BA1E7-8FE1-E611-8B2C-02163E013F32.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/689FE664-AFF1-E611-AB20-02163E019E4B.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/6EA37889-D2E0-E611-BBCD-90B11C0BCC58.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/6EA627E2-D8E3-E611-80F7-ECF4BBE16230.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/7226508F-D2E0-E611-8A8E-008CFA1111A0.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/72EC9F4B-AAE1-E611-8624-0CC47A7C340E.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/76DFBD39-DAE0-E611-B855-0CC47AD98C8A.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/8422764A-CFE0-E611-846E-0CC47AD98C8A.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/8CD71F55-95E0-E611-A851-FA163E9FB4D8.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/92FB4A77-8EE3-E611-BEA6-A4BF010114DB.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/940A4B62-95E0-E611-B792-FA163E14D402.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/9CD3AD8B-8DE0-E611-A26F-02163E015D24.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/9ED30703-97E0-E611-967B-02163E0150EB.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/A261ED25-C0E0-E611-AF0B-FA163EFD23FE.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/A4625013-C7E0-E611-82BE-008CFA110C6C.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/B0C98DCD-CFE0-E611-9455-0CC47AA98B8E.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/B25D6A2F-B8F1-E611-85FF-02163E01A3B1.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/B48E212C-AAE1-E611-91D4-001E67DFF7CB.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/B8FEE3FA-87E0-E611-B8C5-FA163E76892F.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/BA31215A-A7E0-E611-B8FB-FA163E272887.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/BC85EE08-9EE0-E611-8BE8-FA163E26DE73.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/BCC6FD69-A5E1-E611-B57D-0090FAA58824.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/C0B2C4FA-ABE3-E611-8030-0CC47AD98F64.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/C8C1D569-80E1-E611-A4C2-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/C8E926CC-DCE0-E611-966F-1418774121A1.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/CCF1731C-96E2-E611-B649-FA163E6B593C.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/CE8085C6-DCE0-E611-A3A1-0CC47A13CD9C.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/D46BFF5C-95E0-E611-865A-FA163EB64F0F.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/D6D7A1A9-A5E1-E611-A08A-0025905B85D0.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/DA0F5CA9-A6E0-E611-88BE-FA163EB72C5E.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/DE4844C0-A7E4-E611-91E5-001C23C0B763.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/E0772508-7FE0-E611-8A4C-FA163E02238B.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/E83E7B56-C7E3-E611-923B-0CC47A78A478.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/E84ADFA7-E0E0-E611-AAEB-008CFA110C64.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/EAD6414B-CFE0-E611-9874-A4BF01013D80.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/F2CD8427-CAE0-E611-8C87-001E67A40514.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/F6FAF3AF-8DE0-E611-9797-FA163E40486E.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/100000/FAC482D9-C0E0-E611-BD69-A4BF0101DCC9.root',
] )