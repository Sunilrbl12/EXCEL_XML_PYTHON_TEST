import pandas as pd
import xml.etree.ElementTree as ET
import re

df_1 = pd.read_excel('test_input.xlsx',skiprows=4)
def sanitize_column_name(column_name):
    # Replace spaces with underscores
    sanitized_name = re.sub(r'\s', "", column_name)
    return sanitized_name

def excel_to_xml(excel_file, sheet_name, xml_file):
    # Read Excel file using pandas
    df = pd.read_excel('test_input.xlsx',skiprows=4)
    
    # Create XML root element
    root = ET.Element("Sunil_Working_XML_Data")

    # Iterate through each row in the DataFrame
    for _, row in df.iterrows():
        # Create XML sub-element for each row
        data_elem = ET.SubElement(root, "Row")

        # Iterate through each column in the row
        for col_name in df.columns:
            # Sanitize column name
            sanitized_name = sanitize_column_name(col_name)

            # Get the cell value from the row and column
            cell_value = row[col_name]

            # Check if the cell value is null or NaN
            if pd.isnull(cell_value):
                cell_value = ""

            # Create XML sub-element for each column
            col_elem = ET.SubElement(data_elem, sanitized_name)
            col_elem.text = str(cell_value)

    # Create ElementTree object
    tree = ET.ElementTree(root)

    # Write XML to file
    tree.write(xml_file)

# Usage example
excel_to_xml("data.xlsx", "Sheet1", "Output_1_Sunil.xml")
