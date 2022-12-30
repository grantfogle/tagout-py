import camelot
import json
from crawlerMap import colorado
from inputs.colorado.elkCodes import elkCodes

coloradoDataTables = camelot.read_pdf(colorado['harvestStatsInput'], pages="all")

def main(dataTables):
    for table in dataTables:
        tableHeader = table.data[0][0]
        tableData = table.data
        print(tableHeader)


main(coloradoDataTables)
