import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import stats

x = np.asarray(
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105,1106]
)

y = np.asarray(
[0, 73, 80, 77, 75, 80, 301, 293, 289, 313, 306, 291, 315, 311, 314, 309, 312, 313, 313, 289, 296, 308, 307, 312, 298, 303, 300, 307, 296, 314, 310, 285, 316, 302, 304, 312, 308, 315, 299, 301, 314, 303, 293, 301, 305, 304, 314, 301, 313, 309, 304, 309, 306, 306, 303, 307, 298, 304, 303, 301, 314, 306, 295, 309, 303, 312, 311, 313, 313, 305, 308, 297, 308, 309, 314, 313, 314, 304, 306, 305, 312, 312, 309, 310, 312, 308, 310, 298, 304, 290, 308, 310, 312, 310, 307, 315, 316, 314, 311, 310, 293, 313, 293, 308, 297, 316, 313, 311, 301, 311, 295, 304, 307, 308, 291, 285, 314, 303, 308, 309, 308, 314, 314, 292, 305, 306, 309, 311, 313, 308, 292, 309, 304, 295, 293, 306, 314, 311, 312, 301, 303, 312, 290, 311, 306, 306, 303, 302, 305, 311, 313, 309, 307, 284, 313, 302, 309, 298, 288, 314, 313, 307, 300, 305, 307, 313, 316, 313, 309, 295, 316, 309, 300, 304, 312, 314, 315, 305, 292, 308, 308, 305, 308, 314, 312, 305, 313, 309, 313, 306, 308, 303, 303, 303, 303, 306, 306, 306, 311, 296, 303, 310, 314, 309, 302, 311, 313, 306, 311, 307, 307, 306, 295, 306, 302, 310, 311, 314, 314, 311, 308, 291, 309, 304, 316, 313, 311, 312, 310, 314, 622, 627, 625, 313, 980, 637, 636, 636, 1317, 1543, 636, 625, 627, 617, 1200, 854, 1198, 632, 316, 629, 678, 631, 621, 628, 636, 624, 630, 627, 627, 631, 300, 300, 637, 624, 313, 631, 636, 678, 673, 627, 315, 632, 630, 638, 979, 978, 977, 980, 672, 622, 626, 630, 977, 980, 631, 620, 637, 311, 980, 292, 625, 978, 626, 678, 622, 311, 629, 629, 621, 980, 979, 634, 635, 630, 623, 636, 631, 672, 636, 627, 637, 630, 635, 621, 629, 678, 625, 1296, 633, 633, 626, 978, 978, 678, 626, 629, 627, 629, 629, 625, 632, 979, 623, 627, 620, 633, 627, 980, 676, 682, 313, 979, 632, 630, 624, 636, 627, 316, 630, 631, 623, 300, 678, 633, 978, 632, 630, 629, 679, 632, 629, 678, 629, 636, 630, 630, 633, 631, 630, 630, 676, 633, 636, 633, 620, 680, 637, 632, 631, 636, 634, 303, 631, 680, 639, 314, 634, 633, 632, 638, 298, 629, 626, 633, 631, 626, 316, 624, 979, 627, 632, 625, 632, 314, 621, 636, 672, 675, 672, 672, 862, 675, 679, 672, 672, 672, 674, 679, 673, 677, 676, 674, 674, 673, 673, 674, 678, 674, 678, 678, 675, 672, 672, 1364, 672, 1365, 672, 675, 673, 673, 674, 673, 672, 1364, 1364, 677, 673, 673, 678, 674, 1365, 674, 672, 672, 672, 674, 675, 674, 672, 679, 677, 679, 673, 672, 677, 673, 678, 679, 676, 672, 679, 680, 675, 1364, 674, 675, 672, 675, 674, 679, 675, 674, 674, 679, 675, 674, 678, 675, 678, 1365, 675, 680, 672, 1365, 675, 675, 679, 674, 673, 672, 678, 673, 680, 1364, 672, 675, 1365, 673, 672, 672, 673, 672, 1364, 674, 679, 678, 675, 675, 672, 678, 672, 679, 680, 674, 678, 678, 673, 680, 676, 678, 673, 672, 674, 677, 672, 673, 676, 674, 672, 673, 679, 675, 678, 673, 1364, 679, 1364, 676, 673, 674, 679, 677, 672, 674, 674, 672, 673, 672, 1365, 674, 674, 675, 673, 674, 679, 675, 1364, 673, 1365, 679, 678, 673, 674, 672, 675, 672, 672, 1364, 676, 672, 673, 672, 678, 672, 675, 678, 1365, 1364, 676, 674, 674, 678, 674, 672, 1365, 674, 678, 678, 1364, 673, 674, 673, 674, 673, 674, 1365, 674, 674, 672, 678, 674, 678, 678, 677, 673, 672, 672, 672, 674, 674, 678, 675, 675, 672, 673, 1300, 673, 672, 672, 679, 678, 678, 673, 676, 674, 672, 674, 678, 672, 676, 674, 676, 675, 672, 673, 676, 673, 672, 680, 672, 677, 676, 676, 672, 673, 672, 673, 673, 678, 1365, 680, 672, 678, 673, 678, 675, 674, 676, 673, 674, 674, 674, 672, 674, 674, 674, 672, 672, 675, 677, 672, 672, 674, 679, 673, 672, 675, 675, 674, 673, 674, 675, 1364, 674, 672, 672, 672, 679, 678, 674, 678, 675, 679, 1365, 673, 672, 673, 679, 672, 674, 672, 673, 680, 680, 676, 673, 675, 672, 1364, 679, 673, 675, 674, 672, 1364, 674, 677, 674, 672, 674, 672, 673, 673, 672, 676, 672, 674, 678, 673, 673, 1365, 677, 673, 679, 1364, 679, 674, 672, 1365, 672, 672, 673, 672, 1365, 678, 673, 672, 672, 1365, 674, 673, 674, 672, 676, 675, 673, 676, 673, 679, 672, 672, 676, 672, 673, 672, 674, 672, 675, 680, 674, 1365, 672, 1364, 1365, 1364, 674, 672, 677, 679, 675, 679, 679, 676, 673, 675, 674, 1365, 1364, 673, 1364, 675, 673, 672, 675, 1365, 673, 679, 672, 678, 675, 675, 677, 672, 674, 1364, 678, 673, 676, 672, 679, 673, 676, 674, 673, 679, 674, 672, 674, 672, 676, 673, 674, 1364, 672, 675, 672, 672, 673, 1365, 677, 677, 672, 679, 673, 674, 672, 672, 672, 672, 677, 673, 672, 1364, 672, 1365, 674, 674, 673, 680, 676, 674, 1364, 1365, 678, 673, 673, 673, 679, 675, 1364, 675, 680, 673, 678, 672, 672, 673, 678, 675, 678, 673, 672, 672, 674, 675, 674, 672, 673, 675, 672, 674, 674, 673, 675, 673, 675, 673, 673, 673, 673, 673, 672, 678, 1364, 1365, 673, 674, 675, 672, 675, 675, 672, 677, 672, 678, 674, 672, 673, 678, 673, 673, 676, 1365, 673, 1364, 673, 672, 677, 679, 1365, 673, 675, 674, 676, 679, 1365, 1364, 672, 676, 677, 674, 676, 672, 674, 673, 678, 678, 1365, 673, 673, 677, 672, 674, 679, 674, 673, 673, 673, 679, 673, 674, 674, 674, 674, 678, 673, 673, 672, 673, 679, 672, 672, 672, 675, 676, 673, 672, 680, 674, 675, 680, 677, 674, 673, 674, 673, 1364, 672, 675, 672, 1364, 675, 674, 678, 674, 680, 675, 678, 1365, 672, 672, 672, 673, 672, 678, 675, 675, 680, 674, 673, 678, 678, 672, 672, 679, 674, 674, 672, 1365, 1364, 679, 679, 673, 674, 1365, 672, 676, 674, 677, 1365, 678, 1365, 680, 679, 678, 672, 676, 672, 674, 1365, 675, 672, 678, 673, 673, 678, 674, 679, 674, 674, 674, 677, 672, 672, 679, 673, 674, 677, 672, 1365, 673, 1365, 676, 675, 674, 678, 672, 679, 673, 674, 1365, 672, 677, 1365, 680, 676, 673, 678, 672, 672, 1365, 679, 678, 680, 672, 672, 673, 680, 672, 672, 678, 672, 676, 674, 679, 678, 1364, 673, 672, 679, 672, 679, 674, 673, 674, 674,5000]
)
# fit with np.polyfit
print(scipy.stats.pearsonr(x, y))
m, b = np.polyfit(x, y, 1)

plt.plot(x, y, '.')
plt.plot(x, m*x + b, '-')
plt.xlabel('Generation')
plt.ylabel('Best Fitness Score')
plt.show()
