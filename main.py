from mock_api.functions import request_data, authenticate
import ...                          # import dependencies


def fetch_env_vars():
    THIS_USER = ...                  # fill in right command to fetch username from environment variables
    PASSWORD = ...                  # fill in right command to fetch password from environment variables
    return [THIS_USER, PASSWORD]


if __name__ == '__main__':
    ...                             # load environment variables

    credentials = ...               # use the fetch_env_vars function
    authenticate(credentials)
    request_data()