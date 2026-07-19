from fsm_demo import TrafficLightFSM, TrafficLightState

def test_initial_state_is_red():
    """Prueba 1: El estado inicial debe ser RED."""
    fsm = TrafficLightFSM()
    assert fsm.state == TrafficLightState.RED

def test_transition_red_to_green():
    """Prueba 2: La transición RED -> GREEN debe funcionar."""
    fsm = TrafficLightFSM()
    new_state = fsm.transition()
    assert new_state == TrafficLightState.GREEN
    assert fsm.state == TrafficLightState.GREEN

def test_full_cycle_returns_to_red():
    """Prueba 3: Después de 3 transiciones, debe volver a RED."""
    fsm = TrafficLightFSM()
    fsm.transition()  # RED -> GREEN
    fsm.transition()  # GREEN -> YELLOW
    fsm.transition()  # YELLOW -> RED
    assert fsm.state == TrafficLightState.RED

def test_cycle_count_increments():
    """Prueba 4: El contador de ciclos debe incrementarse en cada transición."""
    fsm = TrafficLightFSM()
    assert fsm._cycle_count == 0  # Nota: _cycle_count es "privado", lo accedemos para tests
    fsm.transition()
    assert fsm._cycle_count == 1
    fsm.transition()
    assert fsm._cycle_count == 2