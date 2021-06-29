from collections import OrderedDict

# Create a ordered dictionary, order is important for ingestion
Fd = OrderedDict()

# From file info not in header
# INGESTION_ID is unique per table
Fd['ID'] = 'TEXT'
Fd['FILENAME'] = 'TEXT'
Fd['FILEPATH'] = 'TEXT'
Fd['INGESTION_DATE'] = 'TEXT'

# From header
Fd['NAXIS1'] = 'INT'
Fd['NAXIS2'] = 'INT'
Fd['WCSAXES'] = 'INT'
Fd['CRPIX1'] = 'FLOAT'
Fd['CRPIX2'] = 'FLOAT'
Fd['CDELT1'] = 'FLOAT'
Fd['CDELT2'] = 'FLOAT'
Fd['CUNIT1'] = 'VARCHAR(10)'
Fd['CUNIT2'] = 'VARCHAR(10)'
Fd['CTYPE1'] = 'VARCHAR(10)'
Fd['CTYPE2'] = 'VARCHAR(10)'
Fd['CRVAL1'] = 'FLOAT'
Fd['CRVAL2'] = 'FLOAT'
Fd['LONPOLE'] = 'FLOAT'
Fd['LATPOLE'] = 'FLOAT'
Fd['DATEREF'] = 'VARCHAR(20)'
Fd['MJDREFI'] = 'INT'
Fd['MJDREFF'] = 'INT'
Fd['RADESYS'] = 'VARCHAR(6)'
Fd['EQUINOX'] = 'INT'
Fd['PROJ'] = 'VARCHAR(15)'
Fd['ALPHA0'] = 'FLOAT'
Fd['DELTA0'] = 'FLOAT'
Fd['X0'] = 'FLOAT'
Fd['Y0'] = 'FLOAT'
Fd['MAPTYPE'] = 'VARCHAR(15)'
Fd['COORDREF'] = 'VARCHAR(15)'
Fd['POLAR'] = 'VARCHAR(1)'
Fd['UNITS'] = 'VARCHAR(10)'
Fd['WEIGHTED'] = 'VARCHAR(1)'
Fd['PARENT'] = 'VARCHAR(100)'
Fd['FITSNAME'] = 'VARCHAR(100)'
Fd['DATE_BEG'] = 'TEXT'
Fd['DATE_END'] = 'TEXT'
Fd['OBJECT'] = 'VARCHAR(30)'
Fd['OBS_ID'] = 'BIGINT'
Fd['BAND'] = 'VARCHAR(10)'
Fd['ISWEIGHT'] = 'VARCHAR(1)'
Fd['POLTYPE'] = 'TEXT'
Fd['OVERFLOW'] = 'FLOAT'
Fd['FLATPOL'] = 'VARCHAR(1)'
# Fd['CHECKSUM'] = 'TEXT'
