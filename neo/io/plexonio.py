from neo.io.basefromrawio import BaseFromRaw
from neo.rawio.plexonrawio import PlexonRawIO


class PlexonIO(PlexonRawIO, BaseFromRaw):
    """
    Class for reading the old data format from Plexon
    acquisition system (.plx)

    Note that Plexon now use a new format PL2 which is NOT
    supported by this IO.

    In some cases data there can be data after the end time indicated
    in the file's header. Plexon's SDK appears read this data.
    The recalc_end_ts parameter can be used to override the header to
    include all the data in the file.

    Compatible with versions 100 to 106.
    Other versions have not been tested.
    """
    _prefered_signal_group_mode = 'split-all'

    def __init__(self, filename, *, recalc_end_ts=False):
        PlexonRawIO.__init__(self, filename=filename, recalc_end_ts=recalc_end_ts)
        BaseFromRaw.__init__(self, filename)
