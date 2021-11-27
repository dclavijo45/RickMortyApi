from controllers.apiRickMortyController import ApiRickAndMortyController

api_v1 = {
    "api": "/api/v1/",
    "api_controller": ApiRickAndMortyController.as_view("api"),
    # ----------------------------------------------------------------

    "api_by_id": "/api/v1/<id>/",
    "api_controller_by_id": ApiRickAndMortyController.as_view("api_by_id"),
    # ----------------------------------------------------------------
    
}