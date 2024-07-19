from anthropic import Anthropic
from dotenv import load_dotenv

from prompts import SYSTEM_PROMPT
from utils import csv_to_xml_string
import xml.etree.ElementTree as ET
import streamlit as st

def anthropic_response(csv_path, user_query, max_tokens: int = 4096):
    print(csv_path)
    csv_data = csv_to_xml_string(csv_path)
    client = Anthropic(api_key=st.secrets["api_key"])
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": user_query}
            ]
        }
    ]
    message = client.messages.create(
        max_tokens=max_tokens,
        messages=messages,
        model="claude-3-5-sonnet-20240620",
        system=SYSTEM_PROMPT.replace(
            "{{PRODUCT_DATA}}",
            csv_data
        ),
        temperature=.1
    )
    return message.content

def parse_response(response):
    # get rid of all string not between <recommendation> and </recommendation>
    start = response.find("<recommendation>")
    end = response.find("</recommendation>")
    response = response[start:end+len("</recommendation>")]
    data = {
        "recommendations": [],
        "summary": ""
    }

    # turn in to xml
    root = ET.fromstring(response)
    for product in root.findall('product'):
        data["recommendations"].append(product.text)

    summary = root.find('summary').text.strip()
    data["summary"] = summary
    return data


if __name__ == '__main__':
    load_dotenv()
    response = anthropic_response(
            'fake_clothing_store_dataset.csv',
            "I'm looking for a casual shirt under $50 with long sleeves."
    )
    parsed_response = parse_response(response[0].text)
    print(response)