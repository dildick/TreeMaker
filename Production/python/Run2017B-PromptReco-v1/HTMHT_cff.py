import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/039/00000/F44D72B2-1356-E711-B5EF-02163E01A47B.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/046/00000/C21FA84B-6D56-E711-9779-02163E0139CF.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/047/00000/067C60F9-1B56-E711-AD8C-02163E019E3D.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/050/00000/94E63B9D-6756-E711-8B6F-02163E014538.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/056/00000/3A915274-7456-E711-A439-02163E014140.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/057/00000/3E7D35B2-9056-E711-8DBB-02163E01A1BE.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/057/00000/92FD99AB-3557-E711-B16F-02163E012019.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/068/00000/32212754-8856-E711-A6E9-02163E013735.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/099/00000/54BEBA71-B356-E711-942D-02163E014109.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/100/00000/AC2AB498-F656-E711-B59A-02163E011D03.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/101/00000/8EC525E4-5757-E711-99B5-02163E0124B6.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/101/00000/CA5ABC42-2857-E711-9ACC-02163E01339B.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/107/00000/10EAFE8C-0257-E711-8800-02163E01A505.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/112/00000/84E8BE9B-0257-E711-BC7E-02163E01A288.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/113/00000/F4776D41-4557-E711-B0CF-02163E019DD9.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/114/00000/96366C28-4F57-E711-AC68-02163E019C90.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/116/00000/42427476-1957-E711-9043-02163E01A7A7.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/150/00000/E6343738-2657-E711-93B7-02163E01A65B.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/168/00000/0AAFF89A-3B57-E711-AC3D-02163E0139BB.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/169/00000/46FE13F2-4757-E711-ABBD-02163E0140DF.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/170/00000/6C7E26EC-4E57-E711-9100-02163E019BA0.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/171/00000/88B73811-5457-E711-A29D-02163E01A64C.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/175/00000/2AA5A938-7757-E711-A3CE-02163E01180A.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/176/00000/1602D6E5-6857-E711-90F8-02163E01A208.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/177/00000/CAEFE0EA-6657-E711-B090-02163E0144E2.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/178/00000/7AD0F573-8857-E711-9EF0-02163E0133FE.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/178/00000/CAF062E9-7657-E711-BABD-02163E011F20.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/179/00000/98C08D84-E458-E711-900D-02163E011DD2.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/180/00000/C4A10699-1259-E711-B3B6-02163E014167.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/181/00000/9A3E5DC9-E158-E711-82B7-02163E019D98.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/182/00000/AA1FDEF5-D958-E711-9B1F-02163E011CD8.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/199/00000/7ED9FBD2-D858-E711-958D-02163E0143E9.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/211/00000/4887F5C6-8857-E711-A8AA-02163E014111.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/215/00000/6805B591-9257-E711-89F4-02163E011DD1.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/218/00000/607CEDEB-7757-E711-8680-02163E011AEC.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/219/00000/508A2024-B358-E711-B734-02163E01450F.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/219/00000/7CE5A31A-8F58-E711-945E-02163E011C88.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/219/00000/9A8786FB-7E58-E711-885A-02163E01A3EB.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/219/00000/ACE23EFA-EB58-E711-8356-02163E012076.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/224/00000/36AB8E3B-BD58-E711-B3CA-02163E01A686.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/225/00000/808EB9FB-A958-E711-A7DA-02163E011AD8.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/227/00000/F8D49FAB-E158-E711-A9E8-02163E01A21E.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/228/00000/CE7D48AC-A558-E711-84F8-02163E01A778.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/229/00000/F4F9B4F3-A458-E711-9705-02163E0144E0.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/268/00000/EE03CFF8-A458-E711-B69B-02163E01A3D9.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/281/00000/1A3CD021-DF58-E711-89FF-02163E01A4FB.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/286/00000/7E269288-C258-E711-98E7-02163E01A5F5.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/292/00000/327ABDED-0659-E711-B177-02163E01A211.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/292/00000/6C0478AC-2D59-E711-B1B2-02163E013778.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/293/00000/B09C445B-2659-E711-A11A-02163E013967.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/296/00000/86647A0A-2B59-E711-A262-02163E0133D6.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/308/00000/AE1E3390-1459-E711-91D3-02163E019CCF.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/316/00000/AAAE2A3E-0159-E711-9240-02163E014364.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/341/00000/EC4B5DFE-1559-E711-BD6D-02163E019BB6.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/359/00000/DEBAC567-8359-E711-A05C-02163E01A5DC.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/406/00000/CC4D43A0-A659-E711-879D-02163E019CAF.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/411/00000/2CC9AFA2-1F5A-E711-9071-02163E019DA2.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/411/00000/AE9B4C5B-0C5A-E711-A1C0-02163E01357B.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/424/00000/A672F2DD-415A-E711-8773-02163E011DD1.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/425/00000/A2E9F02E-4D5A-E711-A2F2-02163E019DF5.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/426/00000/683C6EAB-4E5A-E711-B3B8-02163E011A71.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/429/00000/7E3B1BB4-4C5A-E711-A728-02163E0120DD.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/430/00000/961F849B-555A-E711-8629-02163E019C34.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/431/00000/643C535A-785A-E711-8F05-02163E01A616.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/432/00000/AC61DEF6-605A-E711-B62D-02163E0134F9.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/433/00000/BC429C85-695A-E711-9046-02163E0133D6.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/434/00000/D8E84548-775A-E711-BE22-02163E01A50C.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/435/00000/8E678E96-745A-E711-BFF2-02163E01A3EF.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/462/00000/BEA21785-7D5A-E711-A0B4-02163E0143CF.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/467/00000/D2AB177F-D95A-E711-ADE0-02163E012A94.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/468/00000/6047C8B9-EC5A-E711-AE67-02163E013692.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/469/00000/B428D072-DD5A-E711-92BF-02163E01A1C9.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/474/00000/541D0B0F-F45A-E711-BD3F-02163E019D03.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/480/00000/0A994730-EC5A-E711-8B8F-02163E0144BA.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/483/00000/E40C96AE-355B-E711-8758-02163E01361F.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/484/00000/BA07F8C0-405B-E711-A73A-02163E0146FD.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/485/00000/7E0BB1A1-4D5B-E711-B453-02163E014767.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/486/00000/088EE8CF-715B-E711-9A1D-02163E01A58F.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/486/00000/1E5006DC-7E5B-E711-8E79-02163E019D8E.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/487/00000/1834F9B4-985B-E711-8284-02163E014716.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/488/00000/983758BC-A45B-E711-A9E8-02163E01A6F2.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/503/00000/3AE2571C-075C-E711-8EB2-02163E0143BC.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/503/00000/B23D1086-345C-E711-9373-02163E019DD8.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/504/00000/A875A508-0D5C-E711-9582-02163E01A50C.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/505/00000/A0EA9309-335C-E711-BCB4-02163E01A3DB.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/537/00000/D238535D-135C-E711-B72F-02163E013778.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/552/00000/2CF4C97E-385C-E711-9FEA-02163E0128B7.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/557/00000/2A5D1285-AF5C-E711-9DF7-02163E012526.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/557/00000/FC09D46B-C95C-E711-B15C-02163E011C1F.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/558/00000/7023A61F-A75C-E711-B79F-02163E0146E8.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/559/00000/6A8BA1A3-845C-E711-AB5A-02163E014105.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/560/00000/7E744B7B-9C5C-E711-B043-02163E011C17.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/562/00000/50C704A9-C25C-E711-AA60-02163E019E31.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/563/00000/1055572F-CE5C-E711-8D06-02163E011BEA.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/598/00000/6808A576-E25C-E711-AD95-02163E01398A.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/599/00000/82DD7EB4-4E5D-E711-8FD6-02163E01A795.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/599/00000/C6F49849-215D-E711-B3F9-02163E012481.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/603/00000/D641B9D3-505D-E711-AA24-02163E01A39B.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/604/00000/106B5F6E-1261-E711-A65C-02163E0133E6.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/604/00000/20EED3DA-F65D-E711-984F-02163E019BA5.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/605/00000/D0366948-5B5D-E711-B3EE-02163E019E8E.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/606/00000/F8E5F2E1-605D-E711-AEFB-02163E01A3B8.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/618/00000/6A3B86CA-7C5D-E711-92DF-02163E01A3BC.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/620/00000/EACBDC85-B45D-E711-BAFB-02163E019BAA.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/656/00000/4CDCC874-075E-E711-AA26-02163E014109.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/656/00000/92960204-FD5D-E711-87AD-02163E019CB1.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/659/00000/F0041475-E05D-E711-9F7C-02163E019D98.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/660/00000/7C1C0388-FE5D-E711-B57C-02163E011F2C.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/664/00000/EC84EF62-FF5D-E711-BC14-02163E011F2C.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/665/00000/AA08612A-255E-E711-826E-02163E0134D1.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/666/00000/040B3723-405E-E711-B2BC-02163E019C43.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/670/00000/4A24543B-335E-E711-94EE-02163E0146E8.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/671/00000/0EB9785E-475E-E711-9D69-02163E019D47.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/672/00000/C4BEB7BD-2E5E-E711-85E1-02163E01A6F7.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/674/00000/F8715991-6D5E-E711-9978-02163E01A5A5.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/675/00000/96CA1C68-785E-E711-8594-02163E012396.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/675/00000/E2B0C32E-7E5E-E711-B90F-02163E019E36.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/678/00000/7E03449F-585E-E711-A5CD-02163E01A6B8.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/722/00000/BE26870A-F15E-E711-8788-02163E0142C5.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/722/00000/FCCF5377-F35E-E711-A485-02163E01A692.root',
'/store/data/Run2017B/HTMHT/MINIAOD/PromptReco-v1/000/297/723/00000/0C903800-F75E-E711-82B7-02163E01392C.root' ] );
