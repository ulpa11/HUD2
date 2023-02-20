from django.core.exceptions import ValidationError
import os
#validator to check music file
def validate_audio_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp3', '.wav', '.aac']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')

#validator to check image file
def validate_image_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.jpeg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')

#validator to check pdf file
def validate_pdf_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')