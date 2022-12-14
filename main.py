import math

confidence_level_to_z_score = {0: 0,
                               1: .01,
                               2: .03,
                               3: .04,
                               4: .05,
                               5: .06,
                               6: .08,
                               7: .09,
                               8: .1,
                               9: .11,
                               10: .13,
                               11: .14,
                               12: .15,
                               13: .16,
                               14: .18,
                               15: .19,
                               16: .2,
                               17: .21,
                               18: .23,
                               19: .24,
                               20: .26,
                               21: .27,
                               22: .28,
                               23: .29,
                               24: .3,
                               25: .32,
                               26: .33,
                               27: .35,
                               28: .36,
                               29: .36,
                               30: .37,
                               31: .40,
                               32: .41,
                               33: .43,
                               34: .44,
                               35: .45,
                               36: .47,
                               37: .48,
                               38: .50,
                               39: .51,
                               40: .53,
                               41: .54,
                               42: .56,
                               43: .57,
                               44: .58,
                               45: .60,
                               46: .61,
                               47: .63,
                               48: .65,
                               49: .66,
                               50: .68,
                               51: .69,
                               52: .71,
                               53: .72,
                               54: .74,
                               55: .76,
                               56: .77,
                               57: .79,
                               58: .81,
                               59: .83,
                               60: .85,
                               61: .86,
                               62: .88,
                               63: .90,
                               64: .92,
                               65: .94,
                               66: .96,
                               67: .98,
                               68: 1,
                               69: 1.02,
                               70: 1.04,
                               71: 1.06,
                               72: 1.08,
                               73: 1.11,
                               74: 1.13,
                               75: 1.15,
                               76: 1.18,
                               77: 1.2,
                               78: 1.23,
                               79: 1.25,
                               80: 1.28,
                               81: 1.31,
                               82: 1.34,
                               83: 1.37,
                               84: 1.41,
                               85: 1.44,
                               86: 1.48,
                               87: 1.51,
                               88: 1.55,
                               89: 1.6,
                               90: 1.65,
                               91: 1.7,
                               92: 1.75,
                               93: 1.81,
                               94: 1.88,
                               95: 1.96,
                               96: 2.06,
                               97: 2.17,
                               98: 2.33,
                               99: 2.58,
                               99.5: 2.81,
                               99.9: 3.29,
                               }

population_size = int(input('Population Size: '))
confidence_level = int(input('Confidence Level: '))
margin_of_error = int(input('Margin of Error: '))


def sample_size_calculator():

    return (confidence_level_to_z_score[confidence_level] ** 2) * (0.5 * (1 - 0.5)) / ((margin_of_error / 100) ** 2) / \
           (1 + (confidence_level_to_z_score[confidence_level] ** 2) * (0.5 * (1 - 0.5)) / (((margin_of_error / 100) **
            2) * population_size))


print(math.ceil(sample_size_calculator()))
