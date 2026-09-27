# E6 paired-seed analysis

All intervals are two-sided 95% Student-t intervals across the 20 paired seeds.
Positive delta means the absolute equal-opportunity gap increased after contestation.

| Dataset | Model | Scenario | Pre EO gap | Post EO gap | Paired change (95% CI) | Positive seeds |
|---|---|---|---:|---:|---:|---:|
| adult | gradient_boosting | equal_access | 0.0310 | 0.0261 | -0.0050 [-0.0130, +0.0031] | 45% |
| adult | gradient_boosting | moderate_first_group | 0.0310 | 0.0752 | +0.0442 [+0.0252, +0.0632] | 85% |
| adult | gradient_boosting | moderate_second_group | 0.0310 | 0.0837 | +0.0527 [+0.0309, +0.0745] | 90% |
| adult | gradient_boosting | strong_first_group | 0.0310 | 0.1361 | +0.1051 [+0.0868, +0.1233] | 100% |
| adult | gradient_boosting | strong_second_group | 0.0310 | 0.1407 | +0.1097 [+0.0873, +0.1321] | 95% |
| adult | logistic | equal_access | 0.0394 | 0.0288 | -0.0105 [-0.0218, +0.0008] | 35% |
| adult | logistic | moderate_first_group | 0.0394 | 0.0954 | +0.0560 [+0.0361, +0.0759] | 95% |
| adult | logistic | moderate_second_group | 0.0394 | 0.0980 | +0.0587 [+0.0342, +0.0832] | 85% |
| adult | logistic | strong_first_group | 0.0394 | 0.1599 | +0.1205 [+0.1024, +0.1386] | 100% |
| adult | logistic | strong_second_group | 0.0394 | 0.1631 | +0.1237 [+0.0999, +0.1475] | 95% |
| adult | random_forest | equal_access | 0.0394 | 0.0321 | -0.0073 [-0.0175, +0.0029] | 35% |
| adult | random_forest | moderate_first_group | 0.0394 | 0.1082 | +0.0688 [+0.0477, +0.0899] | 90% |
| adult | random_forest | moderate_second_group | 0.0394 | 0.1178 | +0.0784 [+0.0600, +0.0967] | 95% |
| adult | random_forest | strong_first_group | 0.0394 | 0.1762 | +0.1367 [+0.1176, +0.1558] | 100% |
| adult | random_forest | strong_second_group | 0.0394 | 0.1908 | +0.1513 [+0.1321, +0.1706] | 100% |
| german | gradient_boosting | equal_access | 0.0742 | 0.0480 | -0.0263 [-0.0432, -0.0093] | 25% |
| german | gradient_boosting | moderate_first_group | 0.0742 | 0.0662 | -0.0080 [-0.0264, +0.0104] | 35% |
| german | gradient_boosting | moderate_second_group | 0.0742 | 0.0565 | -0.0177 [-0.0406, +0.0051] | 30% |
| german | gradient_boosting | strong_first_group | 0.0742 | 0.0800 | +0.0057 [-0.0143, +0.0258] | 50% |
| german | gradient_boosting | strong_second_group | 0.0742 | 0.0535 | -0.0207 [-0.0528, +0.0113] | 35% |
| german | logistic | equal_access | 0.0945 | 0.0600 | -0.0345 [-0.0507, -0.0183] | 10% |
| german | logistic | moderate_first_group | 0.0945 | 0.0807 | -0.0138 [-0.0350, +0.0075] | 35% |
| german | logistic | moderate_second_group | 0.0945 | 0.0560 | -0.0385 [-0.0618, -0.0152] | 20% |
| german | logistic | strong_first_group | 0.0945 | 0.0882 | -0.0063 [-0.0329, +0.0204] | 50% |
| german | logistic | strong_second_group | 0.0945 | 0.0700 | -0.0245 [-0.0517, +0.0027] | 40% |
| german | random_forest | equal_access | 0.0275 | 0.0200 | -0.0075 [-0.0176, +0.0026] | 20% |
| german | random_forest | moderate_first_group | 0.0275 | 0.0222 | -0.0052 [-0.0119, +0.0014] | 10% |
| german | random_forest | moderate_second_group | 0.0275 | 0.0187 | -0.0087 [-0.0189, +0.0014] | 25% |
| german | random_forest | strong_first_group | 0.0275 | 0.0250 | -0.0025 [-0.0097, +0.0047] | 15% |
| german | random_forest | strong_second_group | 0.0275 | 0.0200 | -0.0075 [-0.0171, +0.0021] | 30% |

## Variability comparison

- **adult:** median paired-change SD 0.0419; range 0.0386--0.0524.
- **german:** median paired-change SD 0.0441; range 0.0142--0.0686.
