import re
from PyPDF2 import PdfReader


def extract_text_from_pdf(file):

    text = ""

    try:

        reader = PdfReader(file)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text
                text += "\n"

    except Exception as error:

        raise Exception(
            f"PDF extraction failed: {error}"
        )

    # Clean excessive whitespace
    text = re.sub(
        r"[ \t]+",
        " ",
        text
    )

    text = re.sub(
        r"\n{3,}",
        "\n\n",
        text
    )

    return text.strip()