from flask import Flask, request, render_template, url_for, make_response, json
from wtforms import SelectField
import asyncio

from forms.character_filter import CharacterFilter
from service.api import StarWarsAPI
from models.starship import Starship
from storage.fake_database import FakeDatabase

app = Flask(__name__, static_url_path='/static')
db = FakeDatabase()


async def download_helper():
    SWApi = StarWarsAPI(db)
    loop = asyncio.get_event_loop()
    futures = [
        loop.run_in_executor(
            None,
            SWApi.get_starships
        ),

        loop.run_in_executor(
            None,
            SWApi.get_people
        ),

        loop.run_in_executor(
            None,
            SWApi.get_films
        ),

        loop.run_in_executor(
            None,
            SWApi.get_vehicles
        ),

        loop.run_in_executor(
            None,
            SWApi.get_planets
        ),
    ]
    await asyncio.gather(*futures)


@app.before_first_request
def download_data():
    loop = asyncio.new_event_loop()
    loop.run_until_complete(download_helper())


@app.route('/')
def index():
    ITEMS_PER_PAGE = 10
    page_query = request.args.get('page')
    order_by_query = request.args.get('orderby')
    filter_type_query = request.args.get('filter_type')
    filter_values_query = request.args.get('filter_values')

    films_group = db.get_films_filter_options()
    form = CharacterFilter()
    form.filter_values.choices = films_group

    filter_type = None
    filter_values = None
    if filter_type_query != None and filter_type_query != '':
        if filter_values_query != None and filter_values_query != '':
            filter_type = filter_type_query
            filter_values = filter_values_query

    order_by = None
    if order_by_query != None and order_by_query != '':
        page = 1
        order_by = order_by_query

    page = 1
    if page_query != None and page_query != '':
        page = int(page_query)

    people, num_pages = db.get_people(
        ITEMS_PER_PAGE, page, order_by=order_by, filter_type=filter_type, filter_value=filter_values)

    return render_template('people.html', people=people,
                           next_page=page+1 if num_pages > 0 else None,
                           previous_page=None if page == 1 else page-1,
                           current_page=page,
                           ordered_by=order_by,
                           filter_type=filter_type,
                           filter_values=filter_values,
                           form=form
                           )


@app.route('/starships')
def starships():
    return render_template('starship.html', starship=db.get_starships_ordered_by_score())


@app.route('/selectform', methods=['POST'])
def select_form():
    choices = None
    filter_type = request.form.get('filter_type')

    if filter_type == 'films':
        choices = db.get_films_filter_options()
    elif filter_type == 'startships':
        choices = db.get_starships_filter_options()
    elif filter_type == 'vehicles':
        choices = db.get_vehicles_filter_options()
    else:
        choices = db.get_planets_filter_options()

    response = make_response(json.dumps(choices))
    response.content_type = 'application/jsons'

    return response
