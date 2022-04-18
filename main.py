from mock_api.functions import request_data, authenticate, reset_password
import ...                          # import dependencies


def fetch_env_vars():
    USERNAME = ...                  # fill in right command to fetch username from environment variables
    PASSWORD = ...                  # fill in right command to fetch password from environment variables
    return [USERNAME, PASSWORD]


if __name__ == '__main__':
    credentials = ...               # use the fetch_env_vars function
    authenticate(credentials)
    request_data()

    # Uncomment the next lines after successfully receiving data
    #reset_password(...)            # fill in your username and new password with identical data type as authenticate(),
    #request_data()                 # and update your .env file accordingly

