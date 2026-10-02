from boutik.loyalty import points_for

def test_un_point_par_euro():
    assert points_for(0) == 0
    assert points_for(49.99) == 49

def test_points_doubles_des_100_euros():
    assert points_for(100) == 200