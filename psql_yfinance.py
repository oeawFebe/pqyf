# Finished. Will never use this (hopefully)!
import yfinance as yf
import psycopg2
from tqdm import tqdm
import time
# get info from yfinance to pqyf database (psql)

print("---PSQL START---")
conn=psycopg2.connect("dbname=pqyf host=localhost user=postgres password=postgres")
cur=conn.cursor()

tickers=\
[1301, 1305, 1306, 1308, 1309, 1311, 1312, 1313, 1319, 1320, 1321, 1322, 1323, 1324, 1325, 1326, 1327, 1328, 1329, 1330, 1332, 1333, 1343, 1344, 1345, 1346, 1348, 1349, 1352, 1356, 1357, 1358, 1360, 1364, 1365, 1366, 1367, 1368, 1369, 1375, 1376, 1377, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1397, 1398, 1399, 1400, 1401, 1407, 1413, 1414, 1417, 1418, 1419, 1420, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 1436, 1439, 1440, 1443, 1445, 1446, 1447, 1448, 1450, 1451, 1452, 1456, 1457, 1458, 1459, 1460, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1496, 1497, 1498, 1499, 1514, 1515, 1518, 1540, 1541, 1542, 1543, 1545, 1546, 1547, 1550, 1551, 1552, 1554, 1555, 1557, 1559, 1560, 1563, 1566, 1567, 1568, 1569, 1570, 1571, 1572, 1573, 1574, 1575, 1576, 1577, 1578, 1579, 1580, 1584, 1585, 1586, 1591, 1592, 1593, 1595, 1596, 1597, 1598, 1599, 1605, 1615, 1617, 1618, 1619, 1620, 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632, 1633, 1651, 1652, 1653, 1654, 1655, 1656, 1657, 1658, 1659, 1660, 1662, 1663, 1670, 1671, 1672, 1673, 1674, 1675, 1676, 1677, 1678, 1679, 1680, 1681, 1682, 1684, 1685, 1686, 1687, 1688, 1689, 1690, 1691, 1692, 1693, 1694, 1695, 1696, 1697, 1698, 1699, 1711, 1712, 1716, 1717, 1718, 1719, 1720, 1721, 1723, 1724, 1726, 1728, 1730, 1736, 1737, 1739, 1743, 1757, 1758, 1762, 1764, 1766, 1768, 1770, 1773, 1775, 1776, 1780, 1782, 1783, 1787, 1788, 1789, 1793, 1795, 1798, 1799, 1801, 1802, 1803, 1805, 1807, 1808, 1810, 1811, 1812, 1813, 1814, 1815, 1820, 1821, 1822, 1824, 1826, 1827, 1828, 1833, 1835, 1840, 1841, 1844, 1847, 1848, 1850, 1852, 1853, 1860, 1861, 1866, 1867, 1870, 1871, 1873, 1878, 1879, 1881, 1882, 1883, 1884, 1885, 1887, 1888, 1890, 1893, 1897, 1898, 1899, 1904, 1905, 1909, 1911, 1914, 1921, 1925, 1926, 1928, 1929, 1930, 1934, 1938, 1939, 1941, 1942, 1944, 1945, 1946, 1948, 1949, 1950, 1951, 1952, 1954, 1959, 1960, 1961, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1971, 1972, 1973, 1975, 1976, 1979, 1980, 1981, 1982, 1992, 1994, 1997, 2001, 2002, 2003, 2004, 2009, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2050, 2053, 2055, 2060, 2065, 2066, 2067, 2068, 2069, 2070, 2071, 2072, 2107, 2108, 2109, 2112, 2114, 2117, 2120, 2121, 2122, 2124, 2127, 2130, 2134, 2136, 2138, 2139, 2146, 2148, 2150, 2151, 2152, 2153, 2154, 2156, 2157, 2158, 2159, 2160, 2162, 2163, 2164, 2168, 2169, 2170, 2173, 2174, 2175, 2176, 2178, 2179, 2180, 2181, 2183, 2185, 2186, 2191, 2193, 2195, 2196, 2198, 2201, 2204, 2206, 2207, 2208, 2209, 2211, 2212, 2215, 2216, 2217, 2220, 2221, 2222, 2224, 2226, 2229, 2230, 2264, 2266, 2267, 2268, 2269, 2270, 2281, 2282, 2286, 2288, 2291, 2292, 2293, 2294, 2296, 2300, 2301, 2303, 2304, 2305, 2307, 2309, 2311, 2315, 2317, 2321, 2323, 2325, 2326, 2327, 2329, 2330, 2331, 2332, 2334, 2335, 2336, 2337, 2338, 2340, 2341, 2342, 2344, 2345, 23459, 2349, 2351, 2352, 2353, 2354, 2359, 2362, 2370, 2371, 2372, 2373, 2374, 2375, 2376, 2378, 2379, 2384, 2385, 2388, 2389, 2391, 2393, 2395, 2397, 2398, 2402, 2404, 2406, 2408, 2410, 2411, 2412, 2413, 2415, 2418, 2424, 2425, 2427, 2428, 2429, 2432, 2433, 2435, 2436, 2437, 2438, 2440, 2445, 2449, 2452, 2453, 2454, 2459, 2461, 2462, 2464, 2468, 2469, 2471, 2475, 2477, 2479, 2480, 2481, 2483, 2484, 2485, 2487, 2488, 2489, 2491, 2492, 2493, 2497, 2498, 2499, 2501, 2502, 2503, 2510, 2511, 2512, 2513, 2514, 2515, 2516, 2517, 2518, 2519, 2520, 2521, 2522, 2523, 2524, 2525, 2526, 2527, 2528, 2529, 2530, 2531, 2533, 2540, 2552, 2553, 2554, 2555, 2556, 2557, 2558, 2559, 2560, 2561, 2562, 2563, 2564, 2565, 2566, 2567, 2568, 2569, 2573, 2579, 2586, 2587, 2588, 2590, 2593, 25935, 2594, 2597, 2599, 2602, 2607, 2612, 2613, 2620, 2621, 2622, 2623, 2624, 2625, 2651, 2652, 2653, 2654, 2656, 2659, 2664, 2666, 2667, 2668, 2669, 2670, 2673, 2674, 2675, 2676, 2678, 2681, 2683, 2685, 2686, 2687, 2689, 2692, 2693, 2694, 2695, 2698, 2700, 2702, 2705, 2706, 2708, 2714, 2715, 2721, 2722, 2726, 2729, 2730, 2733, 2734, 2735, 2736, 2737, 2742, 2743, 2747, 2749, 2750, 2751, 2752, 2753, 2754, 2760, 2761, 2762, 2763, 2764, 2767, 2768, 2769, 2773, 2776, 2777, 2778, 2780, 2782, 2784, 2788, 2789, 2790, 2791, 2792, 2795, 2796, 2798, 2801, 2802, 2804, 2805, 2806, 2809, 2810, 2811, 2812, 2813, 2814, 2815, 2816, 2818, 2819, 2820, 2830, 2831, 2871, 2872, 2874, 2875, 2876, 2877, 2882, 2883, 2884, 2892, 2894, 2897, 2899, 2901, 2903, 2904, 2905, 2907, 2908, 2910, 2911, 2914, 2915, 2916, 2917, 2918, 2922, 2923, 2924, 2925, 2926, 2927, 2929, 2930, 2931, 2932, 2970, 2971, 2972, 2975, 2977, 2978, 2979, 2980, 2981, 2982, 2985, 2986, 2987, 3001, 3002, 3003, 3004, 3010, 3011, 3020, 3021, 3023, 3024, 3028, 3030, 3031, 3034, 3035, 3036, 3038, 3039, 3040, 3041, 3042, 3045, 3046, 3048, 3050, 3053, 3054, 3058, 3059, 3063, 3064, 3065, 3067, 3068, 3069, 3070, 3071, 3073, 3075, 3076, 3077, 3079, 3080, 3082, 3083, 3085, 3086, 3087, 3088, 3089, 3091, 3092, 3093, 3094, 3096, 3097, 3098, 3099, 3101, 3103, 3104, 3105, 3106, 3107, 3109, 3110, 3111, 3113, 3116, 3121, 3123, 3125, 3131, 3132, 3133, 3134, 3135, 3137, 3138, 3139, 3140, 3141, 3143, 3148, 3150, 3151, 3153, 3154, 3156, 3157, 3159, 3160, 3161, 3166, 3167, 3168, 3169, 3172, 3173, 3174, 3175, 3176, 3177, 3178, 3179, 3180, 3181, 3182, 3183, 3184, 3185, 3186, 3187, 3189, 3190, 3191, 3192, 3193, 3194, 3195, 3196, 3197, 3198, 3199, 3201, 3202, 3204, 3205, 3221, 3222, 3223, 3224, 3226, 3227, 3228, 3231, 3232, 3234, 3236, 3237, 3238, 3241, 3242, 3244, 3245, 3246, 3248, 3249, 3252, 3254, 3261, 3264, 3266, 3267, 3269, 3271, 3275, 3276, 3277, 3278, 3279, 3280, 3281, 3282, 3283, 3284, 3286, 3287, 3288, 3289, 3290, 3291, 3292, 3293, 3294, 3295, 3296, 3297, 3298, 3299, 3300, 3302, 3306, 3309, 3315, 3316, 3317, 3319, 3320, 3321, 3322, 3323, 3326, 3328, 3329, 3333, 3341, 3344, 3347, 3349, 3350, 3352, 3353, 3355, 3356, 3358, 3359, 3360, 3361, 3370, 3371, 3372, 3374, 3375, 3376, 3377, 3382, 3386, 3387, 3388, 3390, 3391, 3392, 3393, 3395, 3396, 3397, 3399, 3401, 3402, 3405, 3407, 3408, 3409, 3415, 3416, 3417, 3418, 3420, 3421, 3423, 3426, 3431, 3433, 3434, 3435, 3436, 3437, 3439, 3440, 3441, 3443, 3444, 3445, 3446, 3447, 3448, 3449, 3451, 3452, 3453, 3454, 3455, 3456, 3457, 3458, 3459, 3461, 3462, 3463, 3464, 3465, 3466, 3467, 3468, 3469, 3470, 3471, 3472, 3474, 3475, 3476, 3477, 3478, 3479, 3480, 3481, 3482, 3483, 3484, 3486, 3487, 3488, 3489, 3490, 3491, 3492, 3493, 3494, 3495, 3496, 3497, 3498, 3501, 3512, 3513, 3515, 3521, 3524, 3526, 3528, 3529, 3536, 3537, 3538, 3539, 3540, 3541, 3542, 3543, 3544, 3546, 3547, 3548, 3549, 3550, 3551, 3553, 3556, 3557, 3558, 3559, 3560, 3561, 3562, 3563, 3565, 3566, 3569, 3571, 3577, 3578, 3580, 3583, 3591, 3593, 3597, 3598, 3600, 3604, 3607, 3608, 3611, 3612, 3622, 3623, 3624, 3625, 3626, 3627, 3628, 3630, 3632, 3633, 3634, 3635, 3636, 3639, 3640, 3641, 3645, 3646, 3647, 3648, 3649, 3652, 3653, 3655, 3656, 3657, 3658, 3659, 3660, 3661, 3662, 3663, 3664, 3665, 3666, 3667, 3668, 3670, 3671, 3672, 3673, 3674, 3675, 3676, 3677, 3678, 3679, 3680, 3681, 3682, 3683, 3686, 3687, 3688, 3689, 3690, 3691, 3692, 3693, 3694, 3695, 3696, 3697, 3698, 3708, 3710, 3712, 3719, 3723, 3726, 3727, 3733, 3738, 3741, 3744, 3747, 3750, 3751, 3753, 3758, 3760, 3762, 3763, 3765, 3766, 3768, 3769, 3770, 3771, 3772, 3773, 3774, 3776, 3777, 3778, 3779, 3782, 3784, 3787, 3788, 3791, 3793, 3796, 3798, 3799, 3800, 3802, 3803, 3804, 3807, 3810, 3814, 3815, 3816, 3817, 3823, 3825, 3826, 3834, 3835, 3836, 3837, 3839, 3840, 3841, 3842, 3843, 3844, 3845, 3847, 3848, 3850, 3851, 3852, 3853, 3854, 3856, 3857, 3858, 3861, 3863, 3864, 3865, 3877, 3878, 3880, 3891, 3892, 3895, 3896, 3900, 3901, 3902, 3903, 3904, 3905, 3906, 3907, 3908, 3909, 3910, 3911, 3912, 3913, 3914, 3915, 3916, 3917, 3918, 3919, 3920, 3921, 3922, 3923, 3924, 3925, 3926, 3927, 3928, 3929, 3930, 3931, 3932, 3933, 3934, 3935, 3936, 3937, 3938, 3939, 3940, 3941, 3944, 3945, 3946, 3947, 3948, 3950, 3951, 3953, 3954, 3955, 3956, 3960, 3961, 3962, 3963, 3964, 3965, 3966, 3967, 3968, 3969, 3970, 3974, 3975, 3976, 3978, 3979, 3981, 3983, 3984, 3985, 3986, 3987, 3988, 3989, 3990, 3991, 3992, 3993, 3994, 3995, 3996, 3997, 3998, 3999, 4004, 4005, 4008, 4011, 4012, 4013, 4014, 4015, 4016, 4017, 4021, 4022, 4023, 4025, 4026, 4027, 4028, 4031, 4041, 4042, 4043, 4044, 4045, 4046, 4047, 4051, 4052, 4053, 4054, 4055, 4056, 4057, 4058, 4059, 4060, 4061, 4062, 4063, 4064, 4078, 4080, 4082, 4088, 4091, 4092, 4093, 4094, 4095, 4097, 4098, 4099, 4100, 4102, 4107, 4109, 4112, 4113, 4114, 4115, 4116, 4118, 4119, 4120, 4124, 4151, 4182, 4183, 4185, 4186, 4187, 4188, 4189, 4202, 4203, 4204, 4205, 4206, 4208, 4212, 4215, 4216, 4218, 4220, 4221, 4222, 4224, 4228, 4229, 4231, 4234, 4235, 4237, 4238, 4240, 4241, 4242, 4243, 4245, 4246, 4248, 4249, 4250, 4251, 4272, 4274, 4275, 4282, 4284, 4286, 4287, 4288, 4290, 4293, 4295, 4298, 4299, 4301, 4304, 4307, 4308, 4310, 4312, 4316, 4317, 4318, 4319, 4320, 4321, 4323, 4324, 4326, 4327, 4331, 4333, 4334, 4335, 4336, 4337, 4341, 4342, 4343, 4344, 4345, 4346, 4347, 4348, 4350, 4351, 4355, 4356, 4361, 4362, 4364, 4365, 4366, 4367, 4368, 4369, 4380, 4381, 4382, 4383, 4384, 4385, 4386, 4387, 4388, 4389, 4390, 4391, 4392, 4393, 4394, 4395, 4396, 4397, 4398, 4399, 4401, 4403, 4404, 4406, 4409, 4410, 4420, 4421, 4422, 4423, 4424, 4425, 4426, 4427, 4428, 4429, 4430, 4431, 4433, 4434, 4435, 4436, 4437, 4438, 4439, 4440, 4441, 4442, 4443, 4444, 4445, 4446, 4448, 4449, 4450, 4452, 4461, 4462, 4463, 4464, 4465, 4471, 4475, 4476, 4477, 4478, 4479, 4480, 4481, 4482, 4483, 4484, 4485, 4486, 4487, 4488, 4490, 4491, 4492, 4493, 4494, 4495, 4496, 4497, 4499, 4502, 4503, 4506, 4507, 4512, 4514, 4516, 4517, 4519, 4521, 4523, 4524, 4526, 4527, 4528, 4530, 4531, 4534, 4536, 4538, 4539, 4540, 4541, 4543, 4544, 4547, 4548, 4549, 4550, 4551, 4552, 4553, 4554, 4555, 4556, 4557, 4558, 4559, 4563, 4564, 4565, 4568, 4569, 4570, 4571, 4572, 4574, 4575, 4576, 4577, 4578, 4579, 4581, 4582, 4583, 4584, 4586, 4587, 4588, 4591, 4592, 4593, 4594, 4595, 4596, 4597, 4598, 4599, 4611, 4612, 4613, 4615, 4616, 4617, 4619, 4620, 4621, 4623, 4624, 4625, 4626, 4627, 4628, 4629, 4631, 4633, 4634, 4635, 4636, 4640, 4641, 4642, 4644, 4645, 4650, 4651, 4653, 4657, 4658, 4659, 4661, 4662, 4664, 4665, 4666, 4667, 4668, 4669, 4671, 4673, 4674, 4676, 4678, 4679, 4680, 4681, 4684, 4685, 4686, 4687, 4689, 4690, 4691, 4694, 4696, 4699, 4704, 4705, 4707, 4708, 4709, 4712, 4714, 4716, 4718, 4719, 4720, 4722, 4725, 4726, 4728, 4732, 4733, 4734, 4735, 4736, 4739, 4743, 4745, 4746, 4748, 4750, 4751, 4752, 4754, 4755, 4760, 4761, 4762, 4763, 4764, 4765, 4766, 4767, 4768, 4769, 4770, 4771, 4772, 4776, 4777, 4779, 4781, 4783, 4784, 4792, 4800, 4801, 4809, 4812, 4813, 4814, 4816, 4819, 4820, 4824, 4825, 4826, 4828, 4829, 4832, 4833, 4837, 4838, 4839, 4840, 4845, 4847, 4848, 4849, 4875, 4880, 4883, 4901, 4902, 4911, 4912, 4914, 4917, 4918, 4919, 4920, 4921, 4922, 4923, 4925, 4926, 4927, 4928, 4929, 4930, 4931, 4933, 4934, 4951, 4952, 4955, 4956, 4957, 4958, 4960, 4962, 4963, 4966, 4967, 4968, 4970, 4971, 4972, 4973, 4974, 4975, 4976, 4977, 4978, 4979, 4980, 4985, 4987, 4990, 4992, 4994, 4996, 4997, 4998, 4999, 5008, 5009, 5010, 5011, 5013, 5015, 5017, 5018, 5019, 5020, 5021, 5070, 5071, 5072, 5101, 5103, 5104, 5105, 5108, 5110, 5121, 5122, 5142, 5161, 5162, 5184, 5185, 5186, 5187, 5189, 5191, 5192, 5194, 5195, 5199, 5201, 5202, 5204, 5208, 5210, 5212, 5214, 5216, 5217, 5218, 5232, 5233, 5237, 5261, 5262, 5268, 5269, 5271, 5273, 5277, 5279, 5280, 5282, 5283, 5284, 5285, 5287, 5288, 5290, 5301, 5302, 5304, 5310, 5331, 5332, 5333, 5334, 5337, 5341, 5344, 5351, 5352, 5355, 5357, 5358, 5363, 5367, 5368, 5380, 5381, 5384, 5386, 5387, 5388, 5391, 5393, 5395, 5401, 5406, 5408, 5410, 5411, 5423, 5440, 5444, 5445, 5446, 5449, 5451, 5458, 5463, 5464, 5471, 5476, 5480, 5481, 5482, 5484, 5486, 5491, 5541, 5542, 5563, 5602, 5603, 5609, 5610, 5612, 5614, 5631, 5632, 5644, 5658, 5659, 5660, 5690, 5695, 5697, 5698, 5699, 5702, 5703, 5704, 5706, 5707, 5711, 5713, 5714, 5715, 5721, 5724, 5726, 5727, 5729, 5741, 5742, 5753, 5757, 5781, 5801, 5802, 5803, 5805, 5807, 5809, 5816, 5817, 5819, 5820, 5821, 5851, 5852, 5856, 5857, 5858, 5900, 5901, 5902, 5903, 5905, 5906, 5907, 5909, 5911, 5912, 5915, 5918, 5921, 5922, 5923, 5928, 5929, 5930, 5932, 5933, 5935, 5936, 5938, 5939, 5940, 5941, 5942, 5943, 5945, 5946, 5947, 5949, 5950, 5951, 5952, 5955, 5956, 5957, 5958, 5959, 5962, 5964, 5965, 5966, 5967, 5969, 5970, 5971, 5973, 5974, 5975, 5976, 5981, 5982, 5983, 5984, 5985, 5986, 5987, 5988, 5989, 5990, 5991, 5992, 5994, 5997, 5998, 5999, 6005, 6013, 6016, 6018, 6022, 6023, 6026, 6027, 6028, 6029, 6030, 6031, 6032, 6033, 6034, 6035, 6036, 6037, 6038, 6039, 6040, 6042, 6044, 6045, 6046, 6047, 6048, 6049, 6050, 6054, 6055, 6058, 6059, 6060, 6061, 6062, 6063, 6064, 6066, 6067, 6069, 6070, 6071, 6072, 6073, 6074, 6077, 6078, 6080, 6081, 6082, 6083, 6085, 6086, 6087, 6088, 6089, 6090, 6091, 6092, 6093, 6094, 6095, 6096, 6098, 6099, 6101, 6103, 6104, 6113, 6118, 6121, 6125, 6131, 6134, 6135, 6136, 6137, 6138, 6140, 6141, 6143, 6144, 6145, 6146, 6147, 6149, 6150, 6151, 6155, 6156, 6157, 6158, 6159, 6161, 6164, 6165, 6166, 6167, 6171, 6172, 6173, 6174, 6175, 6176, 6177, 6178, 6180, 6181, 6182, 6183, 6184, 6185, 6186, 6187, 6188, 6189, 6190, 6191, 6192, 6193, 6194, 6195, 6196, 6197, 6198, 6199, 6200, 6201, 6203, 6205, 6208, 6210, 6217, 6218, 6222, 6231, 6232, 6233, 6235, 6236, 6237, 6238, 6239, 6240, 6245, 6246, 6247, 6248, 6249, 6250, 6254, 6255, 6257, 6258, 6262, 6264, 6265, 6266, 6267, 6268, 6269, 6271, 6272, 6273, 6276, 6277, 6278, 6279, 6281, 6282, 6284, 6286, 6287, 6289, 6291, 6292, 6293, 6294, 6297, 6298, 6299, 6301, 6302, 6303, 6305, 6306, 6307, 6309, 6310, 6312, 6315, 6316, 6317, 6319, 6322, 6323, 6324, 6325, 6326, 6327, 6328, 6330, 6331, 6332, 6333, 6334, 6335, 6336, 6337, 6338, 6339, 6340, 6342, 6343, 6345, 6346, 6347, 6349, 6351, 6355, 6356, 6357, 6358, 6360, 6361, 6362, 6363, 6364, 6365, 6366, 6367, 6368, 6369, 6370, 6371, 6373, 6376, 6378, 6379, 6380, 6381, 6382, 6383, 6384, 6387, 6390, 6391, 6392, 6393, 6395, 6396, 6400, 6402, 6403, 6405, 6406, 6407, 6408, 6409, 6411, 6412, 6413, 6414, 6416, 6417, 6418, 6419, 6420, 6424, 6425, 6428, 6430, 6432, 6433, 6436, 6440, 6444, 6445, 6448, 6454, 6455, 6457, 6458, 6459, 6460, 6461, 6462, 6463, 6464, 6465, 6466, 6467, 6469, 6470, 6471, 6472, 6473, 6474, 6479, 6480, 6481, 6482, 6484, 6485, 6486, 6488, 6489, 6490, 6492, 6493, 6494, 6495, 6496, 6497, 6498, 6501, 6502, 6503, 6504, 6505, 6506, 6507, 6508, 6513, 6516, 6517, 6518, 6531, 6532, 6533, 6535, 6537, 6538, 6539, 6540, 6541, 6542, 6543, 6544, 6545, 6546, 6547, 6548, 6549, 6550, 6551, 6552, 6553, 6554, 6555, 6556, 6557, 6558, 6560, 6561, 6562, 6563, 6564, 6565, 6566, 6567, 6568, 6569, 6570, 6571, 6572, 6573, 6574, 6575, 6576, 6577, 6578, 6579, 6580, 6584, 6586, 6588, 6590, 6592, 6594, 6596, 6597, 6599, 6615, 6616, 6617, 6618, 6619, 6620, 6622, 6625, 6626, 6627, 6628, 6629, 6630, 6632, 6633, 6634, 6635, 6637, 6638, 6639, 6640, 6641, 6643, 6644, 6645, 6647, 6648, 6651, 6652, 6653, 6654, 6656, 6658, 6659, 6662, 6663, 6664, 6666, 6668, 6670, 6674, 6675, 6676, 6677, 6678, 6694, 6695, 6696, 6697, 6698, 6699, 6701, 6702, 6703, 6704, 6706, 6707, 6709, 6715, 6718, 6721, 6722, 6723, 6724, 6727, 6728, 6730, 6731, 6734, 6736, 6737, 6740, 6741, 6742, 6743, 6744, 6745, 6748, 6750, 6752, 6753, 6754, 6755, 6757, 6758, 6762, 6763, 6768, 6769, 6770, 6771, 6772, 6775, 6776, 6777, 6778, 6779, 6785, 6786, 6787, 6788, 6789, 6794, 6798, 6800, 6803, 6804, 6806, 6807, 6809, 6810, 6814, 6815, 6817, 6819, 6820, 6822, 6823, 6824, 6826, 6832, 6834, 6835, 6836, 6837, 6838, 6839, 6840, 6841, 6844, 6845, 6848, 6849, 6850, 6852, 6853, 6855, 6856, 6857, 6858, 6859, 6861, 6862, 6863, 6864, 6866, 6867, 6869, 6870, 6871, 6874, 6875, 6877, 6879, 6881, 6882, 6888, 6890, 6894, 6897, 6898, 6899, 6901, 6902, 6904, 6905, 6907, 6908, 6912, 6914, 6915, 6916, 6918, 6919, 6920, 6923, 6924, 6925, 6926, 6927, 6928, 6929, 6930, 6932, 6937, 6938, 6941, 6942, 6943, 6944, 6945, 6946, 6947, 6951, 6952, 6954, 6955, 6957, 6958, 6960, 6961, 6962, 6963, 6964, 6965, 6966, 6967, 6969, 6971, 6973, 6976, 6977, 6981, 6982, 6986, 6988, 6989, 6993, 6994, 6995, 6996, 6997, 6998, 6999, 7003, 7004, 7011, 7012, 7013, 7014, 7018, 7021, 7022, 7030, 7033, 7034, 7035, 7036, 7037, 7038, 7039, 7040, 7041, 7042, 7043, 7044, 7045, 7046, 7047, 7048, 7049, 7050, 7056, 7057, 7058, 7059, 7060, 7061, 7062, 7063, 7064, 7065, 7066, 7067, 7068, 7069, 7070, 7071, 7072, 7073, 7074, 7075, 7077, 7078, 7079, 7080, 7081, 7082, 7083, 7084, 7085, 7086, 7087, 7088, 7089, 7090, 7091, 7093, 7094, 7095, 7097, 7098, 7102, 7105, 7122, 7148, 7150, 7157, 7161, 7162, 7164, 7167, 7169, 7170, 7172, 7173, 7175, 7176, 7177, 7180, 7181, 7182, 7183, 7184, 7185, 7186, 7187, 7189, 7190, 7191, 7192, 7196, 7198, 7199, 7201, 7202, 7203, 7205, 7208, 7211, 7212, 7213, 7214, 7215, 7217, 7218, 7219, 7220, 7222, 7224, 7226, 7228, 7229, 7231, 7235, 7236, 7238, 7239, 7240, 7241, 7242, 7244, 7245, 7246, 7247, 7250, 7254, 7255, 7256, 7259, 7261, 7264, 7265, 7266, 7267, 7268, 7269, 7270, 7271, 7272, 7273, 7276, 7277, 7278, 7279, 7280, 7282, 7283, 7284, 7287, 7291, 7292, 7294, 7296, 7297, 7298, 7299, 7305, 7309, 7313, 7314, 7315, 7317, 7320, 7321, 7322, 7325, 7326, 7327, 7337, 7338, 7339, 7351, 7352, 7353, 7354, 7355, 7356, 7357, 7399, 7408, 7412, 7413, 7414, 7416, 7417, 7419, 7420, 7421, 7422, 7425, 7426, 7427, 7433, 7434, 7435, 7438, 7442, 7443, 7444, 7445, 7446, 7447, 7448, 7450, 7451, 7453, 7455, 7456, 7458, 7459, 7460, 7461, 7462, 7463, 7464, 7466, 7467, 7472, 7475, 7476, 7477, 7480, 7481, 7482, 7483, 7486, 7487, 7490, 7494, 7500, 7501, 7502, 7504, 7505, 7506, 7508, 7509, 7510, 7512, 7513, 7514, 7515, 7516, 7518, 7519, 7520, 7521, 7522, 7523, 7524, 7525, 7527, 7531, 7532, 7537, 7538, 7539, 7544, 7545, 7550, 7551, 7552, 7554, 7555, 7559, 7561, 7562, 7564, 7565, 7567, 7570, 7571, 7575, 7577, 7578, 7581, 7585, 7587, 7590, 7593, 7594, 7595, 7596, 7597, 7599, 7600, 7601, 7602, 7603, 7604, 7605, 7606, 7607, 7608, 7609, 7610, 7611, 7613, 7614, 7615, 7616, 7618, 7619, 7621, 7623, 7624, 7625, 7628, 7630, 7634, 7635, 7636, 7637, 7638, 7640, 7643, 7646, 7647, 7649, 7670, 7671, 7672, 7673, 7674, 7676, 7677, 7678, 7679, 7680, 7681, 7682, 7683, 7685, 7686, 7687, 7688, 7689, 7690, 7691, 7692, 7693, 7701, 7702, 7705, 7707, 7709, 7711, 7713, 7715, 7716, 7717, 7718, 7719, 7721, 7722, 7723, 7725, 7726, 7727, 7729, 7730, 7731, 7732, 7733, 7734, 7735, 7739, 7740, 7741, 7743, 7744, 7745, 7746, 7747, 7748, 7749, 7751, 7752, 7758, 7760, 7762, 7768, 7769, 7771, 7774, 7775, 7776, 7777, 7779, 7780, 7781, 7782, 7790, 7800, 7803, 7804, 7805, 7806, 7807, 7808, 7809, 7810, 7811, 7812, 7813, 7814, 7815, 7816, 7817, 7818, 7819, 7820, 7821, 7822, 7823, 7826, 7827, 7829, 7831, 7832, 7833, 7836, 7837, 7838, 7839, 7840, 7841, 7844, 7846, 7847, 7849, 7850, 7851, 7855, 7856, 7857, 7859, 7860, 7862, 7863, 7864, 7865, 7867, 7868, 7869, 7871, 7872, 7874, 7875, 7877, 7878, 7879, 7883, 7885, 7886, 7887, 7888, 7893, 7895, 7896, 7897, 7898, 7899, 7901, 7902, 7905, 7906, 7908, 7911, 7912, 7914, 7915, 7916, 7917, 7918, 7919, 7921, 7922, 7923, 7925, 7927, 7928, 7931, 7932, 7936, 7937, 7938, 7939, 7940, 7942, 7943, 7945, 7946, 7947, 7949, 7951, 7952, 7953, 7955, 7956, 7957, 7958, 7959, 7961, 7962, 7963, 7965, 7966, 7970, 7971, 7972, 7974, 7975, 7976, 7979, 7980, 7981, 7983, 7984, 7985, 7986, 7987, 7988, 7989, 7990, 7991, 7992, 7994, 7995, 7997, 7999, 8001, 8002, 8005, 8006, 8007, 8008, 8011, 8012, 8013, 8014, 8015, 8016, 8018, 8020, 8022, 8023, 8025, 8029, 8030, 8031, 8032, 8035, 8037, 8038, 8039, 8040, 8041, 8043, 8045, 8046, 8050, 8051, 8052, 8053, 8056, 8057, 8058, 8059, 8060, 8061, 8065, 8066, 8068, 8070, 8072, 8074, 8075, 8077, 8078, 8079, 8081, 8084, 8085, 8086, 8087, 8088, 8089, 8090, 8091, 8093, 8095, 8096, 8097, 8098, 8101, 8103, 8104, 8105, 8107, 8108, 8111, 8113, 8114, 8115, 8117, 8118, 8119, 8123, 8125, 8127, 8129, 8130, 8131, 8132, 8133, 8135, 8136, 8137, 8138, 8139, 8140, 8141, 8142, 8143, 8144, 8147, 8150, 8151, 8152, 8153, 8154, 8155, 8157, 8158, 8159, 8160, 8163, 8165, 8166, 8167, 8168, 8173, 8174, 8179, 8181, 8182, 8184, 8185, 8186, 8194, 8198, 8200, 8202, 8203, 8207, 8208, 8209, 8214, 8215, 8217, 8218, 8219, 8225, 8226, 8227, 8230, 8233, 8237, 8242, 8244, 8247, 8249, 8252, 8253, 8254, 8255, 8256, 8257, 8260, 8267, 8273, 8275, 8276, 8278, 8279, 8281, 8282, 8283, 8285, 8287, 8289, 8291, 8298, 8301, 8303, 8304, 8306, 8308, 8309, 8316, 8331, 8334, 8336, 8337, 8338, 8341, 8342, 8343, 8344, 8345, 8346, 8349, 8350, 8354, 8355, 8356, 8358, 8359, 8360, 8361, 8362, 8363, 8364, 8365, 8366, 8367, 8368, 8369, 8370, 8377, 8381, 8382, 8383, 8385, 8386, 8387, 8388, 8392, 8393, 8395, 8397, 8399, 8410, 8411, 8416, 8418, 8421, 8424, 8425, 8439, 8462, 8473, 8508, 8511, 8515, 8518, 8521, 8522, 8524, 8527, 8530, 8537, 8541, 8542, 8544, 8550, 8551, 8558, 8562, 8563, 8566, 8570, 8572, 8584, 8585, 8586, 8591, 8593, 8595, 8596, 8600, 8601, 8604, 8609, 8613, 8614, 8616, 8617, 8622, 8624, 8628, 8630, 8697, 8698, 8699, 8700, 8704, 8705, 8706, 8707, 8708, 8713, 8714, 8715, 8725, 8732, 8737, 8739, 8740, 8742, 8746, 8747, 8750, 8766, 8769, 8771, 8772, 8783, 8789, 8793, 8795, 8798, 8801, 8802, 8803, 8804, 8806, 8818, 8830, 8835, 8836, 8841, 8842, 8844, 8848, 8850, 8854, 8860, 8864, 8869, 8871, 8876, 8877, 8881, 8886, 8887, 8889, 8890, 8891, 8892, 8893, 8894, 8897, 8898, 8903, 8904, 8905, 8908, 8909, 8912, 8914, 8917, 8918, 8919, 8920, 8922, 8923, 8925, 8927, 8928, 8929, 8931, 8934, 8935, 8938, 8940, 8944, 8945, 8946, 8951, 8952, 8953, 8954, 8955, 8956, 8957, 8958, 8960, 8961, 8963, 8964, 8966, 8967, 8968, 8972, 8975, 8976, 8977, 8979, 8984, 8985, 8986, 8987, 8995, 8999, 9001, 9003, 9005, 9006, 9007, 9008, 9009, 9010, 9012, 9014, 9017, 9020, 9021, 9022, 9024, 9025, 9028, 9029, 9031, 9033, 9034, 9036, 9037, 9039, 9041, 9042, 9044, 9045, 9046, 9048, 9049, 9051, 9052, 9055, 9057, 9058, 9059, 9060, 9062, 9063, 9064, 9065, 9066, 9067, 9068, 9069, 9070, 9072, 9073, 9074, 9075, 9076, 9078, 9081, 9082, 9083, 9086, 9087, 9090, 9099, 9101, 9104, 9107, 9110, 9115, 9119, 9127, 9130, 9142, 9143, 9171, 9173, 9176, 9179, 9193, 9201, 9202, 9206, 9232, 9233, 9260, 9261, 9262, 9263, 9264, 9265, 9266, 9267, 9268, 9270, 9271, 9272, 9273, 9274, 9275, 9276, 9278, 9279, 9281, 9282, 9283, 9284, 9285, 9286, 9287, 9301, 9302, 9303, 9304, 9305, 9306, 9307, 9308, 9310, 9311, 9312, 9313, 9318, 9319, 9322, 9324, 9325, 9326, 9351, 9353, 9355, 9358, 9360, 9361, 9362, 9363, 9364, 9365, 9366, 9367, 9368, 9369, 9375, 9376, 9377, 9380, 9381, 9384, 9385, 9386, 9388, 9399, 9401, 9404, 9405, 9408, 9409, 9412, 9413, 9414, 9416, 9417, 9418, 9419, 9421, 9422, 9423, 9424, 9425, 9428, 9432, 9433, 9434, 9435, 9436, 9437, 9438, 9439, 9441, 9444, 9445, 9446, 9449, 9450, 9465, 9466, 9467, 9468, 9470, 9474, 9475, 9476, 9478, 9479, 9501, 9502, 9503, 9504, 9505, 9506, 9507, 9508, 9509, 9511, 9513, 9514, 9517, 9519, 9531, 9532, 9533, 9534, 9535, 9536, 9537, 9539, 9543, 9551, 9600, 9601, 9602, 9603, 9605, 9610, 9612, 9613, 9616, 9619, 9621, 9622, 9624, 9625, 9627, 9628, 9629, 9631, 9632, 9633, 9635, 9636, 9637, 9639, 9640, 9641, 9644, 9647, 9651, 9656, 9658, 9661, 9663, 9671, 9672, 9675, 9678, 9679, 9681, 9682, 9684, 9685, 9686, 9687, 9691, 9692, 9695, 9696, 9697, 9698, 9699, 9701, 9702, 9704, 9706, 9707, 9708, 9709, 9713, 9715, 9716, 9717, 9719, 9720, 9722, 9723, 9726, 9728, 9729, 9731, 9733, 9734, 9735, 9739, 9740, 9742, 9743, 9744, 9746, 9749, 9753, 9755, 9757, 9758, 9759, 9760, 9761, 9763, 9765, 9766, 9767, 9768, 9769, 9776, 9778, 9780, 9782, 9783, 9787, 9788, 9790, 9791, 9793, 9795, 9797, 9799, 9810, 9812, 9816, 9818, 9820, 9823, 9824, 9827, 9828, 9829, 9830, 9831, 9832, 9835, 9837, 9842, 9843, 9845, 9846, 9849, 9850, 9852, 9853, 9854, 9856, 9857, 9861, 9867, 9869, 9872, 9873, 9876, 9878, 9880, 9882, 9885, 9887, 9888, 9889, 9890, 9895, 9896, 9900, 9902, 9903, 9904, 9906, 9908, 9909, 9913, 9914, 9919, 9927, 9928, 9929, 9930, 9932, 9934, 9936, 9941, 9945, 9946, 9948, 9950, 9955, 9956, 9959, 9960, 9962, 9964, 9966, 9967, 9969, 9972, 9973, 9974, 9976, 9977, 9978, 9979, 9980, 9982, 9983, 9984, 9986, 9987, 9989, 9990, 9991, 9993, 9994, 9995, 9996, 9997]

