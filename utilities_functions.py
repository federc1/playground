import argparse
import sys
import subprocess

def get_arguments(argsin: list) -> argparse.Namespace:
    """
    Parser for the arguments passed in the Databricks notebook by the ADF
    pipeline.
    :param argsin: A list of arguments to be parsed
    :return: A argparse.Namespace with the validated arguments
    """
    arguments = argparse.ArgumentParser()
    arguments.add_argument('--parse-xl',
                            type=str,
                            choices=('CONFIRM', 'DIMENSIONS', 'FACTS'),
                            help='Flag to trigger Excel to JSON extraction')
    args, _ = arguments.parse_known_args(args=argsin)
    return args



def install_dependencies_from_artifacts(packages: list) -> None:
    for pkg in packages:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', pkg])