# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..tracking import Tracks2Prob


def test_Tracks2Prob_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    colour=dict(argstr='-colour',
    position=3,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    fraction=dict(argstr='-fraction',
    position=3,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    out_filename=dict(argstr='%s',
    genfile=True,
    position=-1,
    ),
    output_datatype=dict(argstr='-datatype %s',
    position=2,
    ),
    resample=dict(argstr='-resample %d',
    position=3,
    units='mm',
    ),
    template_file=dict(argstr='-template %s',
    position=1,
    ),
    terminal_output=dict(nohash=True,
    ),
    voxel_dims=dict(argstr='-vox %s',
    position=2,
    sep=',',
    ),
    )
    inputs = Tracks2Prob.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_Tracks2Prob_outputs():
    output_map = dict(tract_image=dict(),
    )
    outputs = Tracks2Prob.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value