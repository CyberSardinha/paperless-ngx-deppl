#!/usr/bin/env python3

import os
import shutil
import deepl

auth_key = "f63c02c5-f056-..."  # Replace with your key
translator = deepl.Translator(auth_key)

# Get the source path and document file name from environment variables
document_source_path = os.environ.get('DOCUMENT_SOURCE_PATH')
document_file_name = os.environ.get('DOCUMENT_FILE_NAME')
document_archive_path = os.environ.get('DOCUMENT_ARCHIVE_PATH')

# Construct the output path
output_path = f"/usr/src/paperless/data/tmp/{document_file_name}"

try:
    # Using translate_document_from_filepath() with file paths
    translator.translate_document_from_filepath(
        document_source_path,
        output_path,
        target_lang="EN-GB",
    )

    # Overwrite the file on DOCUMENT_ARCHIVE_PATH with the translated file
    shutil.move(output_path, document_archive_path)

except deepl.DocumentTranslationException as error:
    doc_id = error.document_handle.id
    doc_key = error.document_handle.key
    error_message = f"Error after uploading {error}, id: {doc_id} key: {doc_key}"
    with open("/usr/src/paperless/data/tmp/error.txt", "w") as error_file:
        error_file.write(error_message)

except deepl.DeepLException as error:
    error_message = str(error)
    with open("/usr/src/paperless/data/tmp/error.txt", "w") as error_file:
        error_file.write(error_message)
