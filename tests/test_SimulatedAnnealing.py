# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import numpy as np

from gradient_free_optimizers import SimulatedAnnealingOptimizer

n_iter = 100


def get_score(pos_new):
    return -(pos_new[0] * pos_new[0])


space_dim = np.array([10])
init_positions = [np.array([0]), np.array([1]), np.array([2]), np.array([3])]


def _base_test(opt, init_positions):
    for nth_init in range(len(init_positions)):
        pos_new = opt.init_pos(nth_init)
        score_new = get_score(pos_new)
        opt.evaluate(score_new)

    for nth_iter in range(len(init_positions), n_iter):
        pos_new = opt.iterate(nth_iter)
        score_new = get_score(pos_new)
        opt.evaluate(score_new)


def _test_SimulatedAnnealingOptimizer(
    init_positions=init_positions, space_dim=space_dim, opt_para={}
):
    opt = SimulatedAnnealingOptimizer(init_positions, space_dim, opt_para)
    _base_test(opt, init_positions)


def test_annealing_rate():
    for annealing_rate in [1, 0.001]:
        opt_para = {"annealing_rate": annealing_rate}
        _test_SimulatedAnnealingOptimizer(opt_para=opt_para)


def test_start_temp():
    for start_temp in [0.001, 10000]:
        opt_para = {"start_temp": start_temp}
        _test_SimulatedAnnealingOptimizer(opt_para=opt_para)
