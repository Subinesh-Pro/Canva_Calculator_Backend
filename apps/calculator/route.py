import logging
from fastapi import APIRouter
import base64
from io import BytesIO
from apps.calculator.utils import analyze_image
from schema import ImageData
from PIL import Image

# Set up logger
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post('')
async def run(data: ImageData):
    logger.debug("Received POST request for image processing")
    
    try:
        # Decode the image
        image_data = base64.b64decode(data.image.split(",")[1])
        logger.debug(f"Decoded image data length: {len(image_data)} bytes")

        image_bytes = BytesIO(image_data)
        image = Image.open(image_bytes)
        logger.debug("Image opened successfully")

        # Log the dict_of_vars
        logger.debug(f"Received dict_of_vars: {data.dict_of_vars}")

        # Call the image analysis function
        responses = analyze_image(image, dict_of_vars=data.dict_of_vars)
        logger.debug(f"Received responses from image analysis: {responses}")

        # Return the processed result
        return {"message": "Image processed", "data": responses, "status": "success"}
    except Exception as e:
        logger.error(f"Error processing image: {str(e)}")
        return {"message": "Error processing image", "status": "failure", "error": str(e)}
