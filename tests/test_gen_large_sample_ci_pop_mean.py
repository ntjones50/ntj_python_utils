# ***************************************************************
# Function written by Nathan Jones
# Pytest tests for stats_utils/gen_large_sample_ci_pop_mean.py

# 2 Pytest tests initially passed 11/15/2025
# ***************************************************************

# Imports
import sys
import os
import pytest

#--------------- Import user defined functions -------------
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "stats_utils")))
from gen_large_sample_ci_pop_mean import gen_large_sample_ci_pop_mean
#-----------------------------------------------------------

def test_gen_large_sample_ci_pop_mean():

    #------------ Test User Input Checks -----------------

    # Sample must be a list
    with pytest.raises(Exception) as e:
        gen_large_sample_ci_pop_mean(sample = 'test',
                                     approx_confidence_level_pct = 95.0)
    assert str(e.value) == "sample needs to be a list"

    # Sample must contain floats
    with pytest.raises(Exception) as e:
        gen_large_sample_ci_pop_mean(sample = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,
                                               4,5,6,7,8,9,1,2,3,4,5,6,7,8,1,2,3,4,1,1,1],
                                     approx_confidence_level_pct = 95.0)
    assert str(e.value) == "sample must contain all floats"

    # approx_confidence_level_pct must be a float
    with pytest.raises(Exception) as e:
        gen_large_sample_ci_pop_mean(sample = [1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,1.1,2.2,3.3,4.4,5.5,6.6,
                                               4.4,3.3,4.4,5.5,6.6,7.7,8.8,5.5,4.4,3.3,2.3,4.4,5.5,6.6,7.7,
                                               2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,1.1,2.2,3.3,4.4,55.5],
                                     approx_confidence_level_pct = 95)
    assert str(e.value) == "approx_confidence_level_pct must be a float"

    # The sample size must be > 40 
    with pytest.raises(Exception) as e:
        gen_large_sample_ci_pop_mean(sample = [1.1,2.2,3.3,4.4,5.5,6.6,7.7],
                                     approx_confidence_level_pct = 95.0)
    assert str(e.value) == "For this confidence interval, the sample size must be greater than 40"
    #-----------------------------------------------------

    #--------------------- Test 1 -------------------------
    test_lst = [6.627097198, 0.565611329, 5.452124555, 4.207005769, 15.11336859, 10.4948278, 10.23477158,
                13.29520304, 12.65522396, 27.84953526, 19.61734686, 17.26530962, 3.701011017, 0.938270194,  
                27.39138931, 16.23671387, 10.35305718, 14.71803803,22.47957493, 7.984420005, 20.39342184,
                9.769078952, 7.605759921, 24.62609094, 29.92986221, 12.01017461, 29.25199146, 0.851064121,
                19.76277762,6.354052648,3.104263259,27.77054194,14.91610322,17.66506237,2.735969651,4.572832961,
                0.263048731,10.73441263,16.82207707,2.614415448,26.6541474,2.856778099,24.55194643,14.84252597,
                22.79482596,7.823792147,23.19652697,20.39917025,5.119005309,13.7937206]

    out_lst = gen_large_sample_ci_pop_mean(test_lst,95.0)

    # Test lower bound
    assert out_lst[0]  == pytest.approx(10.98062138)

    # Test mean
    assert out_lst[1] == pytest.approx(13.41930682)

    # Test upper bound
    assert out_lst[2] == pytest.approx(15.85799225)
    #-------------------- End Test 1 ----------------------

    #--------------------- Test 2 -------------------------
    test_lst = [1206.212308,1087.053469,1295.823072,283.7735061,486.7996367,1178.756857,
                284.3940029,603.4362273,360.9530511,151.9812215,64.60234119,455.5523999,
                607.5155544,719.2101457,188.5406576,840.4434868,931.3734925,197.2772986,
                462.926586,878.0807452,1114.393998,1069.271466,299.4801847,663.6320434,
                645.0570195,183.1514286,995.5411558,444.6536569,332.9705439,804.297034,
                903.1781607,1192.366977,491.5323515,766.4881551,201.312159,996.7110237,
                552.0156777,435.1737825,781.623005,66.24107619,1319.446332,137.3050791,
                1062.252108,994.6295563,771.1582535,1095.751963,1096.007349,123.89426,
                830.4447977,489.622157,774.6255941,1256.15268,732.5472722]
    
    out_lst = gen_large_sample_ci_pop_mean(test_lst,75.0)

    # Test lower bound
    assert out_lst[0]  == pytest.approx(619.1968288)

    # Test mean
    assert out_lst[1] == pytest.approx(677.5025351)

    # Test upper bound
    assert out_lst[2] == pytest.approx(735.8082414)
    #--------------------- End Test 2 -------------------------
   