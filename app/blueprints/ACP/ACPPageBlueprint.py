from flask import Blueprint, request

from blueprints.blueprint_names import ACP_PAGE_BLUEPRINT
from controllers.ACP.PageController import PageController
from modules.Session.requestDecorators import with_session
from request_decorators import with_language
from service_container import sc

acp_page_blueprint = Blueprint(ACP_PAGE_BLUEPRINT, __name__, url_prefix='/<string:language_code>/acp/pages')


@acp_page_blueprint.route('', methods=['GET'])
@with_language
@with_session
def pages_route():
    controller: PageController = sc.get(PageController)

    return controller.pages_page_action()


@acp_page_blueprint.route('<int:page_id>', methods=['GET'])
@with_language
@with_session
def page_route(page_id: int):
    controller: PageController = sc.get(PageController)

    return controller.page_page_action(page_id)


@acp_page_blueprint.route('add', methods=['GET', 'POST'])
@with_language
@with_session
def add_page_route():
    controller: PageController = sc.get(PageController)

    match request.method:
        case 'GET':
            return controller.add_page_page_action()
        case 'POST':
            return controller.add_page_action()


@acp_page_blueprint.route('<int:page_id>/edit', methods=['GET', 'POST'])
@with_language
@with_session
def edit_page_route(page_id: int):
    controller: PageController = sc.get(PageController)

    match request.method:
        case 'GET':
            return controller.edit_page_page_action(page_id)
        case 'POST':
            return controller.edit_page_action(page_id)


@acp_page_blueprint.route('<int:page_id>/delete', methods=['POST'])
@with_language
@with_session
def delete_page_route(page_id: int):
    controller: PageController = sc.get(PageController)

    return controller.delete_page_action(page_id)


@acp_page_blueprint.route('<int:page_id>/add_translation', methods=['GET', 'POST'])
@with_language
@with_session
def add_page_translation_route(page_id: int):
    controller: PageController = sc.get(PageController)

    match request.method:
        case 'GET':
            return controller.add_page_translation_page_action(page_id)
        case 'POST':
            return controller.add_page_translation_action(page_id)


@acp_page_blueprint.route('translations/<int:translation_id>/edit', methods=['GET', 'POST'])
@with_language
@with_session
def edit_page_translation_route(translation_id: int):
    controller: PageController = sc.get(PageController)

    match request.method:
        case 'GET':
            return controller.edit_page_translation_page_action(translation_id)
        case 'POST':
            return controller.edit_page_translation_action(translation_id)
