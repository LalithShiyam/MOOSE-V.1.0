#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
import torch
import logging
from moosez import constants

# This list contains the unique identifiers for all available pre-trained models.
# To make your model available, add its unique identifier to this list.
# The model name or the unique identifier has a specific syntax:
# 'clin' or 'preclin' (indicating Clinical or Preclinical),
# modality tag (like 'ct', 'pt', 'mr'), and then the tissue of interest.

AVAILABLE_MODELS = ["clin_ct_lungs",
                    "clin_ct_organs",
                    "clin_pt_fdg_tumor",
                    "clin_ct_body",
                    "preclin_mr_all"]

# This dictionary holds the pre-trained models available in MooseZ library.
# Each key is a unique model identifier following a specific syntax mentioned above
# It should have the same name mentioned in AVAILABLE_MODELS list.
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

MODELS = {
    "clin_ct_lungs": {
        "url": "https://moose-files.s3.eu-de.cloud-object-storage.appdomain.cloud/clin_ct_lungs_24062023.zip",
        "filename": "Dataset333_HMS3dlungs.zip",
        "directory": "Dataset333_HMS3dlungs",
        "trainer": "nnUNetTrainer_2000epochs_NoMirroring",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "CT_Lungs_"
    },
    "clin_ct_organs": {
        "url": "https://moose-files.s3.eu-de.cloud-object-storage.appdomain.cloud/MOOSEv2_bspline_organs23062023.zip",
        "filename": "Dataset123_Organs.zip",
        "directory": "Dataset123_Organs",
        "trainer": "nnUNetTrainer_2000epochs_NoMirroring",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "CT_Organs_"
    },
    "clin_pt_fdg_tumor": {
        "url": "https://moose-files.s3.eu-de.cloud-object-storage.appdomain.cloud/clin_pt_fdg_tumor_3_30072023.zip",
        "filename": "Dataset789_Tumor_3.zip",
        "directory": "Dataset789_Tumor_3",
        "trainer": "nnUNetTrainerDA5",
        "voxel_spacing": [3, 3, 3],
        "multilabel_prefix": "PT_FDG_Tumor_"
    },
    "preclin_mr_all": {
        "url": "https://moose-files.s3.eu-de.cloud-object-storage.appdomain.cloud/preclin_mr_14062023.zip",
        "filename": "Dataset234_Preclin.zip",
        "directory": "Dataset234_Preclin",
        "trainer": "nnUNetTrainerNoMirroring",
        "voxel_spacing": [0.15, 0.15, 0.15],
        "multilabel_prefix": "Preclin_MR_all_"
    },
    "clin_ct_body": {
        "url": "https://moose-files.s3.eu-de.cloud-object-storage.appdomain.cloud/clin_ct_body_28072023.zip",
        "filename": "Dataset001_PUMA.zip",
        "directory": "Dataset001_PUMA",
        "trainer": "nnUNetTrainer",
        "voxel_spacing": [6, 6, 6],
        "multilabel_prefix": "CT_Body_"
    },
}


# This function returns a dictionary indicating the expected modality for a given model_name, the imaging technique,
# the type of tissue to be segmented. The model_name should be the same as the unique identifier mentioned in the
# MODELS dictionary above and the AVAILABLE_MODELS list.
# If the model_name is not found, it logs an error message and returns an error message.
#
# If you add your own model, update this function to return the expected modality dictionary for your model.

def expected_modality(model_name: str) -> dict:
    """
    Display expected modality for the model.
    :param model_name: The name of the model.
    :return: The expected modality for the model.
    """
    models = {
        "clin_ct_lungs": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "Lungs"},
        "clin_ct_organs": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "Organs"},
        "clin_pt_fdg_tumor": {"Imaging": "Clinical", "Modality": "PET", "Tissue of interest": "Tumor"},
        "clin_ct_body": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "Body, Extremities"},
        "preclin_mr_all": {"Imaging": "Pre-clinical", "Modality": "MR", "Tissue of interest": "All regions"},
    }

    if model_name in models:
        model = models[model_name]
        model["Model name"] = model_name
        return model

    logging.error(" Requested model is not available. Please check the model name.")
    return {"Error": "Requested model is not available. Please check the model name."}


# This function maps the model name to the task number. This is the number that comes after Dataset in DatasetXXXX,
# after nnunetv2 training. If your model folder is Dataset123, then the task number is 123.
# It checks for known model names and returns the associated task number, this is ABSOLUTELY NEEDED for the moosez to
# work. If the provided model name doesn't match any known model, it raises an exception.

# When adding your own model, update this function to return the task number associated with your model.

def map_model_name_to_task_number(model_name: str):
    """
    Maps the model name to the task number.
    :param model_name: The name of the model.
    :return: The task number.
    """
    if model_name == "clin_ct_lungs":
        return '333'
    elif model_name == "clin_ct_organs":
        return '123'
    elif model_name == "clin_pt_fdg_tumor":
        return '789'
    elif model_name == "preclin_mr_all":
        return '234'
    elif model_name == "clin_ct_body":
        return '001'
    else:
        raise Exception(f"Error: The model name '{model_name}' is not valid.")


def check_cuda() -> str:
    """
    This function checks if CUDA is available on the device and prints the device name and number of CUDA devices
    available on the device.

    Returns:
        str: The device to run predictions on, either "cpu" or "cuda".
    """
    if not torch.cuda.is_available():
        print(
            f"{constants.ANSI_ORANGE}CUDA not available on this device. Predictions will be run on CPU.{constants.ANSI_RESET}")
        return "cpu"
    else:
        device_count = torch.cuda.device_count()
        print(
            f"{constants.ANSI_GREEN} CUDA is available on this device with {device_count} GPU(s). Predictions will be run on GPU.{constants.ANSI_RESET}")
        return "cuda"
