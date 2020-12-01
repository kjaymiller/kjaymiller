search_client = Client(
        use_https=True,
        base_endpoint=os.environ["APP_SEARCH_ENDPOINT"],
        api_key=os.environ["APP_SEARCH_API_KEY"],
    )
    search_params = {
        "engine": "kjaymiller",
    }
