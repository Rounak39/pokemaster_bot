TIERS = { 
    "0": [10, 11, 13, 14, 16, 17, 19, 20, 21, 22, 23, 24, 27, 28, 29, 30, 32, 33, 39, 41, 42, 43, 44, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 60, 66, 67, 69, 70, 72, 73, 74, 75, 79, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 95, 96, 97, 98, 99, 100, 101, 102, 104, 109, 111, 114, 116, 118, 119, 120, 121, 129, 161, 162, 163, 164, 165, 167, 168, 170, 177, 179, 180, 183, 187, 188, 189, 191, 194, 195, 203, 206, 209, 216, 218, 220, 234, 261, 263, 264, 265, 266, 268, 270, 273, 274, 276, 278, 280, 283, 285, 287, 290, 293, 296, 300, 302, 303, 304, 307, 309, 311, 312, 313, 314, 315, 316, 318, 319, 320, 322, 324, 325, 327, 331, 339, 341, 353, 355, 366, 396, 399, 401, 403, 406, 412, 415, 417, 418, 420, 422, 425, 427, 431, 433, 434, 436, 449, 453, 456, 459, 504, 505, 506, 507, 509, 510, 519, 522, 524, 527, 529, 531, 532, 533, 535, 540, 541, 543, 546, 547, 548, 549, 550, 551, 557, 559, 560, 562, 568, 572, 573, 574, 575, 577, 578, 580, 581, 582, 583, 585, 587, 588, 590, 591, 592, 595, 596, 597, 598, 599, 600, 602, 605, 607, 618, 619, 629, 630, 659, 660, 661, 662, 664, 665, 667, 669, 670, 672,  674, 676, 677, 678, 679, 682, 684, 686, 687, 688, 690, 692, 694, 703],
    "1": [12, 15, 18, 25, 35, 37, 40, 45, 58, 61, 63, 68, 76, 77, 89, 93, 103, 105, 106, 107, 108, 110, 112, 117, 166, 171, 178, 182, 184, 185, 186, 190, 192, 193, 198, 200, 202, 204, 207, 210, 211, 215, 217, 219, 221, 222, 223, 224, 227, 228, 231, 235, 236, 237, 238, 239, 240, 241, 262, 267, 269, 271, 275, 277, 279, 281, 284, 286, 288, 291, 294, 297, 298, 299, 301, 305, 308, 310, 317, 321, 323, 326, 328, 332, 335, 336, 337, 338, 340, 342, 343, 352, 354, 356, 357, 361, 363, 367, 368, 369, 370, 397, 400, 402, 404, 407, 408, 410, 413, 414, 416, 419, 421, 423, 426, 428, 432, 435, 437, 441, 446, 447, 450, 451, 454, 455, 457, 460, 508, 511, 512, 513, 514, 515, 516, 517, 520, 521, 523, 525, 528, 530, 534, 536, 538, 539, 542, 544, 552, 554, 556, 558, 561, 563, 564, 566, 569, 576, 579, 584, 586, 589, 593, 594, 601, 603, 606, 608, 609, 613, 616, 617, 620, 627, 628, 632, 636, 637, 663, 666, 668, 671, 673, 675, 680, 683, 685, 689, 691, 693, 695, 701, 702, 707, 708, 710],
    "2": [1, 4, 7, 26, 31, 34, 36, 38, 62, 64, 65, 71, 78, 94, 113, 122, 123, 124, 125, 126, 127, 128, 133, 134, 135, 136, 137, 138, 139, 140, 141, 152, 155, 158, 169, 172, 173, 174, 175, 181, 199, 201, 205, 208, 214, 225, 226, 229, 232, 233, 246, 247, 252, 253, 255, 256, 258, 259, 272, 282, 289, 292, 295, 306, 329, 333, 344, 345, 346, 347, 348, 349, 351, 358, 359, 360, 362, 364, 365, 371, 372, 374, 375, 387, 388, 390, 391, 393, 394, 398, 405, 409, 411, 424, 429, 430, 438, 439, 440, 443, 444, 448, 452, 458, 461, 470, 471, 476, 478, 495, 496, 498, 499, 501, 502, 518, 526, 537, 545, 553, 555, 565, 567, 570, 604, 610, 611, 614, 615, 622, 623, 624, 625, 626, 631, 633, 634, 650, 651, 653, 654, 656, 657, 681, 696, 698, 700, 704, 705, 709, 711, 712, 714],
    "3": [2, 3, 5, 6, 8, 9, 59, 83, 115, 130, 131, 132, 142, 143, 147, 148, 149, 153, 154, 156, 157, 159, 160, 176, 196, 197, 212, 230, 242, 248, 254, 257, 260, 330, 334, 350, 373, 376, 389, 392, 395, 442, 445, 462, 463, 464, 465, 466, 467, 468, 469, 472, 473, 474, 475, 477, 479, 497, 500, 503, 571, 612, 621, 635, 652, 655, 658, 697, 699, 706, 713, 715, 720],
    "4": [144, 145, 146, 150, 151, 213, 243, 244, 245, 249, 250, 251, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386,480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 716, 717, 718, 719, 721]
}