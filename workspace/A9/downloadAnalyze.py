import soundDownload as SD
import soundAnalysis as SA


#descriptorMapping = { 0: 'lowlevel.spectral_centroid.mean',
#                      1: 'lowlevel.dissonance.mean',
#                      2: 'lowlevel.hfc.mean',
#                      3: 'sfx.logattacktime.mean',
#                      4: 'sfx.inharmonicity.mean',
#                      5: 'lowlevel.spectral_contrast.mean.0',
#                      6: 'lowlevel.spectral_contrast.mean.1',
#                      7: 'lowlevel.spectral_contrast.mean.2',
#                      8: 'lowlevel.spectral_contrast.mean.3',
#                      9: 'lowlevel.spectral_contrast.mean.4',
#                      10: 'lowlevel.spectral_contrast.mean.5',
#                      11: 'lowlevel.mfcc.mean.0',
#                      12: 'lowlevel.mfcc.mean.1',
#                      13: 'lowlevel.mfcc.mean.2',
#                      14: 'lowlevel.mfcc.mean.3',
#                      15: 'lowlevel.mfcc.mean.4',
#                      16: 'lowlevel.mfcc.mean.5'
#                   }


key = "ty46jgGrQ1xZ1BLjJy4QLP6WR6MwQM6WmyOU00he"
inputDir = "trainDirectory/"
trainingDir = inputDir
testingDir = "testDirectory/"

#SD.downloadSoundsFreesound(queryText = "drum", tag="snare", duration=(1,8), API_Key = key , outputDir = testingDir, topNResults = 1)

#SA.descriptorPairScatterPlot(inputDir, descInput = (0,3), anotOn = 0)

#SA.clusterSounds(inputDir, nCluster = 3, descInput=[0,12,3])

SA.classifySoundkNN("testDirectory/drum/410514/410514_5121236-lq.json", inputDir, 3, descInput = [0,12,3,13,14])
SA.classifySoundkNN("testDirectory/clarinet/356592/356592_6552981-lq.json", inputDir, 3, descInput = [0,12,3,13,14])
SA.classifySoundkNN("testDirectory/viola/374346/374346_2475994-lq.json", inputDir, 3, descInput = [0,12,3,13,14])