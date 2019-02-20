from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired


class UploadForm(FlaskForm):
    file_upload = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg','png','jpeg'], 'Images only!')])
