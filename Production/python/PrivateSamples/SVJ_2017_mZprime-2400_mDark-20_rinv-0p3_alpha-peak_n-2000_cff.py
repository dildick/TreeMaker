import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-1.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-2.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-3.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-4.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-5.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-6.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-7.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-8.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-9.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-10.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-11.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-12.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-13.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-14.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-15.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-16.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-17.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-18.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-19.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-20.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-21.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-22.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-23.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-24.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-25.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-26.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-27.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-28.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-29.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-30.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-31.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-32.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-33.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-34.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-35.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-36.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-37.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-38.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-39.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-40.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-41.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-42.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-43.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-44.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-45.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-46.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-47.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-48.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-49.root',
       '/store/user/lpcsusyhad/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000_part-50.root',
] )
