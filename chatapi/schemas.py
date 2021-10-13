from chatapi import ma
from chatapi.models import Message, Image, Text, Video
from flask_marshmallow import base_fields


class MessageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Message
        include_fk = True
        exclude = ("content_type",)


class TextSchema(ma.SQLAlchemyAutoSchema):
    type = base_fields.Function(lambda obj: "text")

    class Meta:
        model = Text


class ImageSchema(ma.SQLAlchemyAutoSchema):
    type = base_fields.Function(lambda obj: "image")

    class Meta:
        model = Image


class VideoSchema(ma.SQLAlchemyAutoSchema):
    type = base_fields.Function(lambda obj: "video")

    class Meta:
        model = Video


# ------- Instantiate the serializers ---------------------
text_schema = TextSchema()
image_schema = ImageSchema()
video_schema = VideoSchema()
message_schema = MessageSchema()
# ---------------------------------------------------------


def serialize_query(query):
    """
    :param query: array of the type (Message, Text, Image, Video) in such order,
    where Message object is required, and only one of Text, Image, or Video objects is required.
    :return: a serialization (in a dictionary form) of the combined objects.
    """
    message, text, image, video = query
    # first, serialized the Message object
    serialized_data = message_schema.dump(message)
    if text:
        schema = text_schema
        data = text
    elif image:
        schema = image_schema
        data = image
    elif video:
        schema = video_schema
        data = video
    # second, add the serialized content object (one of Text, Image, or Video)
    serialized_data["content"] = schema.dump(data)
    return serialized_data
