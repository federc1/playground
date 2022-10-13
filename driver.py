from utilities_functions import get_arguments
from utilities_functions import install_dependencies_from_artifacts


def entrypoint(argsin: list):
    """
    The program entry point
    :params argsin: list - list of parameters such as input_prefix,
    output_prefix, run_date, run_group, parse_xl
    :return: LakeProcessing instance
    """
    args = get_arguments(argsin)

    if args.parse_xl:
        install_dependencies_from_artifacts(
            ['xlrd==1.2.0']
        )

    return "fede run"