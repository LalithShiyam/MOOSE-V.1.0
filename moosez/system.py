#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import torch
import os
import sys
import emoji
import pyfiglet
from halo import Halo
from datetime import datetime
from contextlib import contextmanager, redirect_stdout, redirect_stderr
from rich.console import Console, RenderableType
from rich.table import Table
from rich.text import Text
from rich.progress import Progress, TextColumn, BarColumn, FileSizeColumn, TransferSpeedColumn, TimeRemainingColumn
from typing import Union, Tuple, List
from moosez.constants import VERSION, ANSI_VIOLET, ANSI_RESET


# ----------------------------------------------------------------------------------------------------------------------
# Author: Lalith Kumar Shiyam Sundar
# Institution: Medical University of Vienna
# Research Group: Quantitative Imaging and Medical Physics (QIMP) Team
# Date: 13.02.2023
# Version: 2.0.0
#
# Description:
# This module contains the urls and filenames of the models and binaries that are required for the moosez.
#
# Usage:
# The variables in this module can be imported and used in other modules within the moosez to download the necessary
# binaries and models for the moosez.
#
# ----------------------------------------------------------------------------------------------------------------------

# This dictionary holds the pre-trained models available in MooseZ library.
# Each key is a unique model identifier following a specific syntax mentioned:
# 'clin' or 'preclin' (indicating Clinical or Preclinical),
# modality tag (like 'ct', 'pt', 'mr'), and then the tissue of interest.
# To make your model available, add its unique identifier to this list.
# Each value is a dictionary containing the following keys:
#    - url: The URL where the model files can be downloaded.
#    - filename: The filename of the model's zip file.
#    - directory: The directory where the model files will be extracted.
#    - trainer: The type of trainer used to train the model.
#    - voxel_spacing: The voxel spacing used in the model in the form [x, y, z], this is basically the median voxel
#    spacing generated by nnunetv2, and you can find this in the plans.json file of the model.
#    - multilabel_prefix: A prefix to distinguish between different types of labels in multi-label models.
#
# To include your own model, add a new entry to this dictionary following the above format.


class OutputManager:
    def __init__(self, verbose_console: bool, verbose_log: bool):
        self.verbose_console = verbose_console
        self.verbose_log = verbose_log

        self.console = Console(quiet=not self.verbose_console)
        self.spinner = Halo(spinner='dots', enabled=self.verbose_console)

        self.logger = None
        self.nnunet_log_filename = os.devnull

    def create_file_progress_bar(self):
        progress_bar = Progress(TextColumn("[bold blue]{task.description}"), BarColumn(bar_width=None),
                                "[progress.percentage]{task.percentage:>3.0f}%", "•", FileSizeColumn(),
                                TransferSpeedColumn(), TimeRemainingColumn(), console=self.console, expand=True)
        return progress_bar

    def create_progress_bar(self):
        progress_bar = Progress(console=self.console)
        return progress_bar

    def create_table(self, header: List[str], styles: Union[List[str], None] = None) -> Table:
        table = Table()
        if styles is None:
            styles = [None] * len(header)
        for header, style in zip(header, styles):
            table.add_column(header, style = style)
        return table

    def configure_logging(self, log_file_directory: Union[str, None]):
        if not self.verbose_log or self.logger:
            return

        if log_file_directory is None:
            log_file_directory = os.getcwd()

        timestamp = datetime.now().strftime('%H-%M-%d-%m-%Y')

        self.nnunet_log_filename = os.path.join(log_file_directory, f'moosez-v{VERSION}_nnUNet_{timestamp}.log')

        self.logger = logging.getLogger(f'moosez-v{VERSION}')
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False

        if not any(isinstance(handler, logging.FileHandler) for handler in self.logger.handlers):
            log_format = '%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
            formatter = logging.Formatter(log_format)

            log_filename = os.path.join(log_file_directory, f'moosez-v{VERSION}_{timestamp}.log')
            file_handler = logging.FileHandler(log_filename, mode='w')
            file_handler.setLevel(logging.INFO)
            file_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)

    def log_update(self, text: str):
        if self.verbose_log and self.logger:
            self.logger.info(text)

    def console_update(self, text: Union[str, RenderableType]):
        if isinstance(text, str):
            text = Text.from_ansi(text)
        self.console.print(text)

    def spinner_update(self, text: str = None):
        if self.spinner.enabled:
            self.spinner.text = text

    def spinner_stop(self):
        if self.spinner.enabled:
            self.spinner.stop()

    def spinner_start(self, text: str = None):
        if self.spinner.enabled:
            self.spinner.start(text)

    def spinner_succeed(self, text: str = None):
        if self.spinner.enabled:
            self.spinner.succeed(text)

    @contextmanager
    def manage_nnUNet_output(self):
        target_path = self.nnunet_log_filename if self.verbose_log else os.devnull
        mode = "a" if self.verbose_log else 'w'
        with open(target_path, mode) as target, redirect_stdout(target), redirect_stderr(target):
            yield

    def display_logo(self):
        """
        Display MOOSE logo

        This function displays the MOOSE logo using the pyfiglet library and ANSI color codes.

        :return: None
        """
        self.console_update(' ')
        result = ANSI_VIOLET + pyfiglet.figlet_format(" MOOSE 3.0", font="smslant").rstrip() + ANSI_RESET
        text = ANSI_VIOLET + " A part of the ENHANCE community. Join us at www.enhance.pet to build the future of" \
                             " PET imaging together." + ANSI_RESET
        self.console_update(result)
        self.console_update(text)
        self.console_update(' ')

    def display_authors(self):
        """
        Display manuscript citation

        This function displays authors for the MOOSE project.

        :return: None
        """
        self.console_update(f'{ANSI_VIOLET} {emoji.emojize(":desktop_computer:")}  AUTHORS:{ANSI_RESET}')
        self.console_update(" ")
        self.console_update(" The Three Moose-keteers 🤺: Lalith Kumar Shiyam Sundar | Sebastian Gutschmayer | Manuel Pires")
        self.console_update(" ")

    def display_doi(self):
        """
        Display manuscript citation

        This function displays the manuscript citation for the MOOSE project.

        :return: None
        """
        self.console_update(f'{ANSI_VIOLET} {emoji.emojize(":scroll:")} CITATION:{ANSI_RESET}')
        self.console_update(" ")
        self.console_update(" Fully Automated, Semantic Segmentation of Whole-Body [18F]-FDG PET/CT Images Based on Data-Centric Artificial Intelligence")
        self.console_update(" 10.2967/jnumed.122.264063")
        self.console_update(" ")
        self.console_update(" Copyright 2022, Quantitative Imaging and Medical Physics Team, Medical University of Vienna")


def check_device(output_manager: OutputManager = OutputManager(False, False)) -> Tuple[str, Union[int, None]]:
    """
    This function checks the available device for running predictions, considering CUDA and MPS (for Apple Silicon).

    Returns:
        str: The device to run predictions on, either "cpu", "cuda", or "mps".
    """
    # Check for CUDA
    if torch.cuda.is_available():
        device_count = torch.cuda.device_count()
        output_manager.console_update(f" CUDA is available with {device_count} GPU(s). Predictions will be run on GPU.")
        return "cuda", device_count
    # Check for MPS (Apple Silicon) Here for the future but not compatible right now
    elif torch.backends.mps.is_available():
        output_manager.console_update(" Apple MPS backend is available. Predictions will be run on Apple Silicon GPU.")
        return "mps", None
    elif not torch.backends.mps.is_built():
        output_manager.console_update(" MPS not available because the current PyTorch install was not built with MPS enabled.")
        return "cpu", None
    else:
        output_manager.console_update(" CUDA/MPS not available. Predictions will be run on CPU.")
        return "cpu", None


def get_virtual_env_root() -> str:
    """
    Returns the root directory of the virtual environment.

    :return: The root directory of the virtual environment.
    :rtype: str
    """
    python_exe = sys.executable
    virtual_env_root = os.path.dirname(os.path.dirname(python_exe))
    return virtual_env_root


ENVIRONMENT_ROOT_PATH: str = get_virtual_env_root()
MODELS_DIRECTORY_PATH: str = os.path.join(ENVIRONMENT_ROOT_PATH, 'models', 'nnunet_trained_models')