#t3857 connection error
tickers=[t for t in tickers if t>=3857]

tickers=yf.Tickers([f"{t}.T" for t in tickers])

for ticker in tqdm(tickers.tickers):
    try:
        name=repr(ticker).rpartition('<')[2]
        name='t'+name[:-3]
        df=ticker.history("max").reset_index()
        for x in df.iterrows():
            data=x[1].to_json(date_format="iso")
            cur.execute(f"""CREATE TABLE IF NOT EXISTS {name} (id serial PRIMARY KEY NOT NULL, data jsonb)
    """)
            cur.execute(f"""INSERT INTO {name} (data) VALUES ('{data}')
    """)
        conn.commit()
        time.sleep(1)
    except:
        conn.rollback()
        time.sleep(100)
        try:
            name=repr(ticker).rpartition('<')[2]
            name='t'+name[:-3]
            df=ticker.history("max").reset_index()
            for x in df.iterrows():
                data=x[1].to_json(date_format="iso")
                cur.execute(f"""CREATE TABLE IF NOT EXISTS {name} (id serial PRIMARY KEY NOT NULL, data jsonb)
        """)
                cur.execute(f"""INSERT INTO {name} (data) VALUES ('{data}')
        """)
            conn.commit()
            time.sleep(1)
        except Exception as e:
            print(f"Stopped at {name}")
            conn.rollback()
            raise e

cur.close()
conn.close()
print("----PSQL END----")

# do later for cleanup of 1301 and 1305
def rm_duplicate():
    pass