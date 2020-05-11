from wtforms import Form, SelectField


class CharacterFilter(Form):
    filter_type = SelectField(
        'Filter', choices=[('films', 'Film'), ('startships', 'Startship'),
                           ('vehicles', 'Vehicles'), ('homeworld', 'Planets')])
    filter_values = SelectField('Filter_value', coerce=int)
