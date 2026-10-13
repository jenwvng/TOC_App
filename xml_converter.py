import xml.etree.ElementTree as ET
import csv


header = ET.Element("TTOCMeasureTemplate",
                        attrib={'_dfv_': '1', 'TemplateUniqueIdent': '29A30E36-D944-4E98-845C-6E75A6F8EF31',
                                'TemplateTitle': 'test_sequence', 'TemplateOperator': '',
                                'TemplateCreateTimestamp': '2026-10-06 17:56:32',
                                'TemplateChangedTimestamp': '2026-10-06 17:56:32', 'TemplateComments': '',
                                'SamplerResetPositionSequence': 'true', 'SamplerResetPositionManual': 'true',
                                'MeasureAggregationState': '0', 'DescriptionColumns': '', 'DilutionAutomatic': 'false',
                                'DilutionIntelligent': 'false', 'VolumeReductionIntelligent': 'false',
                                'ParallelBlowOut': 'false'})
dilution = ET.SubElement(header, 'RTOCDilutionImplicitData',
                        attrib={'DilutionImplicit': 'false', 'DilutionImplicitVolumeThreshhold': '1',
                                'DilutionImplicitMaxMixedVolume': '1'})
TTOCMeasureSteps = ET.Element('TTOCMeasureSteps', attrib={'Name': "", 'Comment': ""})

def IC_step(sample_name, sample_position, repetitions,dilution_factor):
    TTOCMeasureStepIC = ET.SubElement(TTOCMeasureSteps, 'TTOCMeasureStepIC', attrib={'IsActive': 'true',
                                                                                     'Name': sample_name,
                                                                                     'Comment': '',
                                                                                     'IsFinished': 'false',
                                                                                     'StepDescriptions': '',
                                                                                     'AggregationState': '0',
                                                                                     'SamplePosition': str(
                                                                                         sample_position),
                                                                                     'SampleManual': 'false',
                                                                                     'WithEluat': 'false',
                                                                                     'TOCMP_IC': 'true',
                                                                                     'TOCMP_TC': 'false',
                                                                                     'TOCMP_NPOC': 'false',
                                                                                     'TOCMP_TN': 'false',
                                                                                     'TOCMP_S': 'false',
                                                                                     'TOCMP_Cl': 'false',
                                                                                     'TOCMP_POC': 'false',
                                                                                     'MinRepetitions': str(repetitions),
                                                                                     'MaxRepetitions': str(repetitions),
                                                                                     'SampleVolume': '500',
                                                                                     'RinseVolume': '2000',
                                                                                     'StirStrength': '0',
                                                                                     'FurnaceTemperature': '750',
                                                                                     'Block': '10',
                                                                                     'DilutionNumerator': '1',
                                                                                     'DilutionDenominator': '1',
                                                                                     'UseReagentNa2S2O8': 'false',
                                                                                     'UseReagentH3PO4': 'true',
                                                                                     'PickingPosition': '0',
                                                                                     'ReverseRinseCount': '0',
                                                                                     'UseBoat': 'false',
                                                                                     'MethodIdent': '02CA53C4-D759-4F63-816C-11BB3592092C',
                                                                                     'MethodName': 'IC',
                                                                                     'VariationCoefficient': '2',
                                                                                     'StandardDeviation': 'NAN',
                                                                                     'MaxIntegrationTime': '300',
                                                                                     'Start': '0.12',
                                                                                     'BaseApproach': '0.2',
                                                                                     'FurnacePos1': '70',
                                                                                     'FurnaceTime': '30',
                                                                                     'FurnaceFeed': '100',
                                                                                     'CO2Active': 'false'})
    StepType = ET.SubElement(TTOCMeasureStepIC, "StepType")
    RTOCDilutionImplicitData = ET.SubElement(TTOCMeasureStepIC, "RTOCDilutionImplicitData",
                                             attrib={'DilutionImplicit': 'false',
                                                     'DilutionImplicitVolumeThreshhold': '1',
                                                     'DilutionImplicitMaxMixedVolume': '1'})
    TTOCMeasureStepTypeSample = ET.SubElement(StepType, "TTOCMeasureStepTypeSample",
                                              attrib={'StepTypeName': "Sample", 'BoundaryLower': "NAN",
                                                      'BoundaryUpper': "NAN", 'Action': "0"})
    Channels = ET.SubElement(TTOCMeasureStepIC, "Channels")
    Channel = ET.SubElement(Channels, "Channel",
                            attrib={'ChannelName': 'IC', 'IsVirtual': 'false', 'IsControl': 'false', 'ChannelType': '1',
                                    'CalibrationIdent': ''})
    StepType1 = ET.SubElement(Channel, "StepType")
    TTOCMeasureStepTypeSample1 = ET.SubElement(StepType1, "TTOCMeasureStepTypeSample",
                                               attrib={'StepTypeName': 'Sample', 'BoundaryLower': 'NAN',
                                                       'BoundaryUpper': 'NAN', 'Action': '0'})
    TTOCCalibrationData = ET.SubElement(Channel, "TTOCCalibrationData",
                                        attrib={'PreparationWater': 'NAN', 'ReagentPhosphoricAcid': 'NAN',
                                                'ReagentSodiumPersulflat': 'NAN', 'Dilution': 'NAN', 'Eluat': 'NAN',
                                                'Boat': 'NAN'})
    TTOCCalibrationDataRange = ET.SubElement(TTOCCalibrationData, 'TTOCCalibrationDataRange',
                                             attrib={'DayFactor': 'NAN', 'IntervallUpper': '1.79769313486232E308',
                                                     'IntervallLower': '-1.79769313486232E308'})
    cc1 = ET.SubElement(TTOCCalibrationDataRange, "cc", attrib={"c": "0"})
    cc2 = ET.SubElement(TTOCCalibrationDataRange, "cc", attrib={"c": "1540"})
    TTOCMeasureStepCycleParameters = ET.SubElement(TTOCMeasureStepIC, 'TTOCMeasureStepCycleParameters')
    TTOCStepCycleParameterLiquid = ET.SubElement(TTOCMeasureStepCycleParameters, "TTOCStepCycleParameterLiquid",
                                                 attrib={'RinseCycleCount': '3'})
    return TTOCStepCycleParameterLiquid
def TOC_step(TOC_sample_name, TOC_sample_position, TOC_repetitions, TOC_dilution_factor):
    TTOCMeasureStepNPOCTN = ET.SubElement(TTOCMeasureSteps, 'TTOCMeasureStepNPOCTN',
                                          attrib={'IsActive': 'true', 'Name': TOC_sample_name, 'Comment': '',
                                                  'IsFinished': 'false', 'StepDescriptions': '',
                                                  'AggregationState': '0',
                                                  'SamplePosition': str(TOC_sample_position), 'SampleManual': 'false',
                                                  'WithEluat': 'false',
                                                  'TOCMP_IC': 'false', 'TOCMP_TC': 'false', 'TOCMP_NPOC': 'true',
                                                  'TOCMP_TN': 'true', 'TOCMP_S': 'false', 'TOCMP_Cl': 'false',
                                                  'TOCMP_POC': 'false', 'MinRepetitions': str(TOC_repetitions),
                                                  'MaxRepetitions': str(TOC_repetitions),
                                                  'SampleVolume': '500', 'RinseVolume': '2000', 'StirStrength': '5',
                                                  'FurnaceTemperature': '750', 'Block': '3', 'DilutionNumerator': '1',
                                                  'DilutionDenominator': str(TOC_dilution_factor),
                                                  'UseReagentNa2S2O8': 'false',
                                                  'UseReagentH3PO4': 'false', 'PickingPosition': '0',
                                                  'ReverseRinseCount': '0', 'UseBoat': 'false',
                                                  'MethodIdent': '4CC7E50B-3F1F-4341-A597-5DF36BFD480D',
                                                  'MethodName': 'NPOC_TN', 'VariationCoefficient': '2',
                                                  'StandardDeviation': 'NAN', 'MaxIntegrationTime': '300',
                                                  'Start': '0.12',
                                                  'BaseApproach': '0.2', 'WithTICControl': 'false',
                                                  'AutomaticAcidify': 'true', 'BlowoutTime1': '300',
                                                  'BlowoutTime2': '10',
                                                  'CODActive': 'false', 'CODParameterA': '3', 'CODParameterB': '0',
                                                  'BOD5Active': 'false', 'BOD5ParameterC': '3', 'BOD5ParameterD': '0',
                                                  'VariationCoefficientTN': '2', 'StandardDeviationTN': 'NAN',
                                                  'StartTN': '0.12', 'BaseApproachTN': '0.5',
                                                  'TotalProteinActive': 'false',
                                                  'TotalProteinA': '6.25'})
    StepType2 = ET.SubElement(TTOCMeasureStepNPOCTN, 'StepType')
    TTOCMeasureStepTypeSample2 = ET.SubElement(StepType2, 'TTOCMeasureStepTypeSample',
                                               attrib={'StepTypeName': 'Sample', 'BoundaryLower': 'NAN',
                                                       'BoundaryUpper': 'NAN', 'Action': '0'})
    RTOCDilutionImplicitData = ET.SubElement(TTOCMeasureStepNPOCTN, 'RTOCDilutionImplicitData',
                                             attrib={'DilutionImplicit': 'false',
                                                     'DilutionImplicitVolumeThreshhold': '1',
                                                     'DilutionImplicitMaxMixedVolume': '1'})
    Channels2 = ET.SubElement(TTOCMeasureStepNPOCTN, 'Channels')
    Channel3 = ET.SubElement(Channels2, 'Channel',
                             attrib={'ChannelName': 'NPOC', 'IsVirtual': 'false', 'IsControl': 'false',
                                     'ChannelType': '3', 'CalibrationIdent': ''})
    StepType3 = ET.SubElement(Channel3, 'StepType')
    TTOCMeasureStepTypeSample3 = ET.SubElement(StepType3, 'TTOCMeasureStepTypeSample',
                                               attrib={'StepTypeName': 'Sample', 'BoundaryLower': 'NAN',
                                                       'BoundaryUpper': 'NAN', 'Action': '0'})
    TTOCCalibrationData3 = ET.SubElement(Channel3, 'TTOCCalibrationData',
                                         attrib={'PreparationWater': 'NAN', 'ReagentPhosphoricAcid': 'NAN',
                                                 'ReagentSodiumPersulflat': 'NAN', 'Dilution': 'NAN', 'Eluat': 'NAN',
                                                 'Boat': 'NAN'})
    TTOCCalibrationDataRange3 = ET.SubElement(TTOCCalibrationData3, 'TTOCCalibrationDataRange',
                                              attrib={'DayFactor': 'NAN', 'IntervallUpper': '1.79769313486232E308',
                                                      'IntervallLower': '-1.79769313486232E308'})
    cc3 = ET.SubElement(TTOCCalibrationDataRange3, "cc", attrib={'c': '0'})
    cc4 = ET.SubElement(TTOCCalibrationDataRange3, "cc", attrib={'c': '1540'})
    Channel4 = ET.SubElement(Channels2, 'Channel',
                             attrib={'ChannelName': 'TN', 'IsVirtual': 'false', 'IsControl': 'false',
                                     'ChannelType': '2', 'CalibrationIdent': ''})
    StepType4 = ET.SubElement(Channel4, 'StepType')
    TTOCMeasureStepTypeSample4 = ET.SubElement(StepType4, 'TTOCMeasureStepTypeSample',
                                               attrib={'StepTypeName': 'Sample', 'BoundaryLower': 'NAN',
                                                       'BoundaryUpper': 'NAN', 'Action': '0'})
    TTOCCalibrationData4 = ET.SubElement(Channel4, 'TTOCCalibrationData',
                                         attrib={'PreparationWater': 'NAN', 'ReagentPhosphoricAcid': 'NAN',
                                                 'ReagentSodiumPersulflat': 'NAN', 'Dilution': 'NAN', 'Eluat': 'NAN',
                                                 'Boat': 'NAN'})
    TTOCCalibrationDataRange4 = ET.SubElement(TTOCCalibrationData4, 'TTOCCalibrationDataRange',
                                              attrib={'DayFactor': 'NAN', 'IntervallUpper': '1.79769313486232E308',
                                                      'IntervallLower': '-1.79769313486232E308'})
    cc5 = ET.SubElement(TTOCCalibrationDataRange4, "cc", attrib={'c': '0'})
    cc6 = ET.SubElement(TTOCCalibrationDataRange4, "cc", attrib={'c': '833'})
    TTOCMeasureStepCycleParameters2 = ET.SubElement(TTOCMeasureStepNPOCTN, 'TTOCMeasureStepCycleParameters')
    TTOCStepCycleParameterNPOC = ET.SubElement(TTOCMeasureStepCycleParameters2, "TTOCStepCycleParameterNPOC",
                                               attrib={'RinseCycleCount': '3', 'WithBlowOut': 'true'})
    return TTOCStepCycleParameterNPOC
######## STAND BY STEP###############
TTOCMeasureStepControlDeviceStandby = ET.SubElement(TTOCMeasureSteps, "TTOCMeasureStepControlDeviceStandby", attrib={'IsActive': 'true', 'Name': 'Standby', 'Comment': '', 'IsFinished': 'false', 'StepDescriptions': '', 'FurnaceTemperature': '20'})
StepType5 = ET.SubElement(TTOCMeasureStepControlDeviceStandby, 'StepType')
Nil = ET.SubElement(StepType5, 'Nil', attrib={'IsNil':"true"})
###########################################################



with open(input(), newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        print(row)
        if row[0] == "TIC":
            print("inorganic")
            IC_step(row[1],row[2],row[3],row[4])
        elif row[0] == "NPOCTN":
            TOC_step(row[1], row[2], row[3], row[4])
            print("organic")



header.append(TTOCMeasureSteps)
header = ET.ElementTree(header)
header.write("output.xml", xml_declaration=True)

