from freemocap_adapter.ui_view_interface.operators import BLENDER_OPERATORS
from freemocap_adapter.ui_view_interface.properties import FMC_ADAPTER_PROPERTIES
from freemocap_adapter.ui_view_interface.view3d_panel import VIEW3D_PT_freemocap_adapter

USER_INTERFACE_CLASSES = [FMC_ADAPTER_PROPERTIES,
                          VIEW3D_PT_freemocap_adapter,
                          *BLENDER_OPERATORS,
                          ]
