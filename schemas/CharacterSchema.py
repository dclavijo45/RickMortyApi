from util.Ma import ma

class CharacterSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'status', 'species', 'gender', 'image')

character = CharacterSchema()

characters = CharacterSchema(many=True)