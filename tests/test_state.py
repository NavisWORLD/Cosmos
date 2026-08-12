from cosmos.core.state import Dyn12State, GaussianStateKernel, mix_attention, preflight


def test_dyn12_and_kernel_are_live():
    state = Dyn12State()
    states = [state.update([0.1 * (i + j) for j in range(12)]) for i in range(4)]
    kernel = GaussianStateKernel()
    matrix = kernel.matrix(states)
    checks = preflight(states, matrix)
    assert checks["state_varies"]
    assert checks["kernel_not_identity"]
    assert checks["kernel_not_all_ones"]
    mixed = mix_attention([[1.0, 0.0], [0.0, 1.0]], [[1.0, 0.5], [0.5, 1.0]], 0.2)
    assert mixed[0][1] == 0.1
