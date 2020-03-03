import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from routes.mapper import SubMapper
from ckanext.duplicateresource import helpers

class DuplicateDataDictionaryPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)
    plugins.implements(plugins.IFacets, inherit=True)



    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'duplicateresource')


    def get_helpers(self):

        '''
        Define custom helpers (or override existing ones).
        Available as h.{helper-name}() in templates.
        '''
        return {
            'get_resources_list': helpers.get_resources_list,
            'get_resources_list_dropdown': helpers.get_resource_list_dropdown,
            'get_dataset_data_dictionary': helpers.get_dataset_data_dictionary,
            'get_latest_themes': helpers.get_latest_themes,
            'get_latest_datasets': helpers.get_latest_datasets,
            'get_latest_resources': helpers.get_latest_resources
            }

  

     # IRoutes
    def before_map(self, map):
        copy_dict_controller = 'ckanext.duplicateresource.controller:DuplicateDictionaryController'
        with SubMapper(map, controller= copy_dict_controller) as m:
            m.connect('copy_data_dict', '/dataset/{id}/dictionary/{target}/copy', action='copy_data_dict')
        return map

    def after_map(self, map):
        return map
