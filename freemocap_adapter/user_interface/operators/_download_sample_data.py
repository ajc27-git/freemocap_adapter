import logging

import bpy
import bpy_extras

from freemocap_adapter.core_functions.load_data.get_path_to_sample_data import download_sample_data

import logging
logger = logging.getLogger(__name__)


class FMC_ADAPTER_download_sample_data(bpy.types.Operator, bpy_extras.io_utils.ImportHelper):
    bl_idname = 'fmc_adapter.download_sample_data'
    bl_label = "Download Sample Data"

    def execute(self, context):
        logger.info("Downloading sample data....")
        download_sample_data()
        return {'FINISHED'}
