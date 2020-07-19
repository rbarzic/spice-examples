#!/usr/bin/env python3
from typing import List
import argparse
import re
import logging
from pathlib import Path

coloredlogs_avail = False
try:
    import coloredlogs

    coloredlogs_avail = True
except ModuleNotFoundError:
    pass


def setup_logging(verbosity: int, excluded_modules: List[str] = []) -> None:
    """Set-up root logging level according to the number of -v options
       Logging can also be set to be quiet for imported modules
    """
    for module in excluded_modules:
        logging.getLogger("docpie").setLevel(logging.WARNING)

    logging_level = logging.WARNING
    if verbosity == 1:
        logging_level = logging.INFO
    if verbosity == 2:
        logging_level = logging.DEBUG
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(levelname)s %(message)s"  # noqa: E501
    # logging.basicConfig(format=FORMAT, level=logging_level)
    if coloredlogs_avail:
        coloredlogs.install(level=logging_level, fmt=FORMAT)
    else:
        logging.basicConfig(format=FORMAT, level=logging_level)
    # logging.basicConfig(level=logging_level)


def write_to_file_with_backup(filename: str, filecontent: str):
    """Write filecontent to file filename - If filename already exists
       create a backup
    """
    filepath = Path(filename)
    # filepath.rename(filepath.with_suffix('.bak'))
    # above  code doesn't not work very well with
    # file name like xxxx.sch.spi
    filepath.rename(str(filepath.resolve()) + ".bak")
    with filepath.open("w") as file:
        file.write(filecontent)


def get_args() -> argparse.Namespace:
    """
    Get command line arguments
    """
    parser = argparse.ArgumentParser(
        description="""
    Fix an spice netlist converted from gcshem
    """
    )

    # parser.add_argument(
    #    dest="tests", metavar="tests", nargs="*", help="Path(es) to the test"
    # )

    parser.add_argument("spice", help="Analog cell spice file ")

    parser.add_argument(
        "-v",
        "--verbosity",
        action="count",
        help="Increase output verbosity",
        default=0,
    )
    parser.add_argument("--version", action="version", version="0.1")

    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    setup_logging(args.verbosity)

    r_subckt = re.compile(r"^\.subckt\s+(\w+)\s+(.*)", re.IGNORECASE)
    r_ends = re.compile(r"^\.ends\s+(\w+)\s+(.*)", re.IGNORECASE)
    r_main_design_comment = re.compile(
        "^\*==============  Begin SPICE netlist of main design ============"  # noqa: W605,E501
    )

    file_name = args.spice
    with open(file_name) as f:
        data = f.readlines()
    first_subckt_line = 0
    first_subckt = ""
    ends = ""
    last_comment_idx = 0
    nb_subckt_lines = 0
    for idx, line in enumerate(data):
        match1 = r_subckt.search(line)
        if match1:
            nb_subckt_lines += 1
            subckt = match1.group(1)
            logging.info(f"Found subckt : {subckt}")
            if first_subckt_line == 0:
                first_subckt_line = idx
                first_subckt = subckt
            pass
        match2 = r_main_design_comment.search(line)
        if match2:
            last_comment_idx = idx
            logging.info(f"Line with relevant comment : {last_comment_idx}")
        match3 = r_ends.search(line)
        if match3:
            ends = match3.group(1)
            logging.info(f"Found ends : {ends}")
            pass

    # Now we try to see if we need to fix the file
    if nb_subckt_lines > 1 and first_subckt == ends:
        logging.info(f"File seems to need a fix... ")
        subckt_line = data[first_subckt_line]
        data.insert(last_comment_idx + 1, subckt_line)
        del data[first_subckt_line]
        result = "".join(data)
        write_to_file_with_backup(file_name, result)
    else:
        logging.info(f"No good reason found to fix the file - exiting ")
        logging.info(
            f"nb_subckt_lines = {nb_subckt_lines}, first_subckt = {first_subckt}, ends = {ends}"  # noqa: E501
        )


# Local Variables:
# eval: (blacken-mode)
# End:
