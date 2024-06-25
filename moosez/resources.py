#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

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
from moosez import constants

# This list contains the unique identifiers for all available pre-trained models.
# To make your model available, add its unique identifier to this list.
# The model name or the unique identifier has a specific syntax:
# 'clin' or 'preclin' (indicating Clinical or Preclinical),
# modality tag (like 'ct', 'pt', 'mr'), and then the tissue of interest.

AVAILABLE_MODELS = ["clin_ct_lungs",
                    "clin_ct_organs",
                    "clin_ct_body",
                    "preclin_mr_all",
                    "clin_ct_ribs",
                    "clin_ct_muscles",
                    "clin_ct_peripheral_bones",
                    "clin_ct_fat",
                    "clin_ct_vertebrae",
                    "clin_ct_cardiac",
                    "clin_ct_digestive",
                    "preclin_ct_legs",
                    "clin_ct_all_bones_v1",
                    "clin_ct_PUMA",
                    "clin_pt_fdg_brain_v1",
                    "clin_ct_ALPACA",
                    "clin_ct_PUMA4"]

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
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_lungs_24062023.zip",
        "filename": "Dataset333_HMS3dlungs.zip",
        "directory": "Dataset333_HMS3dlungs",
        "trainer": "nnUNetTrainer_2000epochs_NoMirroring",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "Clin_CT_Lungs_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans"
    },
    "clin_ct_organs": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_organs_23062023.zip",
        "filename": "Dataset123_Organs.zip",
        "directory": "Dataset123_Organs",
        "trainer": "nnUNetTrainer_2000epochs_NoMirroring",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "Clin_CT_Organs_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans"
    },
    "preclin_mr_all": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/preclin_mr_all_05122023.zip",
        "filename": "Dataset234_minimoose.zip",
        "directory": "Dataset234_minimoose",
        "trainer": "nnUNetTrainer",
        "voxel_spacing": [0.4000000059604645, 0.4000000059604645, 0.4000000059604645],
        "multilabel_prefix": "Preclin_MR_all_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans"
    },
    "clin_ct_body": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_body_27112023.zip",
        "filename": "Dataset001_body.zip",
        "directory": "Dataset001_body",
        "trainer": "nnUNetTrainer",
        "voxel_spacing": [5, 5, 5],
        "multilabel_prefix": "Clin_CT_Body_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans"
    },
    "clin_ct_ribs": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_ribs_19032024.zip",
        "filename": "Dataset444_Ribs.zip",
        "directory": "Dataset444_Ribs",
        "trainer": "nnUNetTrainer_2000epochs_NoMirroring",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "Clin_CT_Ribs_",
        "configuration": "3d_fullres_big_patch",
        "planner": "nnUNetPlans"
    },
    "clin_ct_muscles": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_muscles_06022024.zip",
        "filename": "Dataset555_Muscles.zip",
        "directory": "Dataset555_Muscles",
        "trainer": "nnUNetTrainer_2000epochs_NoMirroring",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "Clin_CT_Muscles_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans"
    },
    "clin_ct_peripheral_bones": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_peripheral_bones_28082023.zip",
        "filename": "Dataset666_Peripheral-Bones.zip",
        "directory": "Dataset666_Peripheral-Bones",
        "trainer": "nnUNetTrainer_2000epochs_NoMirroring",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "Clin_CT_Peripheral-Bones_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans"
    },
    "clin_ct_fat": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_fat_31082023.zip",
        "filename": "Dataset777_Fat.zip",
        "directory": "Dataset777_Fat",
        "trainer": "nnUNetTrainer_2000epochs_NoMirroring",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "Clin_CT_Fat_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans"
    },
    "clin_ct_vertebrae": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_vertebrae_da5_03102023.zip",
        "filename": "Dataset111_Vertebrae.zip",
        "directory": "Dataset111_Vertebrae",
        "trainer": "nnUNetTrainer_2000_epochs_DA5NoMirroring",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "Clin_CT_Vertebrae_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans"
    },
    "clin_ct_cardiac": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_cardiac_26012024.zip",
        "filename": "Dataset888_Cardiac.zip",
        "directory": "Dataset888_Cardiac",
        "trainer": "nnUNetTrainer_2000epochs_NoMirroring",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "Clin_CT_Cardiac_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans"
    },
    "clin_ct_digestive": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_digestive_10092023.zip",
        "filename": "Dataset999_Digestive.zip",
        "directory": "Dataset999_Digestive",
        "trainer": "nnUNetTrainer_2000epochs_NoMirroring",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "Clin_CT_Digestive_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans"
    },
    "preclin_ct_legs": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/preclin_ct_legs_05122023.zip",
        "filename": "Dataset256_Preclin_leg_muscles.zip",
        "directory": "Dataset256_Preclin_leg_muscles",
        "trainer": "nnUNetTrainerNoMirroring",
        "voxel_spacing": [0.18000000715255737, 0.18000000715255737, 0.18000000715255737],
        "multilabel_prefix": "Preclin_CT_legs_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans"
    },
    "clin_ct_all_bones_v1": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_all_bones_25102023.zip",
        "filename": "Dataset600_Original_bones.zip",
        "directory": "Dataset600_Original_bones",
        "trainer": "nnUNetTrainer_2000epochs",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "Clin_CT_all_bones_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans"
    },
    "clin_ct_PUMA": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_PUMA_1k_23052024.zip",
        "filename": "Dataset002_PUMA.zip",
        "directory": "Dataset002_PUMA",
        "trainer": "nnUNetTrainer_2000epochs_NoMirroring",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "Clin_CT_PUMA_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans"
    },
    "clin_pt_fdg_brain_v1": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_fdg_pt_brain_v1_17112023.zip",
        "filename": "Dataset100_Brain_v1.zip",
        "directory": "Dataset100_Brain_v1",
        "trainer": "nnUNetTrainer_2000epochs_NoMirroring",
        "voxel_spacing": [2.03125, 2.0862598419189453, 2.0862600803375244],
        "multilabel_prefix": "Clin_PT_FDG_brain_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans"
    },
    "clin_ct_ALPACA": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_ALPACA.zip",
        "filename": "Dataset080_Alpaca.zip",
        "directory": "Dataset080_Alpaca",
        "trainer": "nnUNetTrainer_2000epochs_NoMirroring",
        "voxel_spacing": [1.5, 1.5, 1.5],
        "multilabel_prefix": "Clin_CT_ALPACA_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans"
    },
    "clin_ct_PUMA4": {
        "url": "https://enhance-pet.s3.eu-central-1.amazonaws.com/moose/clin_ct_PUMA4_06032024.zip",
        "filename": "Dataset003_PUMA4.zip",
        "directory": "Dataset003_PUMA4",
        "trainer": "nnUNetTrainer_2000epochs",
        "voxel_spacing": [4, 4, 4],
        "multilabel_prefix": "Clin_CT_PUMA4_",
        "configuration": "3d_fullres",
        "planner": "nnUNetPlans"
    }
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
        "clin_ct_body": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "Body, Arms, legs, head"},
        "preclin_mr_all": {"Imaging": "Pre-clinical", "Modality": "MR", "Tissue of interest": "All regions"},
        "clin_ct_ribs": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "Ribs"},
        "clin_ct_muscles": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "Muscles"},
        "clin_ct_peripheral_bones": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "Peripheral Bones"},
        "clin_ct_fat": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "Fat"},
        "clin_ct_vertebrae": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "Vertebrae"},
        "clin_ct_cardiac": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "Cardiac"},
        "clin_ct_digestive": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "Digestive"},
        "preclin_ct_legs": {"Imaging": "Pre-clinical", "Modality": "CT", "Tissue of interest": "Legs"},
        "clin_ct_all_bones_v1": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "All bones"},
        "clin_ct_PUMA": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "PUMA tissues"},
        "clin_pt_fdg_brain_v1": {"Imaging": "Clinical", "Modality": "PT", "Tissue of interest": "Brain regions"},
        "clin_ct_ALPACA": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "ALPACA tissues"},
        "clin_ct_PUMA4": {"Imaging": "Clinical", "Modality": "CT", "Tissue of interest": "PUMA tissues"}
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
    elif model_name == "preclin_mr_all":
        return '234'
    elif model_name == "clin_ct_body":
        return '001'
    elif model_name == "clin_ct_ribs":
        return '444'
    elif model_name == "clin_ct_muscles":
        return "555"
    elif model_name == "clin_ct_peripheral_bones":
        return "666"
    elif model_name == "clin_ct_fat":
        return "777"
    elif model_name == "clin_ct_vertebrae":
        return "111"
    elif model_name == "clin_ct_cardiac":
        return "888"
    elif model_name == "clin_ct_digestive":
        return "999"
    elif model_name == "preclin_ct_legs":
        return "256"
    elif model_name == "clin_ct_all_bones_v1":
        return "600"
    elif model_name == "clin_ct_PUMA":
        return "002"
    elif model_name == "clin_pt_fdg_brain_v1":
        return "100"
    elif model_name == "clin_ct_ALPACA":
        return "080"
    elif model_name == "clin_ct_PUMA4":
        return "003"
    else:
        raise Exception(f"Error: The model name '{model_name}' is not valid.")


def check_device() -> str:
    """
    This function checks the available device for running predictions, considering CUDA and MPS (for Apple Silicon).

    Returns:
        str: The device to run predictions on, either "cpu", "cuda", or "mps".
    """
    # Check for CUDA
    if torch.cuda.is_available():
        device_count = torch.cuda.device_count()
        print(f" CUDA is available with {device_count} GPU(s). Predictions will be run on GPU.")
        return "cuda"
    # Check for MPS (Apple Silicon) Here for the future but not compatible right now
    elif torch.backends.mps.is_available():
        print(" Apple MPS backend is available. Predictions will be run on Apple Silicon GPU.")
        return "mps"
    elif not torch.backends.mps.is_built():
        print(" MPS not available because the current PyTorch install was not built with MPS enabled.")
        return "cpu"
    else:
        print(" CUDA/MPS not available. Predictions will be run on CPU.")
        return "cpu"
