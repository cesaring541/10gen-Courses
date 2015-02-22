import colander
import deform

class Person(colander.MappingSchema):
    username = colander.SchemaNode(colander.String(),title="username")
    password = colander.SchemaNode(
                colander.String(),
                validator=colander.Length(min=5, max=100),
                widget=deform.widget.PasswordWidget(size=20),
                description='Enter a password')
