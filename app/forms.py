from flask_wtf import FlaskForm
from flask_uploads import UploadSet, IMAGES
from flask_wtf.file import FileField, FileAllowed, FileRequired

images = UploadSet('imgaes', IMAGES)

class UploadForm(FlaskForm):
    file_upload = FileField('image', validators=[FileRequired(), FileAllowed(images, 'Images only!')])
