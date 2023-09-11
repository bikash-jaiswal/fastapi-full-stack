from io import BytesIO
import json
import os
from typing import Annotated, Union
from fastapi import APIRouter, File, HTTPException, UploadFile
import openai
from config import settings
from PyPDF2 import PdfFileReader, PdfReader

router = APIRouter()
openai.api_key = settings.OPENAI_API_KEY

@router.post("/files/")
async def create_file(file: Annotated[Union[bytes, None], File()] = None):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file)}
    

@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        data = json.loads(file.file.read())
        return {"filename": file.filename, "content": file.file.read()}
    
# @router.post("/compress-pdf/")
# async def lossless_pdf_compression(file:UploadFile = None):
#     """ Return lossless Compression of PDF file """
#     if not file.filename.endswith(".pdf"):
#         raise HTTPException(status_code=400, detail="Uploaded file is not a PDF")

#     try:
#         # Read the uploaded file into a BytesIO object
#         pdf_bytes = BytesIO(file.file.read())

#         # Use PyPDF2 to read the PDF
#         pdf_reader = PdfFileReader(pdf_bytes)
#         num_pages = pdf_reader.getNumPages()

#         return {"filename": file.filename, "num_pages": num_pages}

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))







    # # Save the uploaded file locally
    # with open(file.filename, "wb") as pdf_file:
    #     pdf_file.write(file.file.read())

    # Use PyPDF2 to read the PDF
    # with open(file.filename, "rb") as pdf_file:
    #     pdf_reader = PdfReader(pdf_file)
    #     num_pages = pdf_reader.numPages
    #     print(f"########### num_pages: {num_pages}")
    # pdf_reader = PdfReader(file.file.read(),bytes)
    # num_pages = pdf_reader.numPages
    # print(f"########### num_pages: {num_pages}")
    # # pdf_reader = PdfReader(file.filename)
    # # num_pages = pdf_reader.numPages
    # return {"filename": file.filename}