from vehicle import vehicle_decision

def test_stop():
    assert vehicle_decision(5) == "STOP"

def test_slow_down():
    assert vehicle_decision(20) == "SLOW DOWN"

def test_move_forward():
    assert vehicle_decision(50) == "MOVE FORWARD"