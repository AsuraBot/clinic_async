from wtforms.validators import ValidationError
from typing import TYPE_CHECKING
import imghdr

if TYPE_CHECKING:
    from wtforms import Form, FileField


def validate_image(form: "Form", field: "FileField") -> bool:
    """Валидация картинки."""

    if field.data:
        filename = field.data.filename

        if filename[-4:] != ".jpg":
            raise ValidationError("file must be .jpg")

        if imghdr.what(field.data) != "jpeg":
            raise ValidationError("file must be a valid jpeg image.")

    field.data = field.data.stream.read()
    return True


def upload_image(form: "Form", field: "FileField") -> bool:
    """Загрузка картинки."""

    if field.data:
        pass
