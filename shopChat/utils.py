import csv

def csv_to_xml_string(csv_file_name):
    """
    Convert a CSV file to an XML string.

    Parameters:
    csv_file_name (str): The name of the CSV file.

    Returns:
    str: The XML string.
    """
    with open(csv_file_name, 'r') as file:
        csv_data = csv.reader(file)
        headers = next(csv_data)  # Get the header row
        xml_string = '<data>\n'
        for row in csv_data:
            xml_string += '  <record>\n'
            for i in range(len(row)):
                xml_string += f'    <{headers[i]}>{row[i]}</{headers[i]}>\n'
            xml_string += '  </record>\n'
        xml_string += '</data>'
    return xml_string

if __name__ == '__main__':
    print(csv_to_xml_string('fake_clothing_store_dataset.csv'))