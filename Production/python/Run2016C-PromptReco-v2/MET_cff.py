import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/420/00000/760B30B9-F539-E611-A78D-02163E01207D.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/476/00000/DA69A960-0D3A-E611-931D-02163E011884.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/588/00000/2205A4D4-3D3A-E611-B1A8-02163E0143AD.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/601/00000/B4E8B9CE-763A-E611-B1EE-02163E014196.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/603/00000/A264CCC9-8B3A-E611-9554-02163E014341.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/656/00000/D6C3877E-463B-E611-A4B2-02163E0142D3.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/657/00000/2CC8AEAB-8D3B-E611-9DA7-02163E0137E4.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/657/00000/420FBE99-833B-E611-A4B6-02163E011EAB.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/657/00000/86209668-733B-E611-8E08-02163E0146E5.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/658/00000/1AB9E246-853B-E611-AB24-02163E0135DA.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/658/00000/2ED9F642-8C3B-E611-A668-02163E011EE1.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/658/00000/5635FF79-913B-E611-8A1B-02163E01390F.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/658/00000/628F82C6-883B-E611-8D3B-02163E011CBF.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/658/00000/A8F91F49-C73B-E611-8B4E-02163E014369.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/658/00000/CCB414A8-993B-E611-B3FF-02163E013950.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/658/00000/EE9E172D-833B-E611-8B0B-02163E0136C6.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/659/00000/7404F2E8-A13B-E611-83DD-02163E013466.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/752/00000/2AC39EF4-F63B-E611-A7B7-02163E0140E6.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/757/00000/CC9204A6-4A3C-E611-9688-02163E013913.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/758/00000/3CC78513-3A3C-E611-BF98-02163E011CF6.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/759/00000/FE374D61-4C3C-E611-BD9F-02163E0146DB.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/761/00000/EA345CD2-3D3C-E611-A822-02163E014332.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/763/00000/F284EDDA-503C-E611-9F15-02163E014650.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/764/00000/02E7C8E6-6F3C-E611-9A61-02163E01410D.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/766/00000/163A108A-5A3C-E611-B6BB-02163E014454.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/766/00000/38B5FEAE-813C-E611-902C-02163E01412B.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/767/00000/16F5A87B-473C-E611-8AF9-02163E0144FD.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/768/00000/30996EB7-553C-E611-90BE-02163E0144D2.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/768/00000/9C5DB231-993C-E611-8D20-02163E014778.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/769/00000/88759F45-353C-E611-BAD4-02163E0143B9.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/772/00000/04DCCCBD-7F3C-E611-9D8D-02163E01434E.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/773/00000/E40C08CB-623C-E611-9CFC-02163E014774.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/774/00000/1CA280F5-743C-E611-B5AE-02163E0129EA.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/774/00000/4A2148D5-7F3C-E611-98A5-02163E011ADF.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/774/00000/72FDA5E1-703C-E611-A10F-02163E0129EA.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/774/00000/983CAEAF-8A3C-E611-B9AF-02163E0118C8.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/774/00000/A61068D4-793C-E611-84F9-02163E014682.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/776/00000/04BC6165-8B3C-E611-AC4A-02163E011FDB.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/776/00000/3644D001-BC3C-E611-A991-02163E01465E.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/777/00000/125E7B22-913C-E611-B766-02163E011937.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/777/00000/946EBF40-A13C-E611-9237-02163E013472.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/777/00000/AC96C695-963C-E611-A2DF-02163E012569.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/777/00000/BC03C920-913C-E611-9201-02163E0146B1.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/778/00000/52B86673-E23C-E611-9BD7-02163E01459D.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/778/00000/60DDCCB3-C23C-E611-B01C-02163E01455C.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/778/00000/F0420CAC-C23C-E611-81A2-02163E011FE3.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/781/00000/F2C21FA2-C83C-E611-BE46-02163E0136F4.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/782/00000/327DB0D1-F93C-E611-8A11-02163E01450B.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/782/00000/48E5D6C8-F93C-E611-8A3E-02163E014439.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/782/00000/528A6ECD-F93C-E611-B0A1-02163E01383E.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/782/00000/768B07C9-F93C-E611-A52A-02163E0145D2.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/782/00000/EEDEE0C4-F93C-E611-BF84-02163E0144CC.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/782/00000/FEBBCBD8-F93C-E611-BC8F-02163E01445A.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/783/00000/041F2721-3D3D-E611-BC3A-02163E0140D9.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/783/00000/0C419A24-3D3D-E611-A6A1-02163E0143F4.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/783/00000/34CF2D26-3D3D-E611-A7DD-02163E014755.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/783/00000/48CB0B29-3D3D-E611-87C0-02163E011A16.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/783/00000/5AD1F026-3D3D-E611-8DE9-02163E014566.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/783/00000/9CE48D2F-3D3D-E611-9224-02163E011C64.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/783/00000/C80CEF47-3D3D-E611-8995-02163E0122F8.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/783/00000/CA895823-3D3D-E611-AB9E-02163E01468D.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/783/00000/EE214525-3D3D-E611-9E6B-02163E012AE4.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/828/00000/145ACE4F-763D-E611-8DF1-02163E0145C5.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/828/00000/F8C8DF85-9F3D-E611-8DDC-02163E0124F5.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/829/00000/B25740BA-853D-E611-9D92-02163E014588.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/831/00000/86619F27-A43D-E611-A833-02163E013403.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/831/00000/90409592-823D-E611-9C37-02163E0141F4.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/832/00000/02567405-A43D-E611-96CF-02163E01394A.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/832/00000/4C6BC279-AF3D-E611-9223-02163E0120F5.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/832/00000/88F31EF2-CF3D-E611-B8B9-02163E012691.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/832/00000/B27C66A2-A73D-E611-8EF2-02163E01394C.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/832/00000/B280AA6E-9D3D-E611-86C3-02163E01419D.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/832/00000/BC348D55-AC3D-E611-A5A3-02163E014508.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/832/00000/F659E5A3-B53D-E611-9DF4-02163E014546.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/833/00000/749BEA7A-C93D-E611-B2BB-02163E0135E5.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/833/00000/769C7464-BC3D-E611-B199-02163E014375.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/833/00000/8A1C657C-C03D-E611-8900-02163E013449.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/833/00000/8C40D61B-EE3D-E611-8671-02163E013663.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/834/00000/22D35884-D53D-E611-B2A0-02163E0126C7.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/834/00000/820559F9-E13D-E611-AF73-02163E011E99.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/834/00000/AEC43E83-DC3D-E611-8342-02163E013774.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/834/00000/DC0A7CA4-273E-E611-9DC4-02163E01351E.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/835/00000/F6278E1D-E83D-E611-93B4-02163E014483.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/836/00000/0459835A-1C3E-E611-99AB-02163E011D35.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/836/00000/06632508-1B3E-E611-9BFB-02163E01338C.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/836/00000/10EA4E9D-1B3E-E611-ACBE-02163E01184A.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/836/00000/1AAF3CB8-1B3E-E611-82A0-02163E011FCC.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/836/00000/229AF60A-213E-E611-BE30-02163E014669.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/836/00000/3400FD6C-453E-E611-84FE-02163E0133C5.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/836/00000/502D7FBE-193E-E611-B958-02163E014588.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/836/00000/585F5FE0-193E-E611-B4B4-02163E01472C.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/836/00000/60CCB4B1-193E-E611-9F2A-02163E011E73.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/836/00000/BC3A9A6C-453E-E611-8380-02163E014766.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/836/00000/CC1477AE-193E-E611-A484-02163E011C86.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/836/00000/D250016B-453E-E611-8E59-02163E0141F4.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/836/00000/D405B016-1B3E-E611-AC02-02163E014468.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/836/00000/DA1A04BD-193E-E611-BA1B-02163E0128BB.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/837/00000/1CEC77B9-953E-E611-89CA-02163E014258.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/837/00000/766318DE-953E-E611-8D72-02163E0141C5.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/837/00000/848DE2BD-953E-E611-937C-02163E01433E.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/837/00000/8C5ED9B6-953E-E611-86BF-02163E011833.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/837/00000/981EEAB1-953E-E611-999F-02163E014332.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/838/00000/9AF2071A-713E-E611-BF71-02163E013648.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/841/00000/74D4873C-7C3E-E611-99F6-02163E0143C9.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/846/00000/EE20FC77-793E-E611-9A6E-02163E012381.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/847/00000/06B5978E-B13E-E611-BF69-02163E0141FF.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/847/00000/224DAC7F-B13E-E611-86CA-02163E0144C8.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/847/00000/2C06B676-B13E-E611-A76E-02163E014540.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/847/00000/4C334081-B13E-E611-B952-02163E014536.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/847/00000/68B10F90-B13E-E611-B65F-02163E012994.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/847/00000/6E98B179-B13E-E611-BB51-02163E0145BD.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/847/00000/746BE8EE-863E-E611-872F-02163E011FB9.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/847/00000/8C08AC82-B13E-E611-8706-02163E014409.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/847/00000/A6660890-B13E-E611-9610-02163E014369.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/847/00000/EA46A67D-B13E-E611-871E-02163E013513.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/886/00000/FA1EB9F0-ED3E-E611-BD0E-02163E01415D.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/887/00000/088AB6E2-0C3F-E611-977A-02163E013706.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/890/00000/069037A7-813F-E611-8C5A-02163E013732.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/890/00000/1639E8CA-853F-E611-A90D-02163E0133B3.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/890/00000/3E1B6660-863F-E611-AC3C-02163E01394C.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/890/00000/66C44E7B-893F-E611-A506-02163E012262.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/890/00000/6CB2C7E7-8C3F-E611-98BA-02163E0133E4.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/890/00000/78AA25EA-913F-E611-9268-02163E011CAC.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/890/00000/7CA83E87-7F3F-E611-8818-02163E014409.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/890/00000/7EFFC436-A03F-E611-903D-02163E011A78.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/890/00000/9210AD9D-773F-E611-8931-02163E012554.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/890/00000/9CC8829A-7E3F-E611-991D-02163E011CB6.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/890/00000/A6BC2D90-803F-E611-B392-02163E0145CC.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/890/00000/A841FE97-AD3F-E611-B555-02163E012AE4.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/890/00000/B6E33608-7D3F-E611-907E-02163E014683.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/890/00000/CC2D22AD-873F-E611-A1CF-02163E014774.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/890/00000/E66FEDD4-833F-E611-AE4A-02163E0142EB.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/890/00000/EC31ADA4-813F-E611-93DD-02163E0133B3.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/890/00000/EC7689CD-823F-E611-9E89-02163E01261B.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/890/00000/F2832BD0-843F-E611-AE34-02163E012179.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/911/00000/52186D59-9D3F-E611-914F-02163E01460B.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/911/00000/7C3D7731-C13F-E611-824D-02163E011CBF.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/911/00000/8EAEF8AF-AC3F-E611-B1B4-02163E01278F.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/911/00000/9E2DE873-A13F-E611-A4EB-02163E01478C.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/911/00000/B24D3EB2-A63F-E611-B3FE-02163E01278F.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/911/00000/F2C0AFF9-A33F-E611-B458-02163E0140ED.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/912/00000/808575D5-D73F-E611-ADB3-02163E01383E.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/912/00000/A2B2D2B6-C23F-E611-A727-02163E011857.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/912/00000/B6F1A03B-C73F-E611-B2A0-02163E014304.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/912/00000/D83E714E-CA3F-E611-A007-02163E0133CD.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/913/00000/0626CDDD-0040-E611-9756-02163E012336.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/913/00000/184C5780-DD3F-E611-AC53-02163E01338C.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/913/00000/1A0EA225-D93F-E611-AA45-02163E014304.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/913/00000/6C174D9F-E03F-E611-9720-02163E014276.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/913/00000/8EA87087-DB3F-E611-9AC6-02163E011BF5.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/913/00000/BEBD8E84-E43F-E611-8648-02163E012A2B.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/918/00000/7E056E3B-0540-E611-BFA9-02163E01265E.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/918/00000/BCB62DCE-FF3F-E611-909F-02163E013558.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/918/00000/E2875BA0-0840-E611-99A2-02163E011D75.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/918/00000/FA0C2E74-1040-E611-8F51-02163E011FC3.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/920/00000/00F03148-3640-E611-96A5-02163E013950.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/920/00000/08168959-3640-E611-B623-02163E013571.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/920/00000/40A0814E-3640-E611-906D-02163E014522.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/920/00000/687D4D55-3640-E611-A402-02163E0141C2.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/921/00000/7AA78EF9-2D40-E611-B04D-02163E0134CD.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/922/00000/BA084CBB-F93F-E611-97BE-02163E01410A.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/923/00000/8CF328BD-3540-E611-A2D5-02163E01387A.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/931/00000/BE652004-3540-E611-8B6D-02163E0143F7.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/958/00000/20D6B334-0840-E611-9944-02163E0134A1.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/960/00000/AA6FCBA9-0C40-E611-A328-02163E014414.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/963/00000/68208439-3C40-E611-ACD4-02163E011963.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/275/963/00000/C65AAD16-4D40-E611-BB80-02163E0135D0.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/049/00000/0A6929FC-6B40-E611-A8D7-02163E0141C3.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/062/00000/BAEA14B5-7C40-E611-8C33-02163E0123AE.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/063/00000/3054EE3C-7D40-E611-A45C-02163E013570.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/064/00000/D6DA010A-8440-E611-BBF6-02163E01361B.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/071/00000/964CA665-8440-E611-B779-02163E01440F.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/072/00000/AC8CC87F-8340-E611-865A-02163E01390E.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/074/00000/00ADB873-8540-E611-B887-02163E01365F.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/092/00000/1ADA89EB-0341-E611-9EC3-02163E0121C9.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/092/00000/38533B26-EA40-E611-8891-02163E0135EA.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/095/00000/EAAEE357-C640-E611-BC70-02163E014429.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/097/00000/04E3AD83-2241-E611-A86C-02163E013892.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/097/00000/36101FC5-2441-E611-A5E8-02163E0140F0.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/097/00000/44E81E66-2A41-E611-AECD-02163E011B86.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/097/00000/6618DA28-1941-E611-BFC8-02163E0119CE.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/097/00000/8EA6E080-2241-E611-8959-02163E014659.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/097/00000/969E8E01-2641-E611-B796-02163E013928.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/097/00000/9ED977C5-1C41-E611-8161-02163E0144AD.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/097/00000/C2846E08-5041-E611-B81B-02163E01478D.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/181/00000/4431A74A-3341-E611-8D74-02163E0129A4.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/183/00000/1ED5F28F-3841-E611-9197-02163E0142F6.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/185/00000/A8A9DD1C-3A41-E611-8604-02163E01350F.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/186/00000/62DC6879-3D41-E611-982F-02163E014727.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/190/00000/D64E05D8-4C41-E611-80B7-02163E014657.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/235/00000/360B5E9F-E241-E611-939C-02163E0135C3.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/237/00000/DE665C9B-E941-E611-AA3C-02163E014668.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/242/00000/00414299-DB42-E611-B084-02163E014476.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/242/00000/00946B84-DD42-E611-92D0-02163E0134E0.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/242/00000/12D8A5A0-DB42-E611-82F3-02163E013557.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/242/00000/16BDD091-DB42-E611-A647-02163E014445.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/242/00000/1C5EC02F-DE42-E611-9A2B-02163E01266A.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/242/00000/32BBAD2E-DE42-E611-9907-02163E014355.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/242/00000/46412F31-DE42-E611-A542-02163E0140F3.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/242/00000/5849324E-DB42-E611-8A2F-02163E011F02.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/242/00000/7ADF5C98-DB42-E611-ABD5-02163E011F5B.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/242/00000/82421A27-DE42-E611-87D8-02163E0119AD.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/242/00000/88E21592-DB42-E611-9C01-02163E0127B7.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/242/00000/962F5B8D-DB42-E611-9CF5-02163E014244.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/242/00000/96576876-DB42-E611-BE83-02163E013836.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/242/00000/A83B8637-DE42-E611-B2EA-02163E012ABC.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/242/00000/C0B46862-DB42-E611-A16B-02163E012499.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/242/00000/CC8E93D5-3744-E611-A4F8-02163E013862.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/242/00000/CEBB7B8F-DB42-E611-AE1A-02163E011A8F.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/242/00000/DE8CE4A4-DB42-E611-8DBF-02163E014142.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/242/00000/EC76B374-DB42-E611-BC41-02163E014518.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/242/00000/F0C0E911-EC42-E611-BEE8-02163E013864.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/243/00000/5CEC962B-B043-E611-8ED6-02163E011D97.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/243/00000/64AC7D45-B043-E611-B843-02163E013421.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/243/00000/78B6541E-B043-E611-8B4B-02163E0144D5.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/243/00000/7E349428-B043-E611-BA1A-02163E0134B8.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/243/00000/FA5DE527-B043-E611-9740-02163E01455E.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/244/00000/0E879B4A-9F43-E611-AB1F-02163E0145CD.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/244/00000/14BC9547-9F43-E611-B4C0-02163E01372F.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/244/00000/5432814B-9F43-E611-89EF-02163E0133AD.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/244/00000/62257F4C-9F43-E611-9698-02163E0142C1.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/244/00000/6A418B49-9F43-E611-B14D-02163E01459E.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/244/00000/6E1AAE44-9F43-E611-A133-02163E011A8F.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/244/00000/F0EF5153-9F43-E611-9800-02163E014399.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/271/00000/C6F5E0A7-3944-E611-9F96-02163E0143D6.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/276/00000/2E05B0B1-3944-E611-B4F7-02163E01374E.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/279/00000/CA07ABB3-3944-E611-91FE-02163E01232B.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/282/00000/0A0E1AB8-7A44-E611-9D19-02163E0143A0.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/282/00000/0CFACDCF-7A44-E611-9480-02163E014272.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/282/00000/202463B6-7A44-E611-B667-02163E014275.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/282/00000/36E250BD-7A44-E611-A876-02163E0142B8.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/282/00000/403136BB-7A44-E611-9D8A-02163E01465B.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/282/00000/4878E1B1-7A44-E611-B08B-02163E0146FE.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/282/00000/561F65B5-7A44-E611-91DF-02163E0139C4.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/282/00000/90BC4FC1-7A44-E611-80D2-02163E012419.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/282/00000/92478CC5-7A44-E611-B2DC-02163E0143A4.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/282/00000/9C87E9EB-7A44-E611-B62A-02163E013434.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/282/00000/AE3362BF-7A44-E611-95F4-02163E011FB7.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/282/00000/B0C771D8-7A44-E611-9EFA-02163E01449B.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/282/00000/BE65F5B7-7A44-E611-88F7-02163E011C7B.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/282/00000/C814ACC5-7A44-E611-90D6-02163E011E85.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/282/00000/F6008DBB-7A44-E611-B448-02163E0142AC.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/283/00000/08C89061-AC44-E611-8E13-02163E0146F8.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/283/00000/0C07FF55-AC44-E611-BB1D-02163E01348A.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/283/00000/1A0C0952-AC44-E611-8EEC-02163E0145AC.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/283/00000/228EF05D-AC44-E611-96D9-02163E011934.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/283/00000/305A6866-AC44-E611-B18B-02163E0138D0.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/283/00000/865EEA52-AC44-E611-BCD9-02163E014611.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/283/00000/B207AB53-AC44-E611-88F2-02163E013937.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/283/00000/D0B6644F-AC44-E611-99AF-02163E01392F.root',
       '/store/data/Run2016C/MET/MINIAOD/PromptReco-v2/000/276/283/00000/EC925552-AC44-E611-9D68-02163E01256A.root',
] )