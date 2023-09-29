import logging
import math as m
import time

from bpy.types import Operator

from freemocap_blender.layer1_core_functions.bones.enforce_rigid_bones import enforce_rigid_bones
from freemocap_blender.layer1_core_functions.load_data.load_freemocap_data import load_freemocap_data

logger = logging.getLogger(__name__)


class FREEMOCAP_ADAPTER_OT_reduce_bone_length_dispersion(Operator):
    bl_idname = 'freemocap_adapter._reduce_bone_length_dispersion'
    bl_label = 'Freemocap Adapter - Reduce Bone Length Dispersion'
    bl_description = 'Reduce the bone length dispersion by moving the tail empty and its children along the bone projection so the bone new length is within the interval'
    bl_options = {'REGISTER', 'UNDO_GROUPED'}

    def execute(self, context):
        scene = context.scene
        freemocap_adapter_tool = scene.freemocap_data_properties

        recording_path = freemocap_adapter_tool.recording_path
        if recording_path == "":
            logger.error("No recording path specified")
            return {'CANCELLED'}
        handler = load_freemocap_data(recording_path=recording_path)

        frame_number = scene.frame_current  # grab the current frame number so we can set it back after we're done
        # Get start time
        start = time.time()
        logger.info('Executing Reduce Bone Length Dispersion...')

        enforce_rigid_bones(handler=handler)

        # Get end time and print execution time
        end = time.time()
        logger.success('Finished! Execution time (s): ' + str(m.trunc((end - start) * 1000) / 1000))
        scene.frame_set(frame_number)  # set the frame back to what it was before we started
        return {'FINISHED'}