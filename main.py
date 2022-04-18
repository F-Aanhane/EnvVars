from mock_api.functions import request_data, authenticate, reset_password
import os
import ...                          # import dependencies


def fetch_env_vars():
    USERNAME = ...                  # fill in right command to fetch username from environment variables
    PASSWORD = ...                  # fill in right command to fetch password from environment variables
    return [USERNAME, PASSWORD]


if __name__ == '__main__':
    ...                             # load environment variables

    credentials = ...               # use the fetch_env_vars function
    authenticate(credentials)
    request_data()

    # Uncomment the next line after successfully receiving data
    #reset_password(...)            # fill in your username and old password with identical data type as authenticate(),
                                    # and update your .env file accordingly from the terminal
                                    # After updating your .env file, run file again.

