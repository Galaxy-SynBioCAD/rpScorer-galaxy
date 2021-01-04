from rptools.rplibs import rpSBML

import argparse
import tempfile
import tarfile
import os
import glob


##
#
#
if __name__ == "__main__":
    parser = argparse.ArgumentParser('Given an SBML, extract the reaction rules and pass them to Selenzyme REST service and write the results to the SBML')
    parser.add_argument('-input', type=str)
    # parser.add_argument('-input_format', type=str, default='tar')
    parser.add_argument('-output', type=str)
    parser.add_argument('-weight_rule_score', type=float, default=0.13346271414277305)
    parser.add_argument('-weight_fba', type=float, default=0.6348436269211155)
    parser.add_argument('-weight_thermo', type=float, default=0.13167126890112002)
    parser.add_argument('-weight_rp_steps', type=float, default=0.10002239003499142)
    parser.add_argument('-max_rp_steps', type=int, default=15)
    parser.add_argument('-topX', type=int, default=10)
    parser.add_argument('-thermo_ceil', type=float, default=5000.0)
    parser.add_argument('-thermo_floor', type=float, default=-5000.0)
    parser.add_argument('-fba_ceil', type=float, default=5.0)
    parser.add_argument('-fba_floor', type=float, default=0.0)
    parser.add_argument('-pathway_id', type=str, default='rp_pathway')
    parser.add_argument('-objective_id', type=str, default='obj_fraction')
    parser.add_argument('-thermo_id', type=str, default='dfG_prime_m')
    params = parser.parse_args()

    rpsbml = rpSBML(params.input)
    rpsbml.compute_globalscore(params.weight_rp_steps,
                               params.weight_rule_score,
                               params.weight_fba,
                               params.weight_thermo,
                               params.max_rp_steps,
                               params.thermo_ceil,
                               params.thermo_floor,
                               params.fba_ceil,
                               params.fba_floor,
                               params.pathway_id,
                               params.objective_id,
                               params.thermo_id)
    rpsbml.writeSBML(params.output)
