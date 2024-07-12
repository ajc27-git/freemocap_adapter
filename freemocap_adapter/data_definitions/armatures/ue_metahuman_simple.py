"""
Dictionary with the bones comforming the ue_metahuman_simple armature.
"""

armature_ue_metahuman_simple = {
    'pelvis': {
        'parent_bone' : 'root',
        'connected' : False,
        'parent_position' : 'head',
        'default_length' : 0.05,
    },
    'pelvis_r': {
        'parent_bone' : 'pelvis',
        'connected' : False,
        'parent_position' : 'head',
        'default_length' : 0,
    },
    'pelvis_l': {
        'parent_bone' : 'pelvis',
        'connected' : False,
        'parent_position' : 'head',
        'default_length' : 0,
    },
    'spine_01': {
        'parent_bone' : 'pelvis',
        'connected' : False,
        'parent_position' : 'head',
        'default_length' : 0,
    },
    'spine_04': {
        'parent_bone' : 'spine_01',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'neck_01': {
        'parent_bone' : 'spine_04',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'face': {
        'parent_bone' : 'neck_01',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'clavicle_r': {
        'parent_bone' : 'spine_04',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'clavicle_l': {
        'parent_bone' : 'spine_04',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'upperarm_r': {
        'parent_bone' : 'clavicle_r',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'upperarm_l': {
        'parent_bone' : 'clavicle_l',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'lowerarm_r': {
        'parent_bone' : 'upperarm_r',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'lowerarm_l': {
        'parent_bone' : 'upperarm_l',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'hand_r': {
        'parent_bone' : 'lowerarm_r',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'hand_l': {
        'parent_bone' : 'lowerarm_l',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'thumb_metacarpal_r': {
        'parent_bone' : 'hand_r',
        'connected' : False,
        'parent_position' : 'head',
        'default_length' : 0,
    },
    'thumb_metacarpal_l': {
        'parent_bone' : 'hand_l',
        'connected' : False,
        'parent_position' : 'head',
        'default_length' : 0,
    },
    'thumb_01_r': {
        'parent_bone' : 'thumb_metacarpal_r',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'thumb_01_l': {
        'parent_bone' : 'thumb_metacarpal_l',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'thumb_02_r': {
        'parent_bone' : 'thumb_01_r',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'thumb_02_l': {
        'parent_bone' : 'thumb_01_l',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'thumb_03_r': {
        'parent_bone' : 'thumb_02_r',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'thumb_03_l': {
        'parent_bone' : 'thumb_02_l',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'index_metacarpal_r': {
        'parent_bone' : 'hand_r',
        'connected' : False,
        'parent_position' : 'head',
        'default_length' : 0,
    },
    'index_metacarpal_l': {
        'parent_bone' : 'hand_l',
        'connected' : False,
        'parent_position' : 'head',
        'default_length' : 0,
    },
    'index_01_r': {
        'parent_bone' : 'index_metacarpal_r',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'index_01_l': {
        'parent_bone' : 'index_metacarpal_l',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'index_02_r': {
        'parent_bone' : 'index_01_r',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'index_02_l': {
        'parent_bone' : 'index_01_l',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'index_03_r': {
        'parent_bone' : 'index_02_r',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'index_03_l': {
        'parent_bone' : 'index_02_l',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'middle_metacarpal_r': {
        'parent_bone' : 'hand_r',
        'connected' : False,
        'parent_position' : 'head',
        'default_length' : 0,
    },
    'middle_metacarpal_l': {
        'parent_bone' : 'hand_l',
        'connected' : False,
        'parent_position' : 'head',
        'default_length' : 0,
    },
    'middle_01_r': {
        'parent_bone' : 'middle_metacarpal_r',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'middle_01_l': {
        'parent_bone' : 'middle_metacarpal_l',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'middle_02_r': {
        'parent_bone' : 'middle_01_r',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'middle_02_l': {
        'parent_bone' : 'middle_01_l',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'middle_03_r': {
        'parent_bone' : 'middle_02_r',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'middle_03_l': {
        'parent_bone' : 'middle_02_l',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'ring_metacarpal_r': {
        'parent_bone' : 'hand_r',
        'connected' : False,
        'parent_position' : 'head',
        'default_length' : 0,
    },
    'ring_metacarpal_l': {
        'parent_bone' : 'hand_l',
        'connected' : False,
        'parent_position' : 'head',
        'default_length' : 0,
    },
    'ring_01_r': {
        'parent_bone' : 'ring_metacarpal_r',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'ring_01_l': {
        'parent_bone' : 'ring_metacarpal_l',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'ring_02_r': {
        'parent_bone' : 'ring_01_r',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'ring_02_l': {
        'parent_bone' : 'ring_01_l',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'ring_03_r': {
        'parent_bone' : 'ring_02_r',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'ring_03_l': {
        'parent_bone' : 'ring_02_l',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'pinky_metacarpal_r': {
        'parent_bone' : 'hand_r',
        'connected' : False,
        'parent_position' : 'head',
        'default_length' : 0,
    },
    'pinky_metacarpal_l': {
        'parent_bone' : 'hand_l',
        'connected' : False,
        'parent_position' : 'head',
        'default_length' : 0,
    },
    'pinky_01_r': {
        'parent_bone' : 'pinky_metacarpal_r',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'pinky_01_l': {
        'parent_bone' : 'pinky_metacarpal_l',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'pinky_02_r': {
        'parent_bone' : 'pinky_01_r',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'pinky_02_l': {
        'parent_bone' : 'pinky_01_l',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'pinky_03_r': {
        'parent_bone' : 'pinky_02_r',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'pinky_03_l': {
        'parent_bone' : 'pinky_02_l',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'thigh_r': {
        'parent_bone' : 'pelvis_r',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'thigh_l': {
        'parent_bone' : 'pelvis_l',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'calf_r': {
        'parent_bone' : 'thigh_r',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'calf_l': {
        'parent_bone' : 'thigh_l',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'foot_r': {
        'parent_bone' : 'calf_r',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'foot_l': {
        'parent_bone' : 'calf_l',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'heel_r': {
        'parent_bone' : 'calf_r',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
    'heel_l': {
        'parent_bone' : 'calf_l',
        'connected' : True,
        'parent_position' : 'tail',
        'default_length' : 0,
    },
}
